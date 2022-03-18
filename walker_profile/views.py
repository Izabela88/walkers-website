from django.shortcuts import render
from django.views import View
from walker_profile.forms import (
    UpdateWalkerProfileForm,
    WalkerAddressForm,
    WalkerUserAvatarForm,
    PetsitterDescriptionForm,
    ServiceDetailsForm,
)
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import DeleteView
from django.urls import reverse
from walker_profile.models import ServiceTypes, ServiceDetails
from walker_profile import utility
from django.shortcuts import redirect, render, get_object_or_404
from walker_profile.models import WalkerUser
from reviews.models import PetsitterReview
from reviews.forms import PetsitterReviewForm



class UserProfileView(View):
    template_name = 'user_profile.html'

    def get(self, request, id):
        if not request.user.is_authenticated:
            return render(request, '401.html')
        
        context = {
            "profile_form_errors": request.session.pop("profile_form_errors", None),
            "address_form_errors": request.session.pop("address_form_errors", None),
            "avatar_form_errors": request.session.pop("avatar_form_errors", None),
            "description_errors": request.session.pop("description_errors", None),
            "description_errors": request.session.pop("description_errors", None),
            "service_details_errors": request.session.pop(
                "service_details_errors", None
            ),
        }

        if not request.user.is_authenticated:
            return render(request, '401.html')
        context['is_petsitter'] = request.user.is_petsitter
        profile_form = UpdateWalkerProfileForm(instance=request.user)
        address_form = WalkerAddressForm(instance=request.user.address_details)
        avatar_form = WalkerUserAvatarForm(instance=request.user)
        description_form = PetsitterDescriptionForm(
            instance=request.user.petsitter_details
        )
        user = get_object_or_404(WalkerUser, id=id)
        context['user'] = user
        context['profile_form'] = profile_form
        context['address_form'] = address_form
        context['avatar_form'] = avatar_form
        context['description_form'] = description_form
        context['service_details_forms'] = {}
        user_service_details = ServiceDetails.objects.filter(
            user_id=request.user.id
        ).all()
        service_types = ServiceTypes.objects.all()

        # Iterate on user service details and create mapping with service types and form with user detail instance
        for i in user_service_details:
            service_detail_form = ServiceDetailsForm(instance=i)
            formatted_type = i.service_type.type.replace("_", " ").capitalize()
            context['service_details_forms'][i.service_type.id] = (
                i.service_type.type,
                formatted_type,
                service_detail_form,
            )

        # Check if any kind of form was not initiated with user data. If not create one with types fields and empty form
        for i in service_types:
            if i.id not in context['service_details_forms']:
                formatted_type = i.type.replace("_", " ").capitalize()
                context['service_details_forms'][i.id] = (
                    i.type,
                    formatted_type,
                    ServiceDetailsForm(),
                )

        if "tab" in request.session:
            context["tab"] = request.session.pop("tab")
        return render(request, 'user_profile/user_profile.html', context)

    def post(self, request, id):
        if not request.user.is_authenticated:
            return render(request, '401.html')
        context = {}
        user = get_object_or_404(WalkerUser, id=id)
        context['user'] = user

        form_mapping = {
            "profile_form": utility._handle_profile_form,
            "address_form": utility._handle_address_form,
            "avatar_form": utility._handle_avatar_form,
            "description_form": utility._handle_description_form,
        }
        service_types = ServiceTypes.objects.all()
        form_type = request.POST.get("form_type")
        service_type_id = None
        for i in service_types:
            form_mapping[i.type] = utility._handle_service_details_forms
            if form_type == i.type:
                service_type_id = i.id
        form_handler = form_mapping.get(form_type)
        if form_handler:
            context = form_handler(request, context, service_type_id)
        return HttpResponseRedirect(f"/profile/user_profile/{id}")


# https://dev.to/earthcomfy/django-update-user-profile-33ho
class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    model = WalkerUser
    template_name = 'change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home')
    

class WalkerUserDelete(DeleteView):
    model = WalkerUser
    template_name = 'user_confirm_delete.html'
    
    def get_success_url(self):
        messages.success(self.request, "Your account has been deleted successfully.")
        return reverse('home')


class WalkerUserReviewList(View):

    def get(self, request, id):
        if not request.user.is_authenticated:
            return render(request, '401.html')
        user = get_object_or_404(WalkerUser, id=id)
        context = {
            'reviews': user.reviewer_reviews.all(),
            'user': user,
        }
        return render(request, 'user_profile/reviews_list.html', context)


class WalkerUserReview(View):

    def get(self, request, user_id, review_id):
        context = {
           'walker_user_review_form_errors': request.session.pop('walker_user_review_form_errors', None),
        }
        
        if not request.user.is_authenticated:
            return render(request, '401.html')
        review = get_object_or_404(PetsitterReview, id=review_id, reviewer_id=user_id)
        walker_user_review_form = PetsitterReviewForm(instance=review)

        if review.reviewer_id != request.user.id:
            return render(request, '403.html')

        context = {
            'walker_user_review_form': walker_user_review_form,
            'petsitter_name': review.user.first_name,
            'petsitter_stars': review.stars,
            
        }
        return render(request, 'user_profile/edit_review.html', context)
    
    def post(self, request, user_id, review_id):
        context = {}
        if not request.user.is_authenticated:
            return render(request, '401.html')
        review = get_object_or_404(PetsitterReview, id=review_id, reviewer_id=user_id)
        if review.reviewer_id != request.user.id:
            return render(request, '403.html')
        walker_user_review_form = PetsitterReviewForm(instance=review, data=request.POST or None)

        if walker_user_review_form.is_valid():
            if walker_user_review_form.has_changed():
                walker_user_review_form.save()
            messages.success(request, 'Your review is updated successfully')
        else:
            print(walker_user_review_form.errors)
            request.session["walker_user_review_form_errors"] = walker_user_review_form.errors
            context['walker_user_review_form'] = PetsitterReviewForm(instance=review)
            return render(request, 'user_profile/edit_review.html', context)
        return HttpResponseRedirect(f'/profile/user_profile/{user_id}/reviews/{review_id}')
        

   