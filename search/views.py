from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from walker_profile.models import WalkerUser
from search.forms import SearchForm
from django.db.models import Q
from django.urls import reverse
from walker_profile import utility
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from walker_profile.utility import geocode


class SearchView(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        """Search pet sitters endpoint"""
        if not request.user.is_authenticated:
            return render(request, '401.html')
        context = {}
        petsitter_search_form = SearchForm(data=request.POST or None)
        if petsitter_search_form.is_valid():
            try:
                search_long, search_lat = geocode.get_postcode_coordinates(
                    petsitter_search_form.cleaned_data['postcode']
                )
            except geocode.GeoCodeError:
                messages.error(request, "Invalid postcode!")
                return HttpResponseRedirect(
                    reverse('home') + '#searching-section'
                )

            petsitters = WalkerUser.search_petsitter(
                petsitter_search_form.cleaned_data
            )
            petsitters = geocode.get_users_within_radius(
                search_long,
                search_lat,
                petsitters,
                petsitter_search_form.cleaned_data['area'],
            )
            # Create tuples pet sitter and review rating for sorting purpose
            search_result = [(i, i.reviews_rating()) for i in petsitters]
            search_result.sort(key=lambda x: x[1], reverse=True)
            context['search_results'] = search_result
        else:
            request.session[
                "petsitter_search_form_errors"
            ] = petsitter_search_form.errors
            petsitter_search_form = SearchForm(data=request.POST or None)
            return redirect(reverse('home') + '#searching-section')
        return render(
            request, 'search/petsitters_search_results.html', context
        )


class PetsitterProfile(View):
    def get(self, request: HttpRequest, id: int) -> HttpResponse:
        """Get petsitter profile"""
        if not request.user.is_authenticated:
            return render(request, '401.html')
        context = {}
        user = get_object_or_404(WalkerUser, id=id)
        context['user'] = user
        context['services'] = []
        context['services'] = user.get_service_details()
        avg_rating, reviews_qty = user.reviews_rating()
        context['reviews_data'] = {
            'reviews': user.user_reviews.filter(
                is_admin_approved=True, is_visible=True
            ).all(),
            'avg_rating': avg_rating,
            'reviews_qty': reviews_qty,
        }
        return render(request, 'search/petsitter_profile.html', context)
