from django.test import TestCase
from search.forms import SearchForm
from django.urls import reverse
from django.contrib.auth import get_user_model
from unittest import mock
from walker_profile.models import WalkerUser


def mock_true(*args, **kwargs):
    return True


def mock_false(*args, **kwargs):
    return False


def get_petsitter_profile_url(id=1):
    return reverse("petsitter_profile", kwargs={"id": id})


PETSITTER_PROFILES_LIST = reverse("petsitter_profiles")


class TestSearchForm(TestCase):
    def test_happy_flow_search_form(self):
        form_data = {
            "postcode": "WV22JA",
            "care_type": "walk",
            "dog_size": "small",
            "area": "10 miles",
        }
        search_form = SearchForm(data=form_data)
        self.assertTrue(search_form.is_valid())

    def test_required_data_missing(self):
        search_form = SearchForm(data={})
        self.assertFalse(search_form.is_valid())


class TestPetsitterProfileUserLogOut(TestCase):
    def test_get_return_401_template(self):
        res = self.client.get(get_petsitter_profile_url(id=1))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "401.html")


class TestPetsitterProfilePage(TestCase):
    def setUp(self):
        user = get_user_model().objects.create(
            email="barlog@gmail.com", password="ilikedestroying1509"
        )
        self.client.force_login(user)

    @mock.patch.object(WalkerUser, "get_service_details")
    @mock.patch.object(WalkerUser, "reviews_rating")
    def test_get_petsitter_profile_page_context_data(
        self, mock_service_details, mock_review_rating
    ):
        services = [{"some_service": True}]
        mock_review_rating.return_value = services
        mock_service_details.return_value = 5, 3
        res = self.client.get(get_petsitter_profile_url(id=1))
        self.assertEqual(res.context["services"], services)
        self.assertEqual(res.context["reviews_data"]["avg_rating"], 5)
        self.assertEqual(res.context["reviews_data"]["reviews_qty"], 3)
