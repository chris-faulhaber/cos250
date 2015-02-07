from datetime import datetime
import os
import subprocess
import uuid
from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import View
import shutil
from rest_framework_jwt.utils import jwt_encode_handler
from models import Submission, Assignment, Line, Part
from django.template import RequestContext
from forms import UploadFileForm, LoginForm
from django.views import generic
from nand2tetris import settings


def _get_completed_parts(parts, user):
    completed_parts = []
    for part in parts:
            if part.submission_set.all().filter(owner=user).exists():
                completed_parts.append(part)
    return completed_parts


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class AssignmentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Assignment

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(AssignmentDetailView, self).get_context_data(**kwargs)
        upload_form = UploadFileForm
        parts = [part for part in Part.objects.filter(assignment=self.object).order_by('order')]
        all_points = [part.weight for part in parts]
        total_points_possible = sum(all_points)
        completed_parts = _get_completed_parts(parts, user)
        incomplete_parts = [part for part in parts if part not in completed_parts]
        submission_points_list = []

        context['form'] = upload_form
        context['completed_parts'] = [model_to_dict(part) for part in completed_parts]
        for part in context['completed_parts']:
            submission = Submission.objects.filter(part=part['id'], owner=user).order_by('-awarded_points')[0]
            part['submission'] = model_to_dict(submission)
            submission_points_list.append(submission.awarded_points)

        context['incomplete_parts'] = [model_to_dict(part) for part in incomplete_parts]
        current_assignment_score = int((sum(submission_points_list)/float(total_points_possible)) * 100)
        context['current_assignment_score'] = current_assignment_score
        upload_form.base_fields['part'].queryset = Part.objects.filter(assignment=self.object).order_by('order')

        return context


class AssignmentListView(LoginRequiredMixin, generic.ListView):
    model = Assignment

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AssignmentListView, self).get_context_data(**kwargs)

        # Add in the grade
        for assignment in context['assignment_list']:
            grade = assignment.grade(user=self.request.user)
            if grade > 0:
                assignment.the_grade = "%02.02f%%" % grade
            else:
                assignment.the_grade = ''

        return context


# Create your views here.
class SubmissionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Submission

    def get_context_data(self, **kwargs):
        context = super(SubmissionDetailView, self).get_context_data(**kwargs)
        context['lines'] = Line.objects.filter(submission=context['submission']).order_by('line_number')

        return context

    def get_queryset(self):
        return Submission.objects.filter(owner=self.request.user)


 # Create your views here.
class StaffSubmissionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Submission
    template = 'submit/submission_detail.html'

    def get_context_data(self, **kwargs):
        context = super(StaffSubmissionDetailView, self).get_context_data(**kwargs)
        context['lines'] = Line.objects.filter(submission=context['submission']).order_by('line_number')

        return context

    def get_queryset(self):
        return Submission.objects.filter(pk=self.kwargs['pk'])


def _submit_part(part, content):
    temp_dir = '/tmp/{0}'.format(uuid.uuid4().hex)
    script = os.path.join(settings.RESOURCES_DIR, part.tester.script)
    test = os.path.join(settings.RESOURCES_DIR, part.test_script)
    test_dest = os.path.join(temp_dir, test.split('/')[-1])

    #create tmp dir and build content
    os.mkdir(temp_dir)
    shutil.copyfile(test, test_dest)

    #copy extras
    for extra in part.extra_files.split(','):
        extra = os.path.join(settings.RESOURCES_DIR, extra)
        shutil.copyfile(extra, temp_dir + '/' + extra.split('/')[-1])

    #save inbound file
    destination = open('%s/%s' % (temp_dir, part.submit_filename), 'w')
    for line in content:
        destination.write(line)

    destination.close()

    cmd = [script, test_dest]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=temp_dir)

    stdout = process.stdout.read()
    stderr = process.stderr.read()

    while process.returncode is None:
        process.poll()

    #retreive output
    if part.output_file:
        try:
            source = open('%s/%s' % (temp_dir, part.output_file), 'r')
            output = source.read()
        except Exception:
            return stderr, ''

    shutil.rmtree(temp_dir)
    results = stderr or stdout or 'No OUTPUT'
    results = results.rstrip()

    return results, output


