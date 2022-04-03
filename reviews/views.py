from django.views import View
from walker_profile.models import WalkerUser
from reviews.forms import PetsitterReviewForm
from reviews.models import PetsitterReview
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.contrib import messages
from django.urls import reverse


class Review(View):
    def get(self, request: HttpRequest, id: int) -> HttpResponse:
        """Pet sitter review GET endpoint"""
        if not request.user.is_authenticated:
            return render(request, '401.html')
        context = {
            'review_form_errors': request.session.pop(
                "review_form_errors", None
            )
        }
        user = get_object_or_404(WalkerUser, id=id)
        context['user'] = user
        context['review_description_form'] = PetsitterReviewForm()
        return render(request, 'reviews/review.html', context)

    def post(self, request: HttpRequest, id) -> HttpResponse:
        """Submit review form"""
        if not request.user.is_authenticated:
            return render(request, '401.html')
        if id == request.user.id:
            return render(request, '403.html')
        user_review = PetsitterReview.objects.filter(
            user_id=id, reviewer_id=request.user.id
        ).first()
        if user_review:
            messages.error(
                request, 'You have already given review to this user !'
            )
        else:
            review_form = PetsitterReviewForm(data=request.POST or None)
            if review_form.is_valid():
                review_form.instance.user_id = id
                review_form.instance.reviewer_id = request.user.id
                review_form.instance.save()
                messages.success(request, 'Thank you for your review!')
            else:
                print(review_form.errors)
                request.session["review_form_errors"] = review_form.errors
                return HttpResponseRedirect(reverse('review'))
        return HttpResponseRedirect(
            reverse('petsitter_profile', kwargs={'id': id})
        )
