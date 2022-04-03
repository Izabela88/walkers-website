from django.shortcuts import render
from home.forms import PetsitterQuestion, PetsitterFormValidationError
from search.forms import SearchForm
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse


class Home(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        """Home view endpoint. First pre check when user is signed in and if
        pet sitter question was submitted"""
        context = {
            "petsitter_search_form_errors": request.session.pop(
                "petsitter_search_form_errors", None
            ),
        }

        if request.user.is_authenticated:
            if request.user.is_petsitter is None:
                return HttpResponseRedirect(reverse('question'))
            context['is_petsitter'] = request.user.is_petsitter

        search_form = SearchForm()
        context['search_form'] = search_form
        return render(request, 'home/index.html', context)


class RegisterQuestion(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        """Render pet sitter question template if user registered via social
        media"""
        if not request.user.is_authenticated:
            return render(request, '401.html')
        form_petsitter = PetsitterQuestion()
        return render(
            request, 'home/question.html', {'form_petsitter': form_petsitter}
        )

    def post(self, request) -> HttpResponse:
        """Submit question form endpoint"""
        if not request.user.is_authenticated:
            return render(request, '401.html')
        pet_sitter = PetsitterQuestion(request.POST)
        try:
            pet_sitter.save(request.user)
        except PetsitterFormValidationError:
            HttpResponseRedirect(reverse('question'))
        return HttpResponseRedirect(reverse('home'))
