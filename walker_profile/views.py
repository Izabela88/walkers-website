
from django.shortcuts import render
from walker_profile.forms import UpdateWalkerProfileForm, WalkerAddressForm, WalkerUserAvatarForm, PetsitterDescriptionForm, ServiceDetailsForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import get_user_model
from django.views.generic.edit import DeleteView
from django.urls import reverse
from .models import ServiceTypes, ServiceDetails



def user_profile(request):
    context = {
        "profile_form_errors": request.session.pop("profile_form_errors", None),
        "address_form_errors": request.session.pop("address_form_errors", None),
        "avatar_errors": request.session.pop("avatar_errors", None),
        "description_errors": request.session.pop("description_errors", None),
        "description_errors": request.session.pop("description_errors", None),
        "service_details_errors": request.session.pop("service_details_errors", None),
    }

    if request.method == "GET":
        if request.user.is_authenticated:
            context['is_petsitter'] = request.user.is_petsitter
        profile_form = UpdateWalkerProfileForm(instance=request.user)
        address_form = WalkerAddressForm(instance=request.user.address_details)
        avatar = WalkerUserAvatarForm(instance=request.user)
        description = PetsitterDescriptionForm(instance=request.user.petsitter_details)
        context['profile_form'] = profile_form
        context['address_form'] = address_form
        context['avatar'] = avatar
        context['description'] = description

        context['service_details'] = {}
        user_service_details = ServiceDetails.objects.filter(user_id=request.user.id).all()
        service_types = ServiceTypes.objects.all()

        # Iterate on user service details and create mapping with service types and form with user detail instance
        for i in user_service_details:
            service_detail_form = ServiceDetailsForm(instance=i)
            formatted_type = i.service_type.types.replace("_", " ").capitalize()
            context['service_details'][i.service_type.id] = (i.service_type.types, formatted_type, service_detail_form)

        # Check if any kind of form was not initiated with user data. If not create one with types fields and empty form
        for i in service_types:
            if i.id not in context['service_details']:
                formatted_type = i.types.replace("_", " ").capitalize()
                context['service_details'][i.id] = (i.types, formatted_type, ServiceDetailsForm())

        if "tab" in request.session:
            context["tab"] =  request.session.pop("tab")
        return render(request, 'user_profile/user_profile.html', context)

    if request.method == "POST" and request.user.is_authenticated:      
        form_type = request.POST.get("form_type")
        if form_type == "profile_form":
            profile_form = UpdateWalkerProfileForm(instance=request.user, data=request.POST or None)
            request.session['tab'] = "update_profile"
            if profile_form.is_valid() and profile_form.has_changed():
                profile_form.save()
                messages.success(request, 'Your profile is updated successfully')
            else:
                request.session["profile_form_errors"] = profile_form.errors
                context['profile_form'] = UpdateWalkerProfileForm(instance=request.user)

        if form_type == "address_form":
            address_form = WalkerAddressForm(instance=request.user.address_details, data=request.POST or None)
            request.session['tab'] = "address_form"
            if address_form.is_valid() and address_form.has_changed():
                address_form.save()
                if request.user.address_details_id != address_form.instance.id:
                    request.user.address_details_id = address_form.instance.id
                    request.user.save()
                messages.success(request, 'Your address is updated successfully')
            else:
                request.session["address_form_errors"] = address_form.errors
                context['address_form'] = WalkerAddressForm(instance=request.user.address_details)
            
        if form_type == "avatar":
            avatar = WalkerUserAvatarForm(request.POST or None, request.FILES, instance=request.user)
            request.session['tab'] = "avatar"
            if avatar.is_valid() and avatar.has_changed():
                avatar.save()
                messages.success(request, 'Your avatar is updated successfully')
            else:
                request.session["avatar_errors"] = avatar.errors
                context['avatar'] = WalkerUserAvatarForm(instance=request.user)

        if form_type == "description":
            description = PetsitterDescriptionForm(instance=request.user.petsitter_details, data=request.POST or None)
            request.session['tab'] = "service_details"

            if description.is_valid() and description.has_changed():
                description.save()
                if request.user.petsitter_details_id != description.instance.id:
                    request.user.petsitter_details_id = description.instance.id
                    request.user.save()
                messages.success(request, 'Your description is updated successfully')
            else:
                request.session["description_errors"] = description.errors
                context['description'] = PetsitterDescriptionForm(instance=request.user.petsitter_details)

        service_types = ServiceTypes.objects.all()
        service_types_mapping = {}
      
        for i in service_types:
            service_types_mapping[i.types] = i.id

        if form_type in service_types_mapping:
            service_type_id = service_types_mapping[form_type]
            service_detail = ServiceDetails.objects.filter(service_type_id=service_type_id, user_id=request.user.id).first()
            service_details_form = ServiceDetailsForm(instance=service_detail, data=request.POST or None)
            request.session['tab'] = "service_details"
            if service_details_form.is_valid() and service_details_form.has_changed():
                service_details_form.instance.service_type_id = service_type_id
                service_details_form.instance.user_id = request.user.id
                service_details_form.save()
                messages.success(request, 'Your data is updated successfully')
            else:
                request.session["service_details_errors"] = service_details_form.errors
                context['service_details'] = ServiceDetailsForm(instance=service_detail)

        return HttpResponseRedirect("/profile/user_profile")

# https://dev.to/earthcomfy/django-update-user-profile-33ho

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('user_profile')


User = get_user_model()

class WalkerUserDelete(DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Your account has been deleted successfully.")
        return reverse('home')
