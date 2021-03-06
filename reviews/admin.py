from django.contrib import admin
from reviews.models import PetsitterReview


class PetsitterReviewAdmin(admin.ModelAdmin):
    list_display = ["description", "stars", "created_at"]


admin.site.register(PetsitterReview, PetsitterReviewAdmin)
