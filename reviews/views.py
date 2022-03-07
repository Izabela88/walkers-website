from django.shortcuts import render
from django.views import View
from walker_profile.models import WalkerUser
from django.shortcuts import redirect, render, get_object_or_404




class Review(View):
    
    def get(self, request, id):
        if not request.user.is_authenticated:
            return render(request, '401.html')
        context = {}
        user = get_object_or_404(WalkerUser, id=id)
        context['user'] = user
        return render(request, 'reviews/reviews.html', context)

