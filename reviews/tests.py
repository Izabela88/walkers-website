from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from reviews.forms import PetsitterReviewForm
from unittest import mock
from django.contrib.messages import get_messages


def get_review_url(id=1):
    return reverse("review", kwargs={"id": id})


def get_petsitter_profile_url(id=1):
    return reverse("petsitter_profile", kwargs={"id": id})


def mock_true(*args, **kwargs):
    return True


def mock_false(*args, **kwargs):
    return False


class TestReviewPageUserLogIn(TestCase):
    def setUp(self):
        user = get_user_model().objects.create(
            email="test@email.com", password="test1234"
        )
        self.client.force_login(user)

    def test_get_reviews_return_200(self):
        res = self.client.get(get_review_url(id=1))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "reviews/review.html")

    def test_user_can_not_self_review(self):
        res = self.client.post(get_review_url(id=1))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "403.html")

    @mock.patch("reviews.views.PetsitterReviewForm")
    def test_post_method_create_success_message(self, mock_review_form):
        mock_review_form.return_value.is_valid = mock_true
        res = self.client.post(get_review_url(id=2))
        messages = list(get_messages(res.wsgi_request))
        expected_msg = (
            "Thank you for your review! Your review will be visible after"
            " approval by the website administrator"
        )
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), expected_msg)

    @mock.patch("reviews.views.PetsitterReviewForm")
    def test_post_method_create_error_message(self, mock_review_form):
        mock_review_form.return_value.is_valid = mock_false
        mock_review_form.return_value.errors = {"Error": "Test Error"}
        self.client.post(get_review_url(id=2))


class TestReviewPageUserLogOut(TestCase):
    def test_post_return_401_template(self):
        res = self.client.post(get_review_url(id=1))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "401.html")

    def test_get_return_401_template(self):
        res = self.client.get(get_review_url(id=1))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "401.html")


class TestReviewForm(TestCase):
    def test_happy_flow_review_form(self):
        form_data = {
            "stars": 5,
            "description": "Sam cooked the best soup ever!",
        }
        review_form = PetsitterReviewForm(data=form_data)
        self.assertTrue(review_form.is_valid())

    def test_required_data_missing(self):
        review_form = PetsitterReviewForm(data={})
        self.assertFalse(review_form.is_valid())
