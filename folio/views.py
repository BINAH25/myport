from django.shortcuts import render, redirect
from .models import Message
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')


def send(request):
    name = request.POST.get('name')
    email = request.POST['email']
    project = request.POST['project']
    message = request.POST['message']

    user = Message.objects.create(name=name, email=email, project=project, message=message)
    user.save()

    messages.add_message(request, messages.INFO, 'Message Successfully sent.')

    return redirect("folio:index")