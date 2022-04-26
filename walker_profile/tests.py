from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from unittest import mock
from django.contrib.messages import get_messages
from reviews.forms import PetsitterReviewForm
from reviews.models import PetsitterReview
from walker_profile.models import (
    AddressDetails,
    PetsitterDetails,
    ServiceDetails,
    ServiceTypes,
    WalkerUser,
)
from walker_profile.utility import geocode, form_handlers


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


def create_user(email, password, address_details_id=None, is_petsitter=True):
    user = get_user_model().objects.create(
        email=email,
        password=password,
        address_details_id=address_details_id,
        is_petsitter=is_petsitter,
    )
    return user


def mock_true(*args, **kwargs):
    return True


def mock_false(*args, **kwargs):
    return False


class ResponseStub:
    def __init__(self, ok=True, data=None):
        self.ok = ok
        self.data = data

    def json(self):
        return self.data


class MessagesListStub(list):
    def add(self, *args):
        self.append((args))
        return self


class HttpRequestStub:
    def __init__(self, session=None, post_data=None, files_data=None):
        self.user = create_user(
            email="legolas@email.com", password="ilovemybow2000"
        )
        self.POST = post_data or None
        self.FILES = files_data or None
        self.session = session or {}
        self._messages = MessagesListStub()


class TestWalkerProfilePageUserLogIn(TestCase):
    def setUp(self):
        user = create_user(email="elrond@gmail.com", password="arvena0008")
        self.client.force_login(user)

    def test_get_return_403_template(self):
        res = self.client.get(get_user_profile_url(id=2))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "403.html")

    def test_get_user_profile_return_200(self):
        res = self.client.get(get_user_profile_url(id=1))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "user_profile/user_profile.html")


class TestWalkerProfilePageUserLogOut(TestCase):
    def test_get_return_401_template(self):
        res = self.client.get(get_user_profile_url(id=1))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "401.html")

    def test_post_return_401_template(self):
        res = self.client.post(get_user_profile_url(id=1))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "401.html")


class TestWalkerUserReviewPageUserLogOut(TestCase):
    def test_get_return_401_template(self):
        res = self.client.get(
            get_walker_user_review_url(user_id=1, review_id=1)
        )
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "401.html")

    def test_post_return_401_template(self):
        res = self.client.post(
            get_walker_user_review_url(user_id=1, review_id=1)
        )
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "401.html")

    def test_delete_return_401_template(self):
        res = self.client.delete(
            get_delete_walker_user_review_url(user_id=1, review_id=1)
        )
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "401.html")


class TestWalkerUserReviewPageUserLogIn(TestCase):
    def setUp(self):
        user = create_user(
            email="legolas@email.com", password="ilovemybow2000"
        )
        self.client.force_login(user)

    def test_get_return_403_template(self):
        res = self.client.get(
            get_walker_user_review_url(user_id=2, review_id=1)
        )
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "403.html")

    def test_post_return_403_template(self):
        res = self.client.post(
            get_walker_user_review_url(user_id=2, review_id=1)
        )
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "403.html")

    def test_delete_return_403_template(self):
        res = self.client.delete(
            get_delete_walker_user_review_url(user_id=2, review_id=1)
        )
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "403.html")

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


class TestWalkerUserReviewListPageUserLogIn(TestCase):
    def setUp(self):
        user = create_user(email="gimmly@email.com", password="ilovemyaxe2000")
        self.client.force_login(user)

    def test_get_reviews_list_return_200(self):
        res = self.client.get(get_user_profile_reviews_url(user_id=1))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "user_profile/reviews_list.html")


class TestWalkerUserReviewListPageUserLogOut(TestCase):
    def test_get_return_401_template(self):
        res = self.client.get(get_user_profile_reviews_url(user_id=1))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "401.html")


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
        user_in_radius = create_user(
            email="legolas@email.com",
            password="ilovemybow2000",
            address_details_id=address_in_radius.id,
        )
        user_out_radius = create_user(
            email="orc123@email.com",
            password="123",
            address_details_id=address_out_radius.id,
        )
        users = [user_in_radius, user_out_radius]
        filtered_users = geocode.get_users_within_radius(
            center_point[1], center_point[0], users, 5
        )
        self.assertEqual(len(filtered_users), 1)
        self.assertEqual(filtered_users[0], user_in_radius)


