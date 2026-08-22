from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from projects.models import Project
from developers.models import DeveloperProfile

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'core/home.html')

@login_required
def dashboard(request):
    projects = request.user.owned_projects.select_related('category').all()
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

@login_required
def project_reviews(request, project_id):
    project = request.user.owned_projects.get(id=project_id)
    return render(request, 'core/reviews.html', {'project': project})

@login_required
def reviewer_dashboard(request):
    if not request.user.is_staff:
        pass
    return render(request, 'core/reviewer_dashboard.html')

@login_required
def licensing_developer(request):
    return render(request, 'core/licensing_developer.html')

@login_required
def licensing_licensee(request):
    return render(request, 'core/licensing_licensee.html')

@login_required
def licensing_admin(request):
    if not request.user.is_staff:
        pass
    return render(request, 'core/licensing_admin.html')

@login_required
def finance_developer(request):
    return render(request, 'core/finance_developer.html')

@login_required
def finance_admin(request):
    if not request.user.is_staff:
        pass
    return render(request, 'core/finance_admin.html')

@login_required
def admin_platform_dashboard(request):
    if not request.user.is_staff:
        pass
    return render(request, 'core/admin_platform_dashboard.html')

@login_required
def admin_operations(request):
    if not request.user.is_staff:
        pass
    return render(request, 'core/admin_operations.html')

@login_required
def api_credentials_view(request):
    return render(request, 'core/api_credentials.html')

@login_required
def webhooks_view(request):
    return render(request, 'core/webhooks.html')

def marketplace_home(request):
    return render(request, 'core/marketplace_home.html')

def marketplace_search(request):
    return render(request, 'core/marketplace_search.html')

def marketplace_detail(request, pk):
    return render(request, 'core/marketplace_detail.html', {'pk': pk})

@login_required
def org_workspace_dashboard(request, org_id):
    return render(request, 'core/workspace/org_dashboard.html', {'org_id': org_id})

@login_required
def project_workspace_dashboard(request, project_id):
    return render(request, 'core/workspace/project_dashboard.html', {'project_id': project_id})

@login_required
def admin_intelligence_dashboard(request):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    return render(request, 'core/admin/intelligence_dashboard.html')

@login_required
def org_governance_dashboard(request, org_id):
    return render(request, 'core/admin/governance_dashboard.html', {'org_id': org_id})
