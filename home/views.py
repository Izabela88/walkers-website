from django.shortcuts import render
from django.shortcuts import redirect
from user.models import PetsitterAttrError
from django.contrib.auth.decorators import login_required
from home.forms import PetsitterQuestion, FormValidationError

# Create your views here.
def index(request):
    context = {
        'is_petsitter': False
    }
    if request.user.is_authenticated:
        try:
            context['is_petsitter'] = request.user.is_petsitter()
        except PetsitterAttrError:
            return redirect('/question')

    return render(request, 'home/index.html', context)

@login_required
def register_question(request):
    if request.method == "GET":
        form_petsitter = PetsitterQuestion()
        return render(request, 'home/question.html', {'form_petsitter': form_petsitter})
    if request.method == "POST":
        pet_sitter = PetsitterQuestion(request.POST)
        try:
            pet_sitter.save(request.user)
        except FormValidationError:
            redirect('/question')
        return redirect("/")