class TestFormHandlers(TestCase):
    """Django messages levels:
    DEBUG = 10
    INFO = 20
    SUCCESS = 25
    WARNING = 30
    ERROR = 40
    """

    @mock.patch("walker_profile.utility.form_handlers.UpdateWalkerProfileForm")
    def test_profile_form_handler_happy_flow(self, update_profile_mock):
        update_profile_mock.return_value.is_valid = mock_true
        update_profile_mock.return_value.save = mock_true
        update_profile_mock.return_value.has_changed = mock_true
        request_stub = HttpRequestStub()
        form_handlers._profile_form_handler(request_stub)
        self.assertEqual(len(request_stub._messages), 1)
        self.assertEqual(
            request_stub._messages[0][1],
            "Your profile is updated successfully",
        )
        self.assertEqual(request_stub._messages[0][0], 25)

    @mock.patch("walker_profile.utility.form_handlers.UpdateWalkerProfileForm")
    def test_profile_form_add_errors_to_session_when_form_is_invalid(
        self, update_profile_mock
    ):
        update_profile_mock.return_value.is_valid = mock_false
        update_profile_mock.return_value.errors = {"error": True}

        request_stub = HttpRequestStub()
        form_handlers._profile_form_handler(request_stub)

        self.assertEqual(len(request_stub._messages), 0)
        self.assertEqual(
            request_stub.session["profile_form_errors"], {"error": True}
        )

    @mock.patch(
        "walker_profile.utility.form_handlers.geocode.get_postcode_coordinates"
    )
    @mock.patch("walker_profile.utility.form_handlers.WalkerAddressForm")
    def test_address_form_handler_happy_flow(
        self, walker_address_mock, get_postcode_coords_mock
    ):
        address_details = AddressDetails.objects.create(
            latitude=66.4854694342929, longitude=25.714669467882725
        )
        get_postcode_coords_mock.return_value = (
            address_details.longitude,
            address_details.latitude,
        )
        walker_address_mock.return_value.is_valid = mock_true
        walker_address_mock.return_value.save = mock_true
        walker_address_mock.return_value.has_changed = mock_true
        walker_address_mock.return_value.instance = address_details

        request_stub = HttpRequestStub()
        form_handlers._address_form_handler(request_stub)

        self.assertEqual(
            request_stub.user.address_details_id, address_details.id
        )
        self.assertEqual(len(request_stub._messages), 1)
        self.assertEqual(
            request_stub._messages[0][1],
            "Your address is updated successfully",
        )
        self.assertEqual(request_stub._messages[0][0], 25)

    @mock.patch("walker_profile.utility.form_handlers.WalkerAddressForm")
    def test_address_form_handler_add_errors_to_session_when_form_is_invalid(
        self, walker_address_mock
    ):
        walker_address_mock.return_value.is_valid = mock_false
        walker_address_mock.return_value.errors = {"error": True}

        request_stub = HttpRequestStub()
        form_handlers._address_form_handler(request_stub)

        self.assertEqual(len(request_stub._messages), 0)
        self.assertEqual(
            request_stub.session["address_form_errors"], {"error": True}
        )

    @mock.patch(
        "walker_profile.utility.form_handlers.geocode.get_postcode_coordinates"
    )
    @mock.patch("walker_profile.utility.form_handlers.WalkerAddressForm")
    def test_address_form_send_error_message_when_geocode_error_raised(
        self, walker_address_mock, get_postcode_coords_mock
    ):
        get_postcode_coords_mock.side_effect = geocode.GeoCodeError
        walker_address_mock.return_value.is_valid = mock_true
        walker_address_mock.return_value.has_changed = mock_true

        request_stub = HttpRequestStub()
        form_handlers._address_form_handler(request_stub)

        self.assertEqual(len(request_stub._messages), 1)
        self.assertEqual(
            request_stub._messages[0][1], "We couldn't find your postcode!"
        )
        self.assertEqual(request_stub._messages[0][0], 40)

    @mock.patch("walker_profile.utility.form_handlers.WalkerUserAvatarForm")
    def test_avatar_form_handler_happy_flow(self, user_avatar_mock):
        user_avatar_mock.return_value.is_valid = mock_true
        user_avatar_mock.return_value.save = mock_true
        user_avatar_mock.return_value.has_changed = mock_true

        request_stub = HttpRequestStub()
        form_handlers._avatar_form_handler(request_stub)

        self.assertEqual(request_stub.session["tab"], "upload_photo")
        self.assertEqual(len(request_stub._messages), 1)
        self.assertEqual(
            request_stub._messages[0][1],
            "Your avatar is updated successfully",
        )
        self.assertEqual(request_stub._messages[0][0], 25)

    @mock.patch("walker_profile.utility.form_handlers.WalkerUserAvatarForm")
    def test_avatar_form_add_errors_to_session_when_form_is_invalid(
        self, user_avatar_mock
    ):
        user_avatar_mock.return_value.is_valid = mock_false
        user_avatar_mock.return_value.errors = {"error": True}

        request_stub = HttpRequestStub()
        form_handlers._avatar_form_handler(request_stub)

        self.assertEqual(request_stub.session["tab"], "upload_photo")
        self.assertEqual(len(request_stub._messages), 0)
        self.assertEqual(
            request_stub.session["avatar_form_errors"], {"error": True}
        )

    @mock.patch(
        "walker_profile.utility.form_handlers.PetsitterDescriptionForm"
    )
    def test_description_form_handler_happy_flow(self, description_mock):
        petsitter_details = PetsitterDetails.objects.create(
            description="Dwarfs are good blacksmiths"
        )
        description_mock.return_value.is_valid = mock_true
        description_mock.return_value.save = mock_true
        description_mock.return_value.has_changed = mock_true
        description_mock.return_value.instance = petsitter_details

        request_stub = HttpRequestStub()
        form_handlers._description_handler(request_stub)

        self.assertEqual(request_stub.session["tab"], "petsitter_profile")
        self.assertEqual(len(request_stub._messages), 1)
        self.assertEqual(
            request_stub._messages[0][1],
            "Your description is updated successfully",
        )
        self.assertEqual(request_stub._messages[0][0], 25)

    @mock.patch(
        "walker_profile.utility.form_handlers.PetsitterDescriptionForm"
    )
    def test_description_form_add_errors_to_messages_when_form_is_invalid(
        self, description_mock
    ):

        description_mock.return_value.is_valid = mock_false
        description_mock.return_value.errors = {"error": "test"}
        request_stub = HttpRequestStub()
        form_handlers._description_handler(request_stub)
        self.assertEqual(request_stub.session["tab"], "petsitter_profile")
        self.assertEqual(len(request_stub._messages), 1)

    @mock.patch("walker_profile.utility.form_handlers.ServiceDetailsForm")
    def test_service_details_form_handler_happy_flow(
        self, service_details_mock
    ):
        request_stub = HttpRequestStub()
        service_type = ServiceTypes.objects.create(type="walk")
        petsitter_details = ServiceDetails.objects.create(
            user=request_stub.user,
            service_type=service_type,
            is_active=True,
        )

        service_details_mock.return_value.is_valid = mock_true
        service_details_mock.return_value.save = mock_true
        service_details_mock.return_value.has_changed = mock_true

        form_handlers._service_details_forms_handler(
            request_stub, petsitter_details.id
        )

        self.assertEqual(request_stub.session["tab"], "petsitter_profile")
        self.assertEqual(len(request_stub._messages), 1)
        self.assertEqual(
            request_stub._messages[0][1],
            "Your data is updated successfully",
        )
        self.assertEqual(request_stub._messages[0][0], 25)

    @mock.patch("walker_profile.utility.form_handlers.ServiceDetailsForm")
    def test_service_details_form_add_errors_to_messages_when_form_is_invalid(
        self, service_details_mock
    ):
        request_stub = HttpRequestStub()
        service_type = ServiceTypes.objects.create(type="walk")
        petsitter_details = ServiceDetails.objects.create(
            user=request_stub.user,
            service_type=service_type,
            is_active=True,
        )
        service_details_mock.return_value.is_valid = mock_false
        service_details_mock.return_value.errors = {"error": "test"}

        form_handlers._service_details_forms_handler(
            request_stub, petsitter_details.id
        )

        self.assertEqual(request_stub.session["tab"], "petsitter_profile")
        self.assertEqual(len(request_stub._messages), 1)


