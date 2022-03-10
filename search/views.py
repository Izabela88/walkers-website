from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from walker_profile.models import WalkerUser
from search.forms import SearchForm
from django.db.models import Q
from django.urls import reverse
from walker_profile import utility
from django.http import HttpResponseRedirect
from walker_profile.utility import GeoCodeError
from reviews.models import PetsitterReview


class SearchView(View):
    def post(self, request):
        context = {}
        petsitter_search_form = SearchForm(data=request.POST or None)
        if petsitter_search_form.is_valid():
            try:
                search_long, search_lat = utility.get_postcode_coordinates(
                    petsitter_search_form.cleaned_data['postcode']
                )
            except GeoCodeError:
                messages.error(request, "Invalid postcode!")
                return HttpResponseRedirect(reverse('home') + '#searching-section')

            care_type = petsitter_search_form.cleaned_data['care_type']
            dog_size = petsitter_search_form.cleaned_data['dog_size']
            radius_miles = petsitter_search_form.cleaned_data['area']

            if dog_size == "small":
                size_filter = Q(service_details__is_small_dog=True)
            elif dog_size == "medium":
                size_filter = Q(service_details__is_medium_dog=True)
            elif dog_size == "big":
                size_filter = Q(service_details__is_big_dog=True)
            filter_ = Q(
                is_petsitter=True,
                service_details__service_type__type=care_type,
                service_details__is_active=True,
                address_details__longitude__isnull=False,
                address_details__latitude__isnull=False,
            )
            petsitters = WalkerUser.objects.filter(filter_ & size_filter).all()
            context['search_results'] =  utility.get_users_within_radius(
                search_long, search_lat, petsitters, radius_miles
            )
        else:
            request.session[
                "petsitter_search_form_errors"
            ] = petsitter_search_form.errors
            petsitter_search_form = SearchForm(data=request.POST or None)
            return redirect(reverse('home') + '#searching-section')
        return render(request, 'search/petsitters_search_results.html', context)


class PetsitterProfile(View):
    def get(self, request, id):
        if not request.user.is_authenticated:
            return render(request, '401.html')
        context = {}
        user = get_object_or_404(WalkerUser, id=id)
        context['user'] = user
        context['services'] = []
        for i in user.service_details.all():
            if i.is_active:
                service = {'type': i.service_type.type, 'dog_sizes': {}}
                if i.is_small_dog:
                    service['dog_sizes']['small'] = {
                        'price_hour': i.s_price_hour,
                        'price_day': i.s_price_day,
                    }
                if i.is_medium_dog:
                    service['dog_sizes']['medium'] = {
                        'price_hour': i.m_price_hour,
                        'price_day': i.m_price_day,
                    }
                if i.is_big_dog:
                    service['dog_sizes']['big'] = {
                        'price_hour': i.b_price_hour,
                        'price_day': i.b_price_day,
                    }

                context['services'].append(service)
        context['reviews'] = PetsitterReview.objects.filter(
            user_id=id, is_admin_approved=True,is_visible=True
        ).all()

        


        return render(request, 'search/petsitter_profile.html', context)
