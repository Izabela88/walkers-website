from django.shortcuts import render
from django.views import View
from newsletter.forms import NewsletterUserForm
from newsletter.models import NewsletterUser
from django.conf import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
from django.contrib import messages
from django.http import HttpResponseRedirect
import datetime



# Mailchimp Settings
api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_EMAIL_LIST_ID

def subscribe(email):
    """
     Contains code handling the communication to the mailchimp api
     to create a contact/member in an audience/list.
    """

    mailchimp = Client()
    mailchimp.set_config({
        "api_key": api_key,
        "server": server,
    })

    member_info = {
        "email_address": email,
        "status": "subscribed",
    }

    try:
        response = mailchimp.lists.add_list_member(list_id, member_info)
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))



class Newsletter(View):
 
    def post(self, request):
        email_form = NewsletterUserForm(data=request.POST or None)
        if email_form.is_valid():
            email = email_form.cleaned_data['newsletter_email']
            newsletter = NewsletterUser.objects.filter(email=email).first()
            if newsletter:
                if not newsletter.is_subscribed:
                    newsletter.is_subscribed = True
                    newsletter.save()
                subscribe(newsletter.email)

            else:
                data = NewsletterUser()
                data.email = email
                data.created_at = datetime.datetime.utcnow()
                data.save()                                   
            subscribe(email)
            messages.success(request, "Thank You for subscribe to our newsletter!")
            return HttpResponseRedirect('/')
        else:
            messages.error(request,
                            'Something went wrong!')

        return HttpResponseRedirect('/')

