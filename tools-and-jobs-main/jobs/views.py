# from .models import *
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import add_jobs
# from .forms import add_jobsForm


# def jobs(request):
#     jobs_list = add_jobs.objects.all()
#     return render(request, 'jobs.html', {'jobs_list': jobs_list})

# def add_job(request):
#     return render(request, 'jobs_add.html')

# def edit_job(request, job_id):
#     job = get_object_or_404(add_jobs, id=job_id)
#     if request.method == 'POST':
#         form = add_jobsForm(request.POST, instance=job)
#         if form.is_valid():
#             form.save()
#             return redirect('jobs')
#     else:
#         form = add_jobsForm(instance=job)
#     return render(request, 'jobs_edit.html', {'form': form})


# from django.shortcuts import render, redirect, get_object_or_404
# from .models import add_jobs
# from .forms import add_jobsForm
# from django.contrib.auth.decorators import login_required  # optional

# def jobs(request):
#     jobs_list = add_jobs.objects.all()
#     return render(request, 'jobs.html', {'jobs_list': jobs_list})

# # optional: require login/company user
# # @login_required
# def add_job(request):
#     if request.method == 'POST':
#         form = add_jobsForm(request.POST, request.FILES)   # <-- include FILES
#         if form.is_valid():
#             form.save()
#             return redirect('jobs')                       # or wherever you want
#         else:
#             # helpful for debugging: show errors in template
#             print(form.errors)
#     else:
#         form = add_jobsForm()

#     return render(request, 'jobs_add.html', {'form': form})
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import add_jobs
from .forms import add_jobsForm

# -------------------------
# Helper
# -------------------------
def user_can_modify(request, job):
    if request.user.is_staff:
        return True
    if hasattr(job, "owner"):
        return job.owner == request.user
    if hasattr(request.user, "company_name") and hasattr(job, "company_name"):
        return job.company_name == request.user.company_name
    return False

# -------------------------
# List view
# -------------------------
def jobs(request):
    """
    Shows all jobs. URL name should be: 'jobs:jobs_list'
    (the view function name can remain 'jobs' for compatibility).
    """
    jobs_list = add_jobs.objects.all()
    return render(request, "jobs/jobs.html", {"jobs_list": jobs_list})

# -------------------------
# Add job
# -------------------------
@login_required
def add_job(request):
    """
    Use template: templates/jobs/jobs_add.html
    URL name should be: 'jobs:jobs_add'
    """
    if request.method == "POST":
        form = add_jobsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Job added successfully.")
            return redirect("jobs:jobs_list")
        else:
            # server-side debug print (optional)
            print("Form is invalid:", form.errors)
    else:
        form = add_jobsForm()

    return render(request, "jobs/jobs_add.html", {"form": form})

# -------------------------
# Edit job
# -------------------------

@login_required
def edit_job(request, pk):
    job = get_object_or_404(add_jobs, pk=pk)

    if not user_can_modify(request, job):
        messages.error(request, "You don't have permission to edit this job.")
        return redirect("jobs:jobs_list")

    if request.method == "POST":
        # include request.FILES here so file inputs are processed
        form = add_jobsForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, "Job updated successfully.")
            return redirect("jobs:jobs_list")
        else:
            print("form errors:", form.errors)   # debug
            print("FILES:", request.FILES)       # debug
    else:
        form = add_jobsForm(instance=job)

    return render(request, "jobs/edit_job.html", {"form": form, "job": job})

# -------------------------
# Delete job
# -------------------------
@login_required
def delete_job(request, pk):
    """
    Use template: templates/jobs/confirm_delete_job.html
    After delete redirect to 'jobs:jobs_list'
    """
    job = get_object_or_404(add_jobs, pk=pk)

    if not user_can_modify(request, job):
        messages.error(request, "You don't have permission to delete this job.")
        return redirect("jobs:jobs_list")

    if request.method == "POST":
        job.delete()
        messages.success(request, "Job deleted successfully.")
        return redirect("jobs:jobs_list")

    return render(request, "jobs/confirm_delete_job.html", {"job": job})


def about_job(request, pk):
    job = get_object_or_404(add_jobs, pk=pk)
    return render(request, "jobs/about_job.html", {"job": job})
