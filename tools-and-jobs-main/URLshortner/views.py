from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import Route
from .forms import RouterForm
from django.views.generic import ListView

# Create your views here.
def ushort(request):
    BASE_URL = request.build_absolute_uri('/')
    # return HttpResponse('Site is working')
    form = RouterForm(request.POST or None)
    if form.is_valid():
        form.save()
        key = form.cleaned_data.get('key')
        messages.success(request, f"{BASE_URL}{key}")
        return render(request, 'URL/link.html')
    return render(request, 'URL/urlindex.html', {"form": form})

#def how_to(request):
    # return HttpResponse("<h1>About Page</h1>")
#    return render(request, 'router/how_to_use.html')

#class URLListView(ListView):
 #   model = Route
  #  context_object_name = 'urls'
  #  paginate_by = 10

def redirector(request, key):

    instance = get_object_or_404(Route, key= key)
    return redirect(instance.original_url)