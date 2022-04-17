from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from unittest import mock
from django.contrib.messages import get_messages
from reviews.forms import PetsitterReviewForm
from reviews.models import PetsitterReview
from walker_profile.models import AddressDetails
from walker_profile.utility import geocode


def get_user_profile_url(id=1):
    return reverse("user_profile", kwargs={"id": id})


def get_user_profile_reviews_url(user_id=1):
    return reverse("reviews", kwargs={"id": user_id})


def get_walker_user_review_url(user_id=1, review_id=1):
    return reverse(
        "walker_user_review",
        kwargs={"user_id": user_id, "review_id": review_id},
    )


def get_delete_walker_user_review_url(user_id=1, review_id=1):
    return reverse(
        "delete_review", kwargs={"user_id": user_id, "review_id": review_id}
    )


def mock_true(*args, **kwargs):
    return True


def mock_false(*args, **kwargs):
    return False


class TestWalkerProfilePageUserLogIn(TestCase):
    def setUp(self):
        user = get_user_model().objects.create(
            email='elrond@gmail.com', password='arvena0008'
        )
        self.client.force_login(user)

    def test_get_return_403_template(self):
        res = self.client.get(get_user_profile_url(id=2))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, '403.html')

    def test_get_user_profile_return_200(self):
        res = self.client.get(get_user_profile_url(id=1))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'user_profile/user_profile.html')


class TestWalkerProfilePageUserLogOut(TestCase):
    def test_get_return_401_template(self):
        res = self.client.get(get_user_profile_url(id=1))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, '401.html')

    def test_post_return_401_template(self):
        res = self.client.post(get_user_profile_url(id=1))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, '401.html')


class TestWalkerUserReviewPageUserLogOut(TestCase):
    def test_get_return_401_template(self):
        res = self.client.get(
            get_walker_user_review_url(user_id=1, review_id=1)
        )
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, '401.html')

    def test_post_return_401_template(self):
        res = self.client.post(
            get_walker_user_review_url(user_id=1, review_id=1)
        )
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, '401.html')

    def test_delete_return_401_template(self):
        res = self.client.delete(
            get_delete_walker_user_review_url(user_id=1, review_id=1)
        )
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, '401.html')


class TestWalkerUserReviewPageUserLogIn(TestCase):
    def setUp(self):
        user = get_user_model().objects.create(
            email='legolas@email.com', password='ilovemybow2000'
        )
        self.client.force_login(user)

    # @mock.patch.object(PetsitterReview, "save", id=1, reviewer_id=1)
    # @mock.patch(
    #     "walker_profile.views.get_object_or_404",
    #     return_value=PetsitterReview(),
    # )
    # def test_get_walker_user_review_return_200(self, *args):
    #     res = self.client.get(get_walker_user_review_url(user_id=1, review_id=1))
    #     self.assertEqual(res.status_code, 200)
    #     self.assertTemplateUsed(res, 'user_profile/edit_review.html')

    def test_get_return_403_template(self):
        res = self.client.get(
            get_walker_user_review_url(user_id=2, review_id=1)
        )
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, '403.html')

    def test_post_return_403_template(self):
        res = self.client.post(
            get_walker_user_review_url(user_id=2, review_id=1)
        )
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, '403.html')

    def test_delete_return_403_template(self):
        res = self.client.delete(
            get_delete_walker_user_review_url(user_id=2, review_id=1)
        )
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, '403.html')

    @mock.patch.object(
        PetsitterReviewForm,
        "save",
        returned_value=True,
    )
    @mock.patch.object(
        PetsitterReviewForm,
        "is_valid",
        returned_value=True,
    )
    @mock.patch.object(
        PetsitterReviewForm,
        "has_changed",
        returned_value=True,
    )
    @mock.patch.object(PetsitterReview, "save", id=1, reviewer_id=1)
    @mock.patch(
        "walker_profile.views.get_object_or_404",
        return_value=PetsitterReview(),
    )
    def test_post_happy_flow_redirect_to_walker_user_review(self, *args):
        res = self.client.post(
            get_walker_user_review_url(user_id=1, review_id=1)
        )
        self.assertEqual(res.status_code, 302)
        self.assertEqual(
            res.url, get_walker_user_review_url(user_id=1, review_id=1)
        )

    @mock.patch("reviews.views.PetsitterReviewForm")
    @mock.patch.object(PetsitterReview, "save", id=1, reviewer_id=1)
    @mock.patch(
        "walker_profile.views.get_object_or_404",
        return_value=PetsitterReview(),
    )
    def test_post_method_create_error_message(self, mock_review_form, *args):
        mock_review_form.return_value.is_valid = mock_false
        mock_review_form.return_value.errors = {}
        res = self.client.post(
            get_walker_user_review_url(user_id=1, review_id=1)
        )
        messages = list(get_messages(res.wsgi_request))
        session = self.client.session
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Something went wrong!")
        self.assertEqual(session["walker_user_review_form_errors"], {})

    # @mock.patch.object(PetsitterReview, "delete", id=1, reviewer_id=1)
    # @mock.patch(
    #     "walker_profile.views.get_object_or_404",
    #     return_value=PetsitterReview(),
    # )
    # def test_delete_happy_flow_redirect_to_walker_user_reviews(self, *args):
    #     data = {
    #         "id": 1,
    #         "description": "Smeagol can't cook!",
    #         "_method": "delete"
    #     }
    #     res = self.client.delete(
    #         get_delete_walker_user_review_url(user_id=1, review_id=1),
    #         data,
    #         header={"Content-Type": "application/json"}
    #     )
    #     self.assertRedirects(res, get_user_profile_reviews_url(user_id=1))


