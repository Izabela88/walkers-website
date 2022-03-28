from django.views import View
from walker_profile.models import WalkerUser
from reviews.forms import PetsitterReviewForm
from reviews.models import PetsitterReview
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages


class Review(View):
    def get(self, request, id):
        if not request.user.is_authenticated:
            return render(request, '401.html')
        context = {
            'review_form_errors': request.session.pop(
                "review_form_errors", None
            )
        }
        user = get_object_or_404(WalkerUser, id=id)
        context['user'] = user
        review_description_form = PetsitterReviewForm()
        context['review_description_form'] = review_description_form
        return render(request, 'reviews/review.html', context)

    def post(self, request, id):
        context = {}
        review_form = PetsitterReviewForm(data=request.POST or None)
        if review_form.is_valid():
            data = PetsitterReview()
            data.description = review_form.cleaned_data['description']
            data.stars = review_form.cleaned_data['stars']
            data.user_id = id
            reviewer = request.user
            data.reviewer_id = reviewer.id
            if id == reviewer.id:
                return render(request, '403.html')
            user_review = PetsitterReview.objects.filter(
                user_id=id, reviewer_id=reviewer.id
            ).first()
            if user_review:
                messages.error(
                    request, 'You have already given review to this user !'
                )
                return redirect(f"/search/petsitter_profiles/{id}")
            data.save()
            messages.success(request, 'Thank you for your review!')
        else:
            print(review_form.errors)
            request.session["review_form_errors"] = review_form.errors
            review_form = PetsitterReviewForm(data=request.POST or None)
            return render(request, 'reviews/review.html', context)
        return HttpResponseRedirect(f'/search/petsitter_profiles/{id}')
