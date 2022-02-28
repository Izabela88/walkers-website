from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def petsitters_list(request):
    return render(request, 'search/petsitters_list.html')