class TestWalkerUserReviewListPageUserLogIn(TestCase):
    def setUp(self):
        user = get_user_model().objects.create(
            email='gimmly@email.com', password='ilovemyaxe2000'
        )
        self.client.force_login(user)

    def test_get_reviews_list_return_200(self):
        res = self.client.get(get_user_profile_reviews_url(user_id=1))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'user_profile/reviews_list.html')


class TestWalkerUserReviewListPageUserLogOut(TestCase):
    def test_get_return_401_template(self):
        res = self.client.get(get_user_profile_reviews_url(user_id=1))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, '401.html')


class ResponseStub:
    def __init__(self, ok=True, data=None):
        self.ok = ok
        self.data = data

    def json(self):
        return self.data


class TestGeocodeUtils(TestCase):
    @mock.patch("walker_profile.utility.geocode.requests")
    def test_postcodes_api_return_invalid_status_code(self, requests_mock):
        requests_mock.get.return_value = ResponseStub(ok=False)
        with self.assertRaises(geocode.GeoCodeError):
            geocode.get_postcode_coordinates("WX10 9SS")

    @mock.patch("walker_profile.utility.geocode.requests")
    def test_postcodes_api_response_is_missing_coordinates(
        self, requests_mock
    ):
        data = {"result": {}}
        requests_mock.get.return_value = ResponseStub(ok=True, data=data)
        with self.assertRaises(geocode.GeoCodeError):
            geocode.get_postcode_coordinates("WX10 9SS")

    @mock.patch("walker_profile.utility.geocode.requests")
    def test_postcodes_api_happy_flow_response(self, requests_mock):
        data = {
            "result": {
                "longitude": 123,
                "latitude": 456,
            }
        }
        requests_mock.get.return_value = ResponseStub(ok=True, data=data)

        longitude, latitude = geocode.get_postcode_coordinates("WX10 9SS")
        self.assertEqual(longitude, 123)
        self.assertEqual(latitude, 456)

    def test_return_users_only_within_given_radius(self):
        center_point = (66.54185013423182, 25.842665542284724)
        address_in_radius = AddressDetails.objects.create(
            latitude=66.4982785106706, longitude=25.70529992490776
        )
        address_out_radius = AddressDetails.objects.create(
            latitude=66.4854694342929, longitude=25.714669467882725
        )
        user_in_radius = get_user_model().objects.create(
            email='legolas@email.com',
            password='ilovemybow2000',
            address_details_id=address_in_radius.id,
        )
        user_out_radius = get_user_model().objects.create(
            email='orc123@email.com',
            password='123',
            address_details_id=address_out_radius.id,
        )
        users = [user_in_radius, user_out_radius]
        filtered_users = geocode.get_users_within_radius(
            center_point[1], center_point[0], users, 5
        )
        self.assertEqual(len(filtered_users), 1)
        self.assertEqual(filtered_users[0], user_in_radius)