class TestWalkerProfileModel(TestCase):
    def test_reviews_rating_with_no_reviews(self):
        user = create_user(email="saruman@gmail.com", password="twotowers123")
        average_rating, reviews_qty = user.reviews_rating()
        self.assertEqual(average_rating, 0)
        self.assertEqual(reviews_qty, 0)

    def test_user_reviews_rating_with_multiple_reviews(self):
        user = create_user(email="saruman@gmail.com", password="twotowers123")
        reviewer = create_user(
            email="orc@gmail.com", password="ilovesauron123"
        )
        PetsitterReview.objects.create(
            stars=5,
            user=user,
            reviewer=reviewer,
            is_visible=True,
            is_admin_approved=True,
        )
        PetsitterReview.objects.create(
            stars=4,
            user=user,
            reviewer=reviewer,
            is_visible=True,
            is_admin_approved=True,
        )
        PetsitterReview.objects.create(
            stars=4,
            user=user,
            reviewer=reviewer,
            is_visible=True,
            is_admin_approved=True,
        )
        average_rating, reviews_qty = user.reviews_rating()
        self.assertEqual(average_rating, 4)
        self.assertEqual(reviews_qty, 3)

    def test_search_petsitters(self):
        service_type = ServiceTypes.objects.create(type="walk")
        user = create_user(
            email="saruman@gmail.com",
            password="twotowers123",
            is_petsitter=True,
        )
        create_user(
            email="orc@gmail.com", password="ilovesauron123", is_petsitter=True
        )
        ServiceDetails.objects.create(
            user=user,
            service_type=service_type,
            is_active=True,
            is_small_dog=True,
        )
        search_params = {"dog_size": "small", "care_type": "walk"}
        search_result = WalkerUser.search_petsitter(search_params)

        self.assertEqual(len(search_result), 1)
        self.assertEqual(search_result[0], user)

    def test_walker_profile_str_method_return_username(self):
        user = get_user_model().objects.create(
            email="orc@gmail.com",
            password="ilovesauron123",
            username="mightyorc",
        )

        self.assertEqual(str(user), "mightyorc")

    def test_service_details_add_only_active_services(self):
        service_walk = ServiceTypes.objects.create(type="walk")
        service_petsitter_home = ServiceTypes.objects.create(
            type="boarding_at_pet_sitter_home"
        )
        user = create_user(
            email="saruman@gmail.com",
            password="twotowers123",
            is_petsitter=True,
        )
        ServiceDetails.objects.create(
            user=user,
            service_type=service_walk,
            is_active=True,
            is_small_dog=True,
            is_medium_dog=True,
            is_big_dog=True,
            s_price_hour=10,
            m_price_hour=15,
            b_price_hour=20,
        )
        ServiceDetails.objects.create(
            user=user,
            service_type=service_petsitter_home,
            is_active=True,
            is_small_dog=False,
            is_medium_dog=False,
            is_big_dog=False,
        )
        active_services = user.get_service_details()
        self.assertEqual(len(active_services), 1)
        self.assertIn("small", active_services[0]["dog_sizes"])
        self.assertIn("medium", active_services[0]["dog_sizes"])
        self.assertIn("big", active_services[0]["dog_sizes"])
