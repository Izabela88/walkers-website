from django.views import View
from contact.forms import ContactForm
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from contact.utility import send_email
from django.urls import reverse


class Contact(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        """Render contact page

        Args:
            request (HttpRequest): Django request object

        Returns:
            HttpResponse: Django http response
        """
        context = {"contact_form": ContactForm()}

        return render(request, "contact/contact.html", context)

    def post(self, request: HttpRequest) -> HttpResponseRedirect:
        """Post contact form endpoint

        Args:
            request (HttpRequest): DJango request object

        Returns:
            HttpResponseRedirect: Redirect page to contact GET
        """
        contact_form = ContactForm(request.POST)
        body = render_to_string("email/body.txt")

        if contact_form.is_valid():
            success = False
            if contact_form.submit_email():
                if send_email(
                    [contact_form.cleaned_data["email"]],
                    settings.EMAIL_HOST_USER,
                    body,
                    "We have got your email",
                ):
                    success = True
            if success:
                messages.success(
                    request, "Your message has been sent successfully!"
                )
            else:
                messages.error(request, "Your message couldn't be sent")
        # TODO: Handle message if form is invalid
        return HttpResponseRedirect(reverse("contact"))
