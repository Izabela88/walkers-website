from django.contrib import admin
from newsletter.models import NewsletterUser

# Register your models here.
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_subscribed']


admin.site.register(NewsletterUser, NewsletterAdmin)