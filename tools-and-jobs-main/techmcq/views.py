from django.shortcuts import render
from .models import TechMCQ,Category
from django.views import generic
from django.db.models import Q
from django.core.paginator import Paginator



# Create your views here.
class TestList(generic.ListView):
    queryset = TechMCQ.objects.order_by('-created_on1')
    template_name = 'test-list.html'
    paginate_by = 7


class SearchResultsView(generic.ListView):
    model = TechMCQ
    template_name = 'search_mcq.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = TechMCQ.objects.filter(
            Q(titles1__icontains=query) | Q(contents1__icontains=query)
        )
        return object_list


class TestDetail(generic.DetailView):
    model = TechMCQ
    template_name = 'test_detail.html'
    slug_field = 'slug1'
    slug_url_kwarg = 'slug1'



class CatListView(generic.ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'



    def get_queryset(self):
        content = {
                'cat':self.kwargs['category'],
                'mcqs': TechMCQ.objects.filter(category__name = self.kwargs['category']).filter(status = '1'),

        }

        return content

def category_list(request):
    request.category_list = Category.objects.exclude(name = 'default')
    content = {
        'category_list': category_list
    }
    return content




