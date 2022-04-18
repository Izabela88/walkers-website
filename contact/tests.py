from django.test import TestCase
from django.urls import reverse
from contact.forms import ContactForm
from contact import utility
from unittest import mock
from django.contrib.messages import get_messages

CONTACT_URL = reverse("contact")


def mock_true(*args, **kwargs):
    return True


def mock_false(*args, **kwargs):
    return False


class TestContactPage(TestCase):
    def test_get_contact_page_return_200(self):
        res = self.client.get(CONTACT_URL)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "contact/contact.html")

    def test_get_contact_page_context_data(self):
        res = self.client.get(CONTACT_URL)
        self.assertIsInstance(res.context["contact_form"], ContactForm)

    @mock.patch("contact.views.ContactForm")
    def test_post_method_redirects_to_contact(self, mock_contact_form):
        mock_contact_form.return_value.is_valid = mock_true
        payload = {
            "full_name": "Gandalf the Grey",
            "email": "thegandalf@gmail.com",
            "message": "Hi Frodo! We need to destroy the ring!",
        }
        res = self.client.post(CONTACT_URL, data=payload)
        self.assertRedirects(res, CONTACT_URL)

    @mock.patch("contact.views.send_email", mock_true)
    @mock.patch("contact.views.ContactForm")
    def test_post_method_create_success_message(self, mock_contact_form):
        mock_contact_form.return_value.is_valid = mock_true
        mock_contact_form.return_value.submit_email = mock_true
        mock_contact_form.return_value.cleaned_data = {
            "email": "mock@email.com"
        }
        res = self.client.post(CONTACT_URL)
        messages = list(get_messages(res.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), "Your message has been sent successfully!"
        )

    @mock.patch("contact.views.send_email", mock_true)
    @mock.patch("contact.views.ContactForm")
    def test_post_method_create_error_message(self, mock_contact_form):
        mock_contact_form.return_value.is_valid = mock_true
        mock_contact_form.return_value.submit_email = mock_false
        mock_contact_form.return_value.cleaned_data = {
            "email": "mock@email.com"
        }
        res = self.client.post(CONTACT_URL)
        messages = list(get_messages(res.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Your message couldn't be sent")


class TestContactForm(TestCase):
    def format_message_mock(self):
        return "Hi Frodo! We need to destroy the ring!"

    def test_happy_flow_contact_form(self):
        form_data = {
            "full_name": "Gandalf the Grey",
            "email": "thegandalf@gmail.com",
            "message": "Hi Frodo! We need to destroy the ring!",
        }
        contact_form = ContactForm(data=form_data)
        self.assertTrue(contact_form.is_valid())

    def test_required_data_missing(self):
        contact_form = ContactForm(data={})
        self.assertFalse(contact_form.is_valid())
        self.assertIn("full_name", contact_form.errors)
        self.assertIn("email", contact_form.errors)
        self.assertIn("message", contact_form.errors)

    def test_formatting_email_message(self):
        expected_message = """
            From:\n\t\tSaruman\n
            Email:\n\t\tsaruman@gmail.com\n
            Message:\n\t\tHi, Sauron! Gandalf is up to something.\n"""
        form_data = {
            "full_name": "Saruman",
            "email": "saruman@gmail.com",
            "message": "Hi, Sauron! Gandalf is up to something.",
        }
        contact_form = ContactForm(data=form_data)
        contact_form.is_valid()
        self.assertEquals(contact_form.format_message(), expected_message)

    @mock.patch("contact.forms.send_email")
    @mock.patch(
        "contact.forms.ContactForm.format_message", format_message_mock
    )
    def test_submit_email_pass_value_from_send_email_fn(self, mock_send_email):
        form_data = {
            "full_name": "Saruman",
            "email": "saruman@gmail.com",
            "message": "Hi, Sauron! Gandalf is up to something.",
        }
        contact_form = ContactForm(data=form_data)
        contact_form.is_valid()
        mock_send_email.return_value = True
        self.assertTrue(contact_form.submit_email())


class TestContactUtility(TestCase):
    @mock.patch("contact.utility.send_mail")
    def test_send_email_happy_flow_return_true(self, mock_send_mail):
        mock_send_mail.return_value = True
        self.assertTrue(
            utility.send_email(
                ["gandalf@gmail.com"],
                "frodo@gmail.com",
                "Hi. We are ok with Sam!",
                "Hi! Gandalf.",
            )
        )

    @mock.patch("contact.utility.send_mail")
    def test_send_email_return_false_when_bad_header_error_raised(
        self, mock_send_mail
    ):
        mock_send_mail.side_effect = utility.BadHeaderError()
        self.assertFalse(
            utility.send_email(
                ["gandalf@gmail.com"],
                "frodo@gmail.com",
                "Hi. We are ok with Sam!",
                "Hi! Gandalf.",
            )
        )
