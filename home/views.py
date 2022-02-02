from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.
def index(request):
    context = {
        'is_petsitter': False
    }
    if request.user.is_authenticated:
        context['is_petsitter'] = request.user.is_petsitter()

    return render(request, 'home/index.html', context)