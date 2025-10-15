from django.shortcuts import render,HttpResponse, Http404
import mimetypes

# Create your views here.
def index(request):
    return render(request,'index.html')

def searchtoolsjobs(request):
    return render(request,'search_jobs_tools.html')

def privacy_policy(request):
    return render(request,'privacy_policy.html')

def about_us(request):
    return render(request, 'about_us.html')


def downloadapp(request):
    return render(request,'download_apk.html' )

import os

# Django project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#
# Download APK file
#
def download_apk(request, toolsandjobs):
    print('Download ' + toolsandjobs + '.apk...')
    # Full path of file
    file_path = BASE_DIR + '/webtools1/files/' + toolsandjobs + '.apk'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/force_download")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    # If file is not exists
    raise Http404

