from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect

# Create your views here.

def card_base(request):
    return render(request, 'cardtemp/base.html', {})


def mail(request):
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST['Email']
        subject = request.POST['Subject'] + " from " + email
        message = request.POST['Message']
        mailto = ['asinitskiy@ukr.net']
        test = email + name + subject + message
        if subject and message and email:
                try:
                    msg = EmailMessage(subject, message, 'support@myserve.com.ua', ['asinitskiy@ukr.net'])
                    msg.send()
                    return HttpResponseRedirect('/#home')
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')

        else:
                # In reality we'd use a form class
                # to get proper validation errors.
                return HttpResponse('Make sure all fields are entered and valid.')
