from django.views import View
from walker_profile.forms import (
    UpdateWalkerProfileForm,
    WalkerAddressForm,
    WalkerUserAvatarForm,
    PetsitterDescriptionForm,
    ServiceDetailsForm,
)
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import DeleteView
from walker_profile.models import ServiceTypes, ServiceDetails
from walker_profile.utility import form_handlers
from django.shortcuts import render, get_object_or_404
from walker_profile.models import WalkerUser
from reviews.models import PetsitterReview
from reviews.forms import PetsitterReviewForm
from django.contrib.sessions.backends.base import SessionBase


class UserProfileView(View):
    def get(self, request: HttpRequest, id: int) -> HttpResponse:
        """Render user profile dashboard"""
        if not request.user.is_authenticated:
            return render(request, "401.html")
        if id != request.user.id:
            return render(request, "403.html")

        context = self._get_context(request.session)

        context["is_petsitter"] = request.user.is_petsitter

        context["profile_form"] = UpdateWalkerProfileForm(
            instance=request.user
        )
        context["address_form"] = WalkerAddressForm(
            instance=request.user.address_details
        )
        context["avatar_form"] = WalkerUserAvatarForm(instance=request.user)
        context["description_form"] = PetsitterDescriptionForm(
            instance=request.user.petsitter_details
        )
        context["user"] = request.user

        context["service_details_forms"] = {}
        user_service_details = ServiceDetails.objects.filter(
            user_id=request.user.id
        ).all()
        service_types = ServiceTypes.objects.all()

        # Iterate on user service details and create mapping with
        # service types and form with user detail instance*/
        for i in user_service_details:
            service_detail_form = ServiceDetailsForm(instance=i)
            formatted_type = i.service_type.type.replace("_", " ").capitalize()
            context["service_details_forms"][i.service_type.id] = (
                i.service_type.type,
                formatted_type,
                service_detail_form,
            )

        # Check if any kind of form was not initiated with user data.
        # If not create one with types fields and empty form
        for i in service_types:
            if i.id not in context["service_details_forms"]:
                formatted_type = i.type.replace("_", " ").capitalize()
                context["service_details_forms"][i.id] = (
                    i.type,
                    formatted_type,
                    ServiceDetailsForm(),
                )

        if "tab" in request.session:
            # Flag for html anchors
            context["tab"] = request.session.pop("tab")
        return render(request, "user_profile/user_profile.html", context)

    def post(self, request, id):
        """User details update"""
        if not request.user.is_authenticated:
            return render(request, "401.html")

        form_handler_mapping = {
            "profile_form": form_handlers._profile_form_handler,
            "address_form": form_handlers._address_form_handler,
            "avatar_form": form_handlers._avatar_form_handler,
            "description_form": form_handlers._description_handler,
        }

        # Get submitted form type name
        form_type = request.POST.get("form_type")

        # Dynamically create/add mapping for service types forms
        service_types = ServiceTypes.objects.all()
        service_type_id = None
        for i in service_types:
            # Add dynamically handler to form handler mapping
            form_handler_mapping[
                i.type
            ] = form_handlers._service_details_forms_handler
            if form_type == i.type:
                # Assign service id flag and break loop, at this point we know
                # already which form was submitted
                service_type_id = i.id
                break

        if form_handler_fn := form_handler_mapping.get(form_type):
            form_handler_fn(request, service_type_id)

        return HttpResponseRedirect(reverse("user_profile", kwargs={"id": id}))

    def _get_context(self, session: SessionBase) -> dict:
        """Prepare context with possible form errors. Function will clear
        session form keys

        Args:
            session (SessionBase): Django session

        Returns:
            dict: Context with form error data
        """
        context = {
            "profile_form_errors": session.pop("profile_form_errors", None),
            "address_form_errors": session.pop("address_form_errors", None),
            "avatar_form_errors": session.pop("avatar_form_errors", None),
            "description_errors": session.pop("description_errors", None),
            "service_details_errors": session.pop(
                "service_details_errors", None
            ),
        }
        return context


# https://dev.to/earthcomfy/django-update-user-profile-33ho
class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    model = WalkerUser
    template_name = "change_password.html"
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy("home")


class WalkerUserDelete(DeleteView):
    model = WalkerUser
    template_name = "user_confirm_delete.html"

    def get_success_url(self):
        messages.success(
            self.request, "Your account has been deleted successfully."
        )
        return reverse("home")


class WalkerUserReviewList(View):
    def get(self, request: HttpRequest, id=int) -> HttpResponse:
        """Get all user posted reviews"""
        if not request.user.is_authenticated:
            return render(request, "401.html")
        user = get_object_or_404(WalkerUser, id=id)
        context = {
            "reviews": user.reviewer_reviews.all(),
            "user": user,
        }
        return render(request, "user_profile/reviews_list.html", context)


class WalkerUserReview(View):
    def dispatch(self, *args, **kwargs):
        """Overwright interface to allow delete method
        https://stackoverflow.com/questions/36455189/put-and-delete-django
        """
        method = self.request.POST.get("_method", "").lower()
        if method == "delete":
            return self.delete(*args, **kwargs)
        return super(WalkerUserReview, self).dispatch(*args, **kwargs)

    def get(
        self, request: HttpRequest, user_id: int, review_id: int
    ) -> HttpResponse:
        """Get review"""
        if not request.user.is_authenticated:
            return render(request, "401.html")
        if user_id != request.user.id:
            return render(request, "403.html")

        review = get_object_or_404(
            PetsitterReview, id=review_id, reviewer_id=user_id
        )

        context = {
            "walker_user_review_form_errors": request.session.pop(
                "walker_user_review_form_errors", None
            ),
            "walker_user_review_form": PetsitterReviewForm(instance=review),
            "petsitter_name": review.user.first_name,
            "petsitter_stars": review.stars,
            "review_id": review_id,
        }
        return render(request, "user_profile/edit_review.html", context)

    def post(
        self, request: HttpRequest, user_id: int, review_id: int
    ) -> HttpResponse:
        """Update review"""
        if not request.user.is_authenticated:
            return render(request, "401.html")
        if user_id != request.user.id:
            return render(request, "403.html")

        review = get_object_or_404(
            PetsitterReview, id=review_id, reviewer_id=user_id
        )

        walker_user_review_form = PetsitterReviewForm(
            instance=review, data=request.POST or None
        )

        if walker_user_review_form.is_valid():
            if walker_user_review_form.has_changed():
                walker_user_review_form.save()
            messages.success(request, "Your review is updated successfully")
        else:
            messages.error(request, "Something went wrong!")
            request.session[
                "walker_user_review_form_errors"
            ] = walker_user_review_form.errors

        return HttpResponseRedirect(
            reverse(
                "walker_user_review",
                kwargs={"user_id": user_id, "review_id": review_id},
            )
        )

    def delete(
        self, request: HttpRequest, user_id: int, review_id: int
    ) -> HttpResponse:
        """Delete review"""
        if not request.user.is_authenticated:
            return render(request, "401.html")
        if user_id != request.user.id:
            return render(request, "403.html")
        review = get_object_or_404(
            PetsitterReview, id=review_id, reviewer_id=user_id
        )
        if review.reviewer_id != request.user.id:
            return render(request, "403.html")
        review.delete()
        messages.success(request, "Review successfully deleted!")
        return HttpResponseRedirect(reverse("reviews", kwargs={"id": user_id}))
