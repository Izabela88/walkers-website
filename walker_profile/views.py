from django.shortcuts import render

# Create your views here.
def user_profile(request):
    context = {}
    if request.user.is_authenticated:
        context['is_petsitter'] = request.user.is_petsitter
    return render(request, 'user_profile/user_profile.html', context)