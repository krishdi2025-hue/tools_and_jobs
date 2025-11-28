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
from .models import add_jobs
from .forms import add_jobsForm
from django.contrib.auth.decorators import login_required   # optional

# list view (unchanged)
def jobs(request):
    jobs_list = add_jobs.objects.all()
    return render(request, 'jobs.html', {'jobs_list': jobs_list})

# add job (handles POST + FILES and shows errors)
# @login_required   # uncomment if only logged-in/company users should add jobs
def add_job(request):
    if request.method == 'POST':
        form = add_jobsForm(request.POST, request.FILES)   # <-- include request.FILES
        if form.is_valid():
            form.save()
            return redirect('jobs')
        else:
            # keep form with errors to render on template and for debugging
            print("Form is invalid:", form.errors)   # server console
    else:
        form = add_jobsForm()

    return render(request, 'jobs_add.html', {'form': form})