@login_required
def upload(request):

    # by default we display the form.
    form = UploadFileForm()  # A empty, unbound form

    # Handle file upload
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if not form.is_valid():
            field_error = form.errors.keys()[0]
            error_msg = str(form.errors[field_error][0])
            error_msg = "{0}: {1}".format(field_error, error_msg)
            messages.error(request, error_msg)
            return redirect(request.META['HTTP_REFERER'])
        part = Part.objects.get(pk=request.POST['part'])

        submit = Submission()
        submit.owner = request.user
        submit.submission_date = datetime.now()
        submit.part = part
        submit.awarded_points = 0  # initially

        submit.save()

        uploaded_file = request.FILES['docfile']
        content = uploaded_file.readlines()

        count = 0
        found_parts = False
        for one_line in content:
            line = Line()

            if not part.allow_builtin and 'BUILTIN' in one_line:
                error_msg = "The usage of 'BUILTIN' is not allowed. Line {0}".format(count+1)
                messages.error(request, error_msg)
                return redirect(request.META['HTTP_REFERER'])

            if part.nand_only and found_parts and '(' in one_line and not 'Nand' in one_line:
                error_msg = "You may use only Nand's. Line {0}".format(count+1)
                messages.error(request, error_msg)
                return redirect(request.META['HTTP_REFERER'])

            if 'PARTS:' in one_line:
                found_parts = True

            # note the truncation and let's try to submit...
            if len(one_line) > 1024:
                line.truncated = True
                one_line = one_line[:1024]

            line.line_number = count
            stripped = one_line.rstrip()  # remove line ends
            line.line = stripped
            line.submission = submit
            line.save()
            count += 1

        # Ok we are ready to test.
        submit.test_results, submit.output = _submit_part(part, content)
        if submit.test_results == submit.part.expected_result:
            submit.awarded_points = submit.part.weight
        else:
            submit.awarded_points = 0

        submit.output = submit.output[:4000] + ' ... TRUNCATED ... ' \
            if len(submit.output) > 4096 else submit.output

        submit.test_results = submit.test_results[:1000] + ' ... TRUNCATED ... ' \
            if len(submit.test_results) > 1024 else submit.test_results

        submit.save()

        return HttpResponseRedirect(
            reverse('submission', args=(submit.id,))
        )

    return redirect(request.META['HTTP_REFERER'])


class LoginView(View):
    template = 'submit/home.html'

    def get(self, request):
        if request.user.is_authenticated():
            return redirect(reverse('assignment_list'))
        form = LoginForm()
        context = RequestContext(request, {'auth_form': form})
        return render(request, self.template, context)

    def post(self, request):
        if request.method == 'POST':
            data = {
                'username': request.POST['username'],
                'password': request.POST['password']
            }
            form = LoginForm(data=data)
            if form.is_valid():
                login(request, form.get_user())
                # Success
                return redirect(reverse('assignment_list'))
            else:
                # Failure
                return redirect('/')
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


class StudentListView(generic.ListView):
    model = User
    template_name = 'submit/user_list.html'
    queryset = User.objects.filter(is_staff=False)


class StudentAssignmentView(generic.View):
    template_name = 'submit/assignment_submissions_list.html'

    def get(self, request, user_pk, part_pk=None):
        user = User.objects.get(id=user_pk)

        if part_pk:
            part = Part.objects.get(id=part_pk)
            submissions = Submission.objects.filter(owner=user, part=part).order_by('-submission_date')
        else:
            submissions = Submission.objects.filter(owner=user).order_by('-submission_date')

        submits = []
        for submit in submissions:
            submits.append({'pk': submit.pk, 'awarded_points': submit.awarded_points,
                            'name': submit.part.name,
                            'submission_date': submit.submission_date})

        if len(submissions) > 0:
            context = RequestContext(request, {'submissions': submits})
            return HttpResponse(render(request, self.template_name, context))
        else:
            #TODO something here, return to prior page or show error...
            pass


class StudentDetailView(generic.View):
    template_name = 'submit/grade_view.html'

    def get(self, request, user_pk):
        user = User.objects.get(id=user_pk)
        assignments = Assignment.objects.all()
        grades = []

        for assignment in assignments:
            grade_dict = {'grade': assignment.grade(user), 'assignment': model_to_dict(assignment),
                          'parts': assignment.part_grades(user)}
            grades.append(grade_dict)

        context = RequestContext(request, {'grades': grades, 'student': model_to_dict(user)})
        return HttpResponse(render(request, self.template_name, context))


class AssignmentGradesView(View):
    template_name = 'submit/assignment_grades.html'

    def get(self, request):
        jwt_payload = {'username': request.user.username, 'password': request.user.password}
        jwt = jwt_encode_handler(jwt_payload)
        context = RequestContext(request, {'jwt': jwt})
        return  HttpResponse(render(request, self.template_name, context))