from django.shortcuts import render,redirect,HttpResponse
from django.db.models import Q
from django.contrib import messages
from itertools import chain
from .models import Engifree, Learnfree
# Create your views here.



def engifree(request):
    engi = Engifree.objects.all().order_by('-date_time')

    return render(request,'engifree.html',{'engi':engi})


def learnfree(request):
    learn = Learnfree.objects.all().order_by('-date_time5')
    return render(request,'learnfree.html',{'learn':learn})






def search(request):
    query1 = request.GET.get('query1')




    learn = Learnfree.objects.filter(Q(title5__icontains=query1) | Q(tex5__icontains=query1))


    context = { 'query1':query1,  'learn':learn, }
    return render(request,'search.html',context)








