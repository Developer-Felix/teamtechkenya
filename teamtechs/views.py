from django.shortcuts import render,redirect
from django.db.models import Q
from django.views.generic import ListView
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User,auth
from teamtechkenya.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
# Create your views here.


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() # saves in database
            messages.success(request, f"Your message has been sent.Thanks for visiting our site!")
    else:
        form = ContactForm()

    obj = LandingPage.objects.all()
    objabout = About.objects.all()
    object_list = Team.objects.all().order_by('id')
    services = Services.objects.all()
    projects_web = Projects_web.objects.all()
    projects_loan = Projects_loan.objects.all()
    projects_webstartup = Projects_webstartup.objects.all()
    context = {
        'obj':obj,
        'objabout':objabout,
        'object_list':object_list,
        'services':services,
        'projects_web':projects_web,
        'projects_loan':projects_loan,
        'projects_webstartup':projects_webstartup,
        'form':form
    }

    return render(request,'teamtechs/index.html',context=context)


#registration
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username has been taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password1)
                # subject = 'TeamTechkenya Registration'
                # message = 'Hae welcome to teamtechkenya software development company send send work to this email or learning session go to www.teamtechkenya/learningsessions and register with us. we are glad coding with you.'
                # recepient = str(email['email'].value())
                # send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
                user.save()
                messages.success(request, 'Congrats for signing up!')
                return redirect('login')
        else:
            messages.info(request, 'password does not match')
            return redirect('signup')

    else:
        return render(request,'registration/signup.html',{'title':'signup'})


def codewithttk(request):
    ttk = Codewithttk.objects.all()
    return render(request,'teamtechs/codewithttk.html',{'ttk':ttk})
    

def registerwithttk(request):
	if request.method == 'POST':
	    email = request.POST['email']
	    form = RegisterWithTTKForm(request.POST)
	    if form.is_valid():
		    
		    subject = 'TeamTechkenya Learning sessions admissions'
		    message = 'Hae welcome to teamtechkenya learning session platform where we will help you grow in your coding skills. Wait for the release of our modules by the end of the week.Happy coding with teamtechkenya'
		    recepient = str(form['email'].value())
		    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
		    form.save() # saves in database
		    #return redirect('home')
		    messages.success(request, f"Your message has been sent.Thanks for visiting our site!")
	else:
		form = RegisterWithTTKForm()
	return render(request,'teamtechs/registerwithttk.html',{'form': form})
    
    
