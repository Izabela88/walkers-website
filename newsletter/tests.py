from django.test import TestCase
from django.urls import reverse
from newsletter.forms import NewsletterUserForm
from unittest import mock
from django.contrib.messages import get_messages
import datetime
from newsletter.models import NewsletterUser
import json

NEWSLETTER_URL = reverse("newsletter")
HOME_URL = reverse("home")
UPDATE_SUBSCRIPTION_URL = reverse("update_subscription")


def mock_true(*args, **kwargs):
    return True


def mock_false(*args, **kwargs):
    return False


class TestNewsletterForm(TestCase):
    def test_happy_flow_newsletter_form(self):
        form_data = {
            "newsletter_email": "sylvanas@gmail.com",
        }
        newsletter_form = NewsletterUserForm(data=form_data)
        self.assertTrue(newsletter_form.is_valid())

    def test_required_data_missing(self):
        newsletter_form = NewsletterUserForm(data={})
        self.assertFalse(newsletter_form.is_valid())
        self.assertIn("newsletter_email", newsletter_form.errors)


class TestNewsletterPage(TestCase):
    @mock.patch("newsletter.views.subscribe")
    @mock.patch.object(NewsletterUserForm, "save", return_value=True)
    def test_post_happy_flow_redirect_to_home(self, _, mock_subscribe):
        mock_subscribe.return_value = True
        res = self.client.post(NEWSLETTER_URL)
        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.url, HOME_URL)

    @mock.patch("newsletter.views.subscribe")
    @mock.patch.object(NewsletterUserForm, "save", return_value=True)
    def test_post_method_redirects_to_home(self, _, mock_subscribe):
        mock_subscribe.return_value = True
        payload = {
            "newsletter_email": "thegandalf@gmail.com",
        }
        res = self.client.post(NEWSLETTER_URL, data=payload)
        self.assertRedirects(res, HOME_URL)

    @mock.patch("newsletter.views.subscribe")
    @mock.patch("newsletter.views.NewsletterUserForm")
    def test_post_method_create_success_message(
        self, mock_newsletter_form, mock_subscribe
    ):
        mock_subscribe.return_value = True
        mock_newsletter_form.return_value.is_valid = mock_true
        mock_newsletter_form.return_value.cleaned_data = {
            "newsletter_email": "mock@email.com"
        }
        res = self.client.post(NEWSLETTER_URL)
        messages = list(get_messages(res.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), "Thank You for subscribe to our newsletter!"
        )

    @mock.patch("newsletter.views.subscribe")
    @mock.patch("newsletter.views.NewsletterUserForm")
    def test_post_method_create_error_message(
        self, mock_newsletter_form, mock_subscribe
    ):
        mock_subscribe.return_value = True
        mock_newsletter_form.return_value.is_valid = mock_false
        mock_newsletter_form.return_value.errors = {"Error": "Test Error"}
        res = self.client.post(NEWSLETTER_URL)
        messages = list(get_messages(res.wsgi_request))
        session = self.client.session
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Something went wrong!")
        self.assertEqual(session["email_form_errors"], {"Error": "Test Error"})


class TestUpdateSubscriptionAPI(TestCase):
    def test_ping_endpoint(self):
        res = self.client.get(UPDATE_SUBSCRIPTION_URL)
        self.assertEqual(res.status_code, 200)

    def test_unsubscribe_email(self):
        NewsletterUser.objects.create(
            email="gandalf@gmail.com", is_subscribed=True
        )
        payload = {
            "type": "unsubscribed",
            "fired_at": str(datetime.datetime.utcnow()),
            "data": {"id": "123", "email": "gandalf@gmail.com"},
        }
        res = self.client.post(
            UPDATE_SUBSCRIPTION_URL,
            data=json.dumps(payload),
            content_type='application/json',
        )
        updated_use = NewsletterUser.objects.filter(
            email="gandalf@gmail.com"
        ).first()
        self.assertEqual(res.status_code, 200)
        self.assertFalse(updated_use.is_subscribed)

    def test_unsubscribe_email_invalid_payload(self):
        NewsletterUser.objects.create(
            email="gandalf@gmail.com", is_subscribed=True
        )
        payload = {
            "type": "unsubscribed",
            "fired_at": str(datetime.datetime.utcnow()),
        }
        res = self.client.post(
            UPDATE_SUBSCRIPTION_URL,
            data=json.dumps(payload),
            content_type='application/json',
        )
        self.assertEqual(res.status_code, 400)
