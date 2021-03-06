from django.test import TestCase
from django.urls import reverse
from search.forms import SearchForm
from django.contrib.auth import get_user_model
from home.forms import PetsitterQuestionForm, PetsitterFormValidationError
from unittest import mock


HOME_URL = reverse("home")
REGISTER_QUESTION_URL = reverse("question")


def create_user(is_petsitter=None):
    user = get_user_model().objects.create(
        email="test@email.com", password="test1234", is_petsitter=is_petsitter
    )
    return user


class TestHomePage(TestCase):
    def test_get_home_page_return_200_when_user_not_logged_in(self):
        self.client.force_login(create_user(is_petsitter=True))
        res = self.client.get(HOME_URL)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "home/index.html")

    def test_user_missing_petsitter_question(self):
        self.client.force_login(create_user())
        res = self.client.get(HOME_URL)
        self.assertRedirects(res, REGISTER_QUESTION_URL)

    def test_get_home_page_context_data(self):
        res = self.client.get(HOME_URL)
        self.assertIsInstance(res.context["search_form"], SearchForm)


class TestRegisterQuestionPage(TestCase):
    def setUp(self):
        user = get_user_model().objects.create(
            email="test@email.com", password="test1234"
        )
        self.client.force_login(user)

    def test_get_register_question_return_200(self):
        res = self.client.get(REGISTER_QUESTION_URL)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "home/question.html")

    def test_register_question_includes_correct_form(self):
        res = self.client.get(REGISTER_QUESTION_URL)
        self.assertIsInstance(
            res.context["form_petsitter"], PetsitterQuestionForm
        )

    @mock.patch.object(PetsitterQuestionForm, "save", return_value=True)
    def test_post_happy_flow_redirect_to_home(self, mock_petsitter_form):
        res = self.client.post(REGISTER_QUESTION_URL)
        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.url, HOME_URL)

    @mock.patch.object(
        PetsitterQuestionForm, "save", side_effect=PetsitterFormValidationError
    )
    def test_post_form_invalid_redirect_to_question(self, mock_petsitter_form):
        res = self.client.post(REGISTER_QUESTION_URL)
        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.url, REGISTER_QUESTION_URL)


class TestRegisterQuestionForm(TestCase):
    def test_petsitter_question_form_updates_user_to_petsitter(self):
        petsitter_q_form = PetsitterQuestionForm(data={"is_petsitter": True})
        user = petsitter_q_form.save(create_user())
        self.assertTrue(user.is_petsitter)

    def test_petsitter_question_form_updates_user_to_not_petsitter(self):
        petsitter_q_form = PetsitterQuestionForm(data={})
        user = petsitter_q_form.save(create_user())
        self.assertFalse(user.is_petsitter)

    @mock.patch.object(PetsitterQuestionForm, "is_valid", return_value=False)
    def test_petsitter_form_raises_validation_error(self, is_valid_mock):
        petsitter_q_form = PetsitterQuestionForm(data={})
        with self.assertRaises(PetsitterFormValidationError):
            petsitter_q_form.save(create_user())
