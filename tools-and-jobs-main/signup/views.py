from django.shortcuts import render,redirect,HttpResponse
from django.core.mail import send_mail
from .models import Signup,Contact
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.
def suscribe(request):
    if request.method == 'POST':
        user = Signup()
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.job_field = request.POST['job_field']
        if user.first_name =="" or user.last_name =="" or user.email =="" or user.job_field=="":

            messages.info(request, 'Some fields are empty try to fill all')
            return redirect('suscribe')
        else:
            messages.success(request, 'Your subscription is submitted succesfully we will send you the best tools & jobs you needed kindly verify email'
                                      )
            user.save()
            sign = Signup.objects.last()
            html_message = render_to_string('mail_subscribe.html', {'sign': sign})
            plain_message = strip_tags(html_message)
            email_to = sign.email
            email_from = settings.EMAIL_HOST_USER
            send_mail(
                'Free subscription for job alerts & web tools',
                plain_message,
                email_from,
                [email_to],
                html_message=html_message,
                fail_silently=False,
            )
            return render(request, 'signup.html', {'sign': sign})


    return render(request,'signup.html')


def contactus(request):
    if request.method == "POST":
        con = Contact()
        con.full_name = request.POST['full_name']
        con.email1 = request.POST['email1']
        con.msg = request.POST['msg']

        #context = {'name':con.full_name}

        if con.full_name=="" or con.email1=="" or con.msg=="" :
            messages.info(request, 'Some fields are empty')
            return redirect('contactus')
        else:
            messages.success(request,'Your contact is submitted succesfully we will approch you via your email',)
            con.save()
            name = Contact.objects.last()
            html_message = render_to_string('mail_contact.html', {'name': name})
            plain_message = strip_tags(html_message)
            email_to = name.email1
            email_from = settings.EMAIL_HOST_USER
            send_mail(
                'Free subscription for job alerts & web tools',
                plain_message,
                email_from,
                [email_to],
                html_message=html_message,
                fail_silently=False,
            )
            return render(request, 'contact.html',{'name':name})

    return render(request,'contact.html')

