from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from home.forms import PetsitterQuestion, FormValidationError
from search.forms import SearchForm




# Create your views here.
def index(request):
    context = {}
    if request.user.is_authenticated:
        if request.user.is_petsitter is None:
            return redirect('/question') 
        context['is_petsitter'] = request.user.is_petsitter
      
    search_form = SearchForm()
    context['search_form'] = search_form

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


