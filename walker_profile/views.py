
from django.shortcuts import render
from walker_profile.forms import UpdateWalkerProfile, WalkerAddressForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin



def user_profile(request):
    context = {
        "errors": {
            "profile_form_errors": request.session.pop("profile_form_errors", None),
            "address_form_errors": request.session.pop("address_form_errors", None),
        }
    }

    if request.method == "GET":
        if request.user.is_authenticated:
            context['is_petsitter'] = request.user.is_petsitter
        profile_form = UpdateWalkerProfile(instance=request.user)
        address_form = WalkerAddressForm(instance=request.user.address_details)
        context['profile_form'] = profile_form
        context['address_form'] = address_form
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
            if address_form.is_valid():
                address_form.save()
                if request.user.address_details_id != address_form.instance.id:
                    request.user.address_details_id = address_form.instance.id
                    request.user.save()
                messages.success(request, 'Your address is updated successfully')
            else:
                request.session["address_form_errors"] = address_form.errors
                context['address_form'] = WalkerAddressForm(instance=request.user.address_details)

        return HttpResponseRedirect("/profile/user_profile")

# https://dev.to/earthcomfy/django-update-user-profile-33ho

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('user_profile')