from django.test import TestCase
from search.forms import SearchForm
from django.urls import reverse
from django.contrib.auth import get_user_model
from unittest import mock
from walker_profile.models import WalkerUser
from reviews.models import PetsitterReview
from walker_profile.utility import geocode
from django.contrib.messages import get_messages


SEARCH_URL = reverse("petsitter_profiles")
HOME_URL = reverse("home")


def mock_true(*args, **kwargs):
    return True


def mock_false(*args, **kwargs):
    return False


def get_petsitter_profile_url(id=1):
    return reverse("petsitter_profile", kwargs={"id": id})


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


class TestSearchPage(TestCase):
    @mock.patch("search.views.geocode.get_postcode_coordinates")
    @mock.patch("search.views.geocode.get_users_within_radius")
    @mock.patch("search.views.WalkerUser")
    @mock.patch("search.views.SearchForm")
    def test_search_return_filtered_users(
        self,
        mock_search_form,
        mock_walker_user,
        mock_user_within_radius,
        mock_postcode_coordinates,
    ):
        user_one = get_user_model().objects.create(
            email="gandalf@gmail.com", password="magicwand"
        )
        user_two = get_user_model().objects.create(
            email="frodo@gmail.com", password="ring123"
        )

        PetsitterReview.objects.create(
            stars=5,
            user=user_one,
            reviewer=user_two,
            is_visible=True,
            is_admin_approved=True,
        )

        mock_postcode_coordinates.return_value = (10, 15)
        mock_walker_user.return_value.search_petsitter = True
        mock_user_within_radius.return_value = [user_two, user_one]
        mock_search_form.return_value.is_valid = mock_true
        mock_search_form.return_value.cleaned_data = {
            "postcode": "WS10 9JA",
            "area": 20,
        }
        res = self.client.post(SEARCH_URL)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "search/petsitters_search_results.html")
        self.assertEqual(len(res.context["search_results"]), 2)
        self.assertEqual(res.context["search_results"][0], (user_one, (5, 1)))
        self.assertEqual(res.context["search_results"][1], (user_two, (0, 0)))

    @mock.patch("search.views.geocode.get_postcode_coordinates")
    @mock.patch("search.views.SearchForm")
    def test_reverse_user_to_home_if_postcode_not_found(
        self, mock_search_form, mock_postcode_coordinates
    ):
        mock_search_form.return_value.is_valid = mock_true
        mock_postcode_coordinates.side_effect = geocode.GeoCodeError

        res = self.client.post(SEARCH_URL)
        messages = list(get_messages(res.wsgi_request))

        self.assertRedirects(res, HOME_URL + "#searching-section")
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "We couldn't find your postcode!")

    @mock.patch("search.views.SearchForm")
    def test_correct_message_and_session_when_form_is_invalid(
        self, mock_search_form
    ):
        mock_search_form.return_value.is_valid = mock_false
        mock_search_form.return_value.errors = {"error": True}

        res = self.client.post(SEARCH_URL)
        messages = list(get_messages(res.wsgi_request))
        expected_error = self.client.session["petsitter_search_form_errors"]

        self.assertRedirects(res, HOME_URL + "#searching-section")
        self.assertEqual(expected_error, {"error": True})
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Something went wrong!")
