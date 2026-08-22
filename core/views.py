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
    return render(request, 'core/dashboard.html', {'projects': projects, 'profile': profile})

@login_required
def project_compliance(request, project_id):
    project = request.user.owned_projects.get(id=project_id)
    return render(request, 'core/compliance.html', {'project': project})

@login_required
def project_repository(request, project_id):
    project = request.user.owned_projects.get(id=project_id)
    return render(request, 'core/repository.html', {'project': project})

@login_required
def project_security(request, project_id):
    project = request.user.owned_projects.get(id=project_id)
    return render(request, 'core/security.html', {'project': project})
