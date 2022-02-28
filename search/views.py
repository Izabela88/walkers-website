from django.shortcuts import render
from django.views import View
from walker_profile.models import WalkerUser
from search.forms import SearchForm
from django.db.models import Q


class SearchView(View):
    # template_name = 'petsitters_search_results.html'

    def post(self, request): 
        context = {}
        petsitter_search_form = SearchForm(data=request.POST or None)
    
        if petsitter_search_form.is_valid():
            post_code = petsitter_search_form.cleaned_data['post_code']
            care_type = petsitter_search_form.cleaned_data['care_type']
            dog_size = petsitter_search_form.cleaned_data['dog_size']
            
            if dog_size == "small":
                size_query = Q(servicedetails__is_small_dog=True)
            elif dog_size == "medium":
                size_query = Q(servicedetails__is_medium_dog=True)
            elif dog_size == "big":
                size_query = Q(servicedetails__is_big_dog=True)
            query = Q(is_petsitter=True,servicedetails__service_type__types=care_type , servicedetails__is_active=True)
            context['search_results'] = WalkerUser.objects.filter(query & size_query).all()
        else:
            # TODO: Handle if form is not valid
            pass

        return render(request, 'search/petsitters_search_results.html', context)