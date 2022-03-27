from django.views import View
from contact.forms import ContactForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from contact.utility import send_email


class Contact(View):
    def get(self, request):
        context = {'contact_form': ContactForm()}

        return render(request, 'contact/contact.html', context)

    def post(self, request):
        context = {}
        contact_form = ContactForm(request.POST)
        email = settings.EMAIL_HOST_USER
        body = render_to_string('email/body.txt')

        if contact_form.is_valid():
            form_data = {
                'full_name': contact_form.cleaned_data['full_name'],
                'email': contact_form.cleaned_data['email'],
                'message': contact_form.cleaned_data['message'],
            }
            message = '''
            From:\n\t\t{}\n
            Email:\n\t\t{}\n
            Message:\n\t\t{}\n
            '''.format(
                form_data['full_name'],
                form_data['email'],
                form_data['message'],
            )
            if send_email(
                [email], form_data['email'], message, 'You got a mail!'
            ):
                print('Your message has been sent successfully')
                messages.success(
                    request, 'Your message has been sent successfully!'
                )
                send_email(
                    [form_data['email']],
                    settings.EMAIL_HOST_USER,
                    body,
                    'We have got your email',
                )
            else:
                messages.error(request, "Your message couldn't be sent")
                print("Your message couldn't be sent")
                return render(request, "contact/contact.html", context)

        return HttpResponseRedirect('/contact')
