from datetime import datetime
import os, subprocess
from django.contrib.auth import login, logout
from django.shortcuts import render, render_to_response, redirect
from django.views import generic
from django.views.generic import View
from models import Person, Submission, Line, Assignment, Attendee
from django.template import RequestContext
from forms import UploadFileForm, LoginForm


# Create your views here.
class SubmissionListView(generic.ListView):
    template_name = 'submit/submission_list.html'
    model = Submission

    def get_context_data(self, **kwargs):
        context = super(SubmissionListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        user = Person.objects.first()  # TODO until we setup security...
        return Submission.objects.filter(owner=user).order_by('submission_date')


# Create your views here.
class SubmissionDetailView(generic.DetailView):
    model = Submission

    def get_context_data(self, **kwargs):
        context = super(SubmissionDetailView, self).get_context_data(**kwargs)
        context['lines'] = Line.objects.filter(submission=context['submission']).order_by('line_number')

        return context

    def get_queryset(self):
        user = Person.objects.first()  # TODO until we setup security...
        return Submission.objects.filter(owner=user)


def index(request):
    person_list = Person.objects.all()
    context = RequestContext(request, {
        'personList': person_list
    })

    return render(request, 'submit/index.html', context)


def upload(request):
    user = Person.objects.first()  # TODO until we setup security...

    # by default we display the form.
    form = UploadFileForm()  # A empty, unbound form

    # Handle file upload
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = Assignment.objects.get(pk=request.POST['assignments'])

            submit = Submission()
            submit.owner = user  # TODO until we setup security...
            submit.submission_date = datetime.now()
            submit.assignment = assignment

            uploaded_file = request.FILES['docfile']
            content = uploaded_file.readlines()

            #TODO limit the size of file!
            if len(content) > 1000:
                pass

            # piped_file = ''.join(content)
            cmd = ['java',
                   '-classpath "${CLASSPATH}:bin/classes:BuiltIn:bin/lib/Hack.jar:bin/lib/HackGUI.jar:bin/lib/Simulators.jar:bin/lib/SimulatorsGUI.jar:bin/lib/Compilers.jar" HardwareSimulatorMain "And.tst"']
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            outstd = process.stdout.read()
            print outstd

            outerr = process.stderr.read()
            print outerr

            submit.test_results = outstd or outerr
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

            return render_to_response(
                'submit/success.html',
                {'form': form},
                context_instance=RequestContext(request)
            )

    enrolled = Attendee.objects.filter(student=user)
    form.fields['assignments'].queryset = Assignment.objects.filter(course__in=enrolled)

    form.submissions = Submission.objects.filter(owner=user).order_by('-submission_date')[:5]

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
                return redirect('/upload')
            else:
                # Failure
                return redirect('/')
        return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')