from django.test import TestCase
from django.urls import reverse

ABOUT_URL = reverse("about")


class TestAboutPage(TestCase):
    def test_about_page_return_200(self):
        res = self.client.get(ABOUT_URL)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "about/about.html")
