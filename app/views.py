from django.shortcuts import render
from .models import Student, Comment, Member
from .forms import UploadFileForm
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import reverse, redirect
from django.core.exceptions import PermissionDenied, SuspiciousOperation


# Create your views here.

def index(request):
    students = Student.objects.all()
    return render(request, 'app/index.html', {
        'students': students,
        'count': 5,
        'code': '<h2>Code<h2>    '
    })


def temp(request):
    return render(request, 'app/home.html', {'title': 'New title'})


def home(request):
    return render(request, 'app/sub_home.html')


def learn_template(request):
    context = {
        'a_str': 'abcdefg',
        'a_list': ['abcdef'],
        'a_int': 10,
        'a_float': 1.6,
        'a_dict': {'key': 'value'},
        'list': list,
    }
    return render(request, 'app/learn_template.html', context)


def upload_file_success(request):
    return HttpResponse('Upload file successfully.')


def upload_file(request):
    def handle_uploaded_file(f):
        with open(f'UploadedFiles/{datetime.now()}', 'wb+') as destination:
            for chunk in f.chunks():
                print(chunk)
                destination.write(chunk)

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect(reverse('upload_file_success'))
    else:
        return render(request, 'app/upload_file.html', {'form': UploadFileForm()})


def when404(request, exception):
    return render(request, '404.html')


def history(request):
    return HttpResponse('history')


def edit(request):
    return HttpResponse('edit')


def discuss(request):
    return HttpResponse('discuss')


def permissions(request):
    return HttpResponse('permissions')


def learn_redirect(request):
    return HttpResponseRedirect(reverse('app:home'))


def when403(request, exception):
    return HttpResponse('Permission denied.')


def when400(request, exception):
    return HttpResponse('bad request.')


def test_error(request):
    1 / 0


def post_comment(request):
    if request.session.get('has_commented', False):
        return HttpResponse('You\'already commented.')
    Comment.objects.create(content=request.POST['comment'])
    request.session['has_commented'] = True
    return HttpResponse('Thanks for your comment!')


# def login(request):
#     m = Member.objects.get(username=request.POST['username'])
#     if m.password == request.POST['password']:
#         request.session['member_id'] = m.id
#         return HttpResponse('You\'re logged in.')
#     else:
#         return HttpResponse('Your username and password didn\'t match.')

def login(request):
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            return HttpResponse('You\'re logged in.')
        else:
            return HttpResponse('Please enable cookies and try again.')
    request.session.set_test_cookie()
    return HttpResponse('??????')


def logout(request):
    try:
        del request.session['member']
    except KeyError:
        pass
    return HttpResponse('You\'re logged out.')
