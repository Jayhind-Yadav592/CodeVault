from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from projects.models import Project
from developers.models import DeveloperProfile

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'core/home.html')

@login_required
def dashboard(request):
    projects = request.user.owned_projects.all()
    try:
        profile = request.user.developer_profile
    except DeveloperProfile.DoesNotExist:
        profile = None

    context = {
        'projects': projects,
        'profile': profile,
    }
    return render(request, 'core/dashboard.html', context)
