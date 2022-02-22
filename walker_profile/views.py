
from django.shortcuts import render
from walker_profile.forms import UpdateWalkerProfile, WalkerAddressForm, WalkerUserAvatar, PetsitterDescription
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import get_user_model
from django.views.generic.edit import DeleteView
from django.urls import reverse


def user_profile(request):
    context = {
        "profile_form_errors": request.session.pop("profile_form_errors", None),
        "address_form_errors": request.session.pop("address_form_errors", None),
        "avatar_errors": request.session.pop("avatar_errors", None),
        "description_errors": request.session.pop("description_errors", None),
    }

    if request.method == "GET":
        if request.user.is_authenticated:
            context['is_petsitter'] = request.user.is_petsitter
        profile_form = UpdateWalkerProfile(instance=request.user)
        address_form = WalkerAddressForm(instance=request.user.address_details)
        avatar = WalkerUserAvatar(instance=request.user)
        description = PetsitterDescription(instance=request.user.petsitter_details)
        context['profile_form'] = profile_form
        context['address_form'] = address_form
        context['avatar'] = avatar
        context['description'] = description
        if "tab" in request.session:
            context["tab"] =  request.session.pop("tab")
        return render(request, 'user_profile/user_profile.html', context)

    if request.method == "POST" and request.user.is_authenticated:
        if request.POST.get("form_type") == "profile_form":
            profile_form = UpdateWalkerProfile(instance=request.user, data=request.POST or None)
            request.session['tab'] = "update_profile"
            if profile_form.is_valid() and profile_form.has_changed():
                profile_form.save()
                messages.success(request, 'Your profile is updated successfully')
            else:
                request.session["profile_form_errors"] = profile_form.errors
                context['profile_form'] = UpdateWalkerProfile(instance=request.user)

        if request.POST.get("form_type") == "address_form":
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
            
        if request.POST.get("form_type") == "avatar":
            avatar = WalkerUserAvatar(request.POST or None, request.FILES, instance=request.user)
            request.session['tab'] = "avatar"
            if avatar.is_valid() and avatar.has_changed():
                avatar.save()
                messages.success(request, 'Your avatar is updated successfully')
            else:
                request.session["avatar_errors"] = avatar.errors
                context['avatar'] = WalkerUserAvatar(instance=request.user)

        if request.POST.get("form_type") == "description":
            description = PetsitterDescription(instance=request.user.petsitter_details, data=request.POST or None)
            request.session['tab'] = "description"
            if description.is_valid() and description.has_changed():
                description.save()
                if request.user.petsitter_details_id != description.instance.id:
                    request.user.petsitter_details_id = description.instance.id
                    request.user.save()
                messages.success(request, 'Your description is updated successfully')
            else:
                request.session["description_errors"] = description.errors
                context['description'] = PetsitterDescription(instance=request.user.petsitter_details)

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
