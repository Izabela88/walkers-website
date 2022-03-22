from django.shortcuts import render
from django.views import View
from contact.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings


class Contact(View):
    def get(self, request):
        context = {
            'contact_form': ContactForm()
        }
        
        return render(request, 'contact/contact.html', context)

    def post(self, request):       
        context = {}
        contact_form =  ContactForm(request.POST)
        email = settings.EMAIL_HOST_USER
        
        if contact_form.is_valid():
            form_data = {
            'full_name':contact_form.cleaned_data['full_name'],
            'email':contact_form.cleaned_data['email'],
            'message':contact_form.cleaned_data['message'],
        }
            message = '''
            From:\n\t\t{}\n
            Email:\n\t\t{}\n
            Message:\n\t\t{}\n
            '''.format(form_data['full_name'], form_data['email'], form_data['message'])
            try:
                send_mail('You got a mail!', message, '', [email])
                messages.success(request, 'Your message has been sent '
                                 'successfully!')
            except BadHeaderError:
                messages.error(request, "Your message couldn't be sent")  
                return render(request, "contact/contact.html", context)
        return HttpResponseRedirect('/contact')