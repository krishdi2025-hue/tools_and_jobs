from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import  Engineering,Busi_Management_administration,Communication,Sales
from django.db.models import Q

# Create your views here.
def jobs(request):
    return render(request,'jobs.html')

def engineering(request, eng_id=id):
    engineer = Engineering.objects.all().order_by('-date_time')
    return render(request,'engineer.html',{'engineer':engineer})


def business(request):
    busi = Busi_Management_administration.objects.all().order_by('-date_time6')
    return render(request,'business.html',{'busi':busi})

def sales(request):
    sal = Sales.objects.all().order_by('-date_time8')
    return render(request,'sales.html',{'sal':sal})

def communication(request):
    com = Communication.objects.all().order_by('-date_time1')
    return render(request,'communication.html',{'com':com})

def search1(request):
    query = request.GET.get('query')


#search queries
    engineer = Engineering.objects.filter(Q(head__icontains=query)|Q(desc__icontains=query)|Q(loc__icontains=query)|Q(desc__icontains=query)
                                          |Q(ind_type__icontains=query)|Q(func_area__icontains=query)|Q(role__icontains=query)|Q(empl_type__icontains=query)|Q(edu_or_elig__icontains=query))



    busi = Busi_Management_administration.objects.filter(Q(head6__icontains=query)|Q(desc6__icontains=query)|Q(loc6__icontains=query)|Q(desc6__icontains=query)
                                          |Q(ind_type6__icontains=query)|Q(func_area6__icontains=query)|Q(role6__icontains=query)|Q(empl_type6__icontains=query)|Q(edu_or_elig6__icontains=query))


    sal = Sales.objects.filter(Q(head8__icontains=query)|Q(desc8__icontains=query)|Q(loc8__icontains=query)|Q(desc8__icontains=query)
                                          |Q(ind_type8__icontains=query)|Q(func_area8__icontains=query)|Q(role8__icontains=query)|Q(empl_type8__icontains=query)|Q(edu_or_elig8__icontains=query))

    com = Communication.objects.filter(Q(head9__icontains=query)|Q(desc9__icontains=query)|Q(loc9__icontains=query)|Q(desc9__icontains=query)
                                          |Q(ind_type9__icontains=query)|Q(func_area9__icontains=query)|Q(role9__icontains=query)|Q(empl_type9__icontains=query)|Q(edu_or_elig9__icontains=query))



    context = { 'query':query ,'engineer':engineer,
                'busi':busi,'sal':sal,'com':com,}
    return render(request,'search1.html',context)


