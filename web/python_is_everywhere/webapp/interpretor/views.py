from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.template import engines
import bleach
from urllib.parse import urlencode
from django.contrib import messages
from django.contrib.messages import get_messages


URLS_QUEUE = []


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('interpretor')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required()
def index(request):
    messages_stored = get_messages(request)
    template = loader.get_template('index.html')
    context = {
        'title': 'Python interpretor',
        'messages': messages_stored
    }
    return HttpResponse(template.render(context, request))


@login_required()
def report(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        python = request.POST.get('python')
        if not (python and len(python) > 0):
            messages.add_message(request, messages.ERROR, 'Python code is empty')
        elif len(URLS_QUEUE) < 20:
            params = {
                'm': message,
                'u': request.user.username,
                'p': python
            }
            query_string = urlencode(params)
            URLS_QUEUE.append('http://host/admin?' + query_string)
            messages.add_message(request, messages.SUCCESS, 'Message successfully delivered')
        else:
            messages.add_message(request, messages.ERROR, 'Admins have already received a lot of messages, try again in a few minutes, sorry')
    return redirect('interpretor')


@login_required()
def admin(request):
    if request.user.username == 'admin':
        html_message = bleach.clean(request.GET.get('m'))
        engine = engines["django"]
        template = engine.from_string(
            """
                <html lang="en">
                  <head>
                    <meta charset="utf-8" />
                    <meta name="viewport" content="width=device-width,initial-scale=1" />
                    <title>{{ title }}</title>
                  </head>
    
                  <body>
                    <h2>Report by : {{ username }}</h2>
                    <p>Message : %s</p>
                    <iframe src="/?python={{ python }}"></iframe>
                  </body>
                </html>
            """ % html_message)
        context = {
            'title': 'User report',
            'username': request.GET.get('u'),
            'python': request.GET.get('p')
        }
        return HttpResponse(template.render(context, request))
    return redirect('interpretor')


@login_required()
def bot(request):
    if request.user.username == 'admin':
        if len(URLS_QUEUE) != 0:
            return HttpResponse(URLS_QUEUE.pop(0))
        else:
            return HttpResponse('')
    return redirect('interpretor')


