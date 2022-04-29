from django.views import View
from newsletter.forms import NewsletterUserForm
from newsletter.models import NewsletterUser
from newsletter.mailchimp_utils import subscribe
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
import datetime
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from newsletter.serializers import SubscriptionSerializer
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.sessions.backends.base import SessionBase
from django.utils import timezone


class Newsletter(View):
    def get(self, request: HttpRequest, session: SessionBase) -> HttpResponse:
        """Prepare context with possible newsletter form errors.

        Args:
            request (HttpRequest): request 'home' template
        """
        return render(request, "home/home.html")

    def post(self, request) -> HttpResponse:
        """Subscribe email address"""
        email_form = NewsletterUserForm(data=request.POST or None)
        if email_form.is_valid():
            email = email_form.cleaned_data["newsletter_email"]
            newsletter = NewsletterUser.objects.filter(email=email).first()
            if newsletter:
                newsletter.subscribe()
            else:
                data = NewsletterUser()
                data.email = email
                data.created_at = datetime.datetime.now(tz=timezone.utc)
                data.save()
            subscribe(email)
            messages.success(
                request,
                (
                    "Thank you for subscribe to our newsletter!"
                    " You will soon receive a notification on your e-mail."
                ),
            )
            return HttpResponseRedirect(reverse("home"))
        else:
            display_key_map = {
                "newsletter_email": "Newsletter Email",
            }
            for key, value in email_form.errors.items():
                display_key = display_key_map.get(key) or key
                messages.error(request, f"{display_key}: {value[0]}")

        return HttpResponseRedirect(reverse("home"))


class UpdateSubscription(APIView):
    serializer_class = SubscriptionSerializer

    def get(self, _) -> Response:
        """
        Ping method. Required by mailchimp.
        """
        return Response({}, status=status.HTTP_200_OK)

    def post(self, request) -> Response:
        """
        Update subscription webhook
        """

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            subscription = get_object_or_404(
                NewsletterUser, email=data["data"]["email"]
            )
            if data["type"] == "unsubscribed":
                subscription.is_subscribed = False
                subscription.unsubscribed_at = data["fired_at"]
                subscription.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
