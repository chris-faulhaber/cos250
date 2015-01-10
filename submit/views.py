from datetime import datetime
import os
import subprocess
import uuid
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.forms import model_to_dict, ModelChoiceField
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.views.generic import View, ListView
import shutil
from models import Submission, Assignment, Line, Part, AssignmentGrade
from django.template import RequestContext
from forms import UploadFileForm, LoginForm
from django.views import generic
from nand2tetris import settings


def get_completed_parts(parts, user):
    completed_parts = []
    for part in parts:
            if part.submission_set.all().filter(owner=user).exists():
                completed_parts.append(part)
    return completed_parts


class AssignmentDetailView(generic.DetailView):
    model = Assignment

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(AssignmentDetailView, self).get_context_data(**kwargs)
        upload_form = UploadFileForm
        parts = [part for part in Part.objects.filter(assignment=self.object).order_by('order')]
        all_points = [part.weight for part in parts]
        total_points_possible = sum(all_points)
        completed_parts = get_completed_parts(parts, user)
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

    #todo do we need?
    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(AssignmentDetailView, self).dispatch(*args, **kwargs)


class AssignmentListView(generic.ListView):
    model = Assignment


class SubmissionListView(generic.ListView):
    template_name = 'submit/submission_list.html'
    model = Submission

    def get_context_data(self, **kwargs):
        context = super(SubmissionListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Submission.objects.filter(owner=self.request.user).order_by('submission_date')


# Create your views here.
class SubmissionDetailView(generic.DetailView):
    model = Submission

    def get_context_data(self, **kwargs):
        context = super(SubmissionDetailView, self).get_context_data(**kwargs)
        context['lines'] = Line.objects.filter(submission=context['submission']).order_by('line_number')

        return context

    def get_queryset(self):
        return Submission.objects.filter(owner=self.request.user)

@login_required
def index(request):
    person_list = User.objects.all()
    context = RequestContext(request, {
        'personList': person_list
    })

    return render(request, 'submit/index.html', context)


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
        process.communicate()

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
        if form.is_valid():
            part = Part.objects.get(pk=request.POST['part'])

            submit = Submission()
            submit.owner = request.user
            submit.submission_date = datetime.now()
            submit.part = part

            uploaded_file = request.FILES['docfile']
            content = uploaded_file.readlines()

            submit.test_results, submit.output = _submit_part(part, content)
            if submit.test_results == submit.part.expected_result:
                submit.awarded_points = submit.part.weight
            else:
                submit.awarded_points = 0

            submit.save()

            count = 0
            for one_line in content:
                line = Line()
                line.line_number = count
                stripped = one_line.rstrip()
                line.line = stripped
                line.submission = submit
                line.save()
                count += 1

            return HttpResponseRedirect(
                reverse('submission', args=(submit.id,))
            )

    form.submissions = Submission.objects.filter(owner=request.user).order_by('-submission_date')[:5]

    # Render list page with the documents and the form
    return render_to_response(
        'submit/upload.html',
        {'form': form},
        context_instance=RequestContext(request)
    )


class LoginView(View):
    template = 'submit/home.html'

    def get(self, request):
        if request.user.is_authenticated():
            return upload(request)
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


class StudentGradeView(generic.View):
    template_name = 'submit/grade_view.html'

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        assignments = Assignment.objects.all()
        grades = []
        for assignment in assignments:
            for assignment_grade in assignment.assignmentgrade_set.filter(user=user):
                grade, part_grades = assignment_grade.get_grade()
                grade_dict = {'grade': grade, 'assignment': assignment.description, 'parts': part_grades}
                grades.append(grade_dict)

        context = RequestContext(request, {'grades': grades, 'student': model_to_dict(user)})
        return HttpResponse(render(request, self.template_name, context))