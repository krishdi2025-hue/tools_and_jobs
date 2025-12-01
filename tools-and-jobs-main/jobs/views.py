from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import add_jobs
from .forms import add_jobsForm
from django.http import HttpResponseForbidden
from .permissions import is_company_user, is_owner_of_job

# -------------------------
# Helper
# -------------------------
def user_can_modify(request, job):
    """Compatibility wrapper used by templates or other code.

    Returns True when the requesting user is allowed to modify the job.
    Uses `is_company_user` and `is_owner_of_job` helpers for robust checks.
    """
    if getattr(request.user, 'is_staff', False):
        return True
    return is_company_user(request.user) and is_owner_of_job(job, request.user)

# -------------------------
# List view
# -------------------------
def jobs(request):
    jobs_list = add_jobs.objects.all().order_by('-date_time')
    return render(request, "jobs/jobs.html", {"jobs_list": jobs_list})

# -------------------------
# Add job
# -------------------------
@login_required
def add_job(request):
    if not is_company_user(request.user):
        return HttpResponseForbidden("Only company accounts may create job posts.")
    
    if request.method == "POST":
        form = add_jobsForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.posted_by = getattr(request.user, 'company', request.user)
            job.save()   # PK is assigned here
            messages.success(request, "Job added successfully.")
            # Redirect to the edit page of the newly created job using the auto-assigned PK
            return redirect("jobs:edit_job", pk=job.pk)

            # return redirect("jobs:edit_job", pk=job.pk)
        else:
            print("Form is invalid:", form.errors)
    else:
        form = add_jobsForm()

    return render(request, "jobs/jobs_add.html", {"form": form})

# -------------------------
# Edit job
# -------------------------

# @login_required
# def edit_job(request, pk):
#     job = get_object_or_404(add_jobs, pk=pk, user = request.user)


#     if request.method == "POST":
#         # include request.FILES here so file inputs are processed
#         form = add_jobsForm(request.POST, request.FILES, instance=job)
#         if form.is_valid():
#             form.save(commit=False)
#             job.user = request.user
#             # job.posted_by = getattr(request.user, 'company', request.user)
#             form.save()
#             messages.success(request, "Job updated successfully.")
#             return redirect("jobs:jobs_list",pk=job.pk)
#         else:
#             print("form errors:", form.errors)   # debug
#             print("FILES:", request.FILES)       # debug
#     else:
#         form = add_jobsForm(instance=job)

#     return render(request, "jobs:edit_job.html", {"form": form, "job": job})

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages

@login_required
def edit_job(request, pk):
    job = get_object_or_404(add_jobs, pk=pk)   # do not filter by user here

    # permission: owner OR posted company OR staff/superuser
    is_owner = (job.user_id is not None and job.user == request.user)
    user_company = getattr(request.user, "company", None)
    is_company_poster = (user_company is not None and job.posted_by == user_company)
    is_staff = request.user.is_staff or request.user.is_superuser

    if not (is_owner or is_company_poster or is_staff):
        return HttpResponseForbidden("You are not allowed to edit this job.")

    if request.method == "POST":
        form = add_jobsForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            updated_job = form.save(commit=False)
            # do NOT overwrite updated_job.user unless you intentionally want to change owner
            updated_job.save()
            messages.success(request, "Job updated successfully.")
            return redirect("jobs:jobs_list")   # or redirect("jobs:edit_job", pk=updated_job.pk)
        else:
            print("form errors:", form.errors)
    else:
        form = add_jobsForm(instance=job)

    # NOTE: use a filesystem-style path, not a namespaced path with a colon
    return render(request, "jobs/edit_job.html", {"form": form, "job": job})

# -------------------------
# Delete job
# -------------------------
from django.views.decorators.http import require_POST
@login_required
def delete_job(request, pk):
    job = get_object_or_404(add_jobs, pk=pk,user = request.user)
    if request.method == "POST":
        job.delete()
        messages.success(request, "Job deleted successfully.")
        return redirect("jobs:jobs_list")
    return render(request, "jobs/confirm_delete_job.html", {"job": job})



def about_job(request, pk):
    job = get_object_or_404(add_jobs, pk=pk)
    return render(request, "jobs/about_job.html", {"job": job})



@login_required
def job_apply(request, pk):
    job = get_object_or_404(add_jobs.objects.select_related('posted_by'), pk=pk)
    # Prevent applying to your own job: check ownership via helper
    if is_owner_of_job(job, request.user):
        messages.error(request, "You cannot apply to your own job.")
        return redirect('jobs:about_job', pk=pk)

    # implement application logic here (create Application model entry, send email, etc.)
    # For demo:
    messages.success(request, "Application submitted (demo).")
    return redirect('jobs:detail', pk=pk)
