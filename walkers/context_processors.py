from newsletter.forms import NewsletterUserForm

def global_variables(request):
   newsletter_email = NewsletterUserForm()
   context = {'newsletter_email': newsletter_email}
   return context