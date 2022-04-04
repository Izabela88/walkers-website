from django.test import TestCase
from django.urls import reverse
from contact.forms import ContactForm
from unittest import mock

CONTACT_URL = reverse("contact")


class TestContactPage(TestCase):

    def test_get_contact_page_return_200(self):
        res = self.client.get(CONTACT_URL)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'contact/contact.html')
    
    def test_get_contact_page_context_data(self):
        res = self.client.get(CONTACT_URL)
        self.assertIsInstance(res.context["contact_form"], ContactForm)


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
    @mock.patch("contact.forms.ContactForm.format_message", format_message_mock)
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
