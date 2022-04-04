from django.test import TestCase
from django.urls import reverse
from newsletter.forms import NewsletterUserForm

NEWSLETTER_URL = reverse("newsletter")


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
