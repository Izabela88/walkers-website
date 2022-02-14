from django.shortcuts import render
from walker_profile.forms import ContactDetailsForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect



# Create your views here.
def user_profile(request):
    context = {}
    if request.user.is_authenticated:
        context['is_petsitter'] = request.user.is_petsitter
    contact_details_form = ContactDetailsForm()
    context['contact_details_form'] = contact_details_form
    return render(request, 'user_profile/user_profile.html', context)


@login_required
def profile_contact_details(request):
    if request.method == "POST":
        contact_details_form = ContactDetailsForm(request.POST)
        if contact_details_form.is_valid():
            contact_details_form.save()
        return redirect('/profile/user_profile')
        