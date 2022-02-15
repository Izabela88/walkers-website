from django.shortcuts import render
from walker_profile.forms import UpdateWalkerProfile
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.
def user_profile(request):
    print(" ::: User profile GET method ::: ")
    context = {}
    if request.user.is_authenticated:
        context['is_petsitter'] = request.user.is_petsitter
    profile_form = UpdateWalkerProfile(instance=request.user)
    context['profile_form'] = profile_form
    return render(request, 'user_profile/user_profile.html', context)


@login_required
def update_walker_profile(request):
    context = {}
    if request.method == "POST":
        profile_form = UpdateWalkerProfile(request.POST, instance=request.user)

        if profile_form.is_valid() and profile_form.has_changed():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('/profile/user_profile')
        else:
            print(profile_form.errors)
            context['profile_form'] = profile_form
            context['tab'] = "update_profile"
            return render(request, 'user_profile/user_profile.html', context)
    else:
        return render(request, 'user_profile/user_profile.html', context)

# change js to use class instead style
# create class css
#     context['tab'] = "update_profile"
# 