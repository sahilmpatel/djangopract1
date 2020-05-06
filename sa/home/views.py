from django.shortcuts import render, redirect
from .forms import profieform,loginform
from django.conf import settings
from django.core.mail import send_mail
from .models import profile,Userdetails
# Create your views here.
def home(request):
    temp = 'index.html'
    if request.session.get('email') == None:
        return redirect("Home:loginuser")


    return render(request, temp, {})

def profileshow(request):
    temp = "profile.html"

    if request.method == "POST":
        form = profieform(request.POST or None)
        if form.is_valid():
            regform = form.save(commit=False)
            name = request.POST.get('name')
            passwd = request.POST.get('password')
            conf_passwd = request.POST.get('conf_password')
            email = request.POST.get('email')
            if (passwd == conf_passwd):
                regform.save()
                Userdetails.objects.create(u_name=name)
                request.session["email"] = email
                # email for welcome
                subject = "sa@hil"
                message = "We will we will rock you"
                email_from = settings.EMAIL_HOST_USER
                email_to = [email, ]
                send_mail(subject, message, email_from, email_to)
                # email logic complate
                return redirect('Home:home')
    else:
        form = profieform()
    return render(request,temp,{"form":form})

def loginuser(request):
    temp = "login.html"
    if request.method == 'POST':
        form = loginform(request.POST or None)
        if form.is_valid():
            email = request.POST.get("email")
            password = request.POST.get("password")

            isemail = profile.objects.filter(email__iexact=email).exists()
            ispass = profile.objects.filter(password__iexact=password).exists()

            if isemail and ispass:
                check = profile.objects.get(email=email)
                if check.password == password:
                    request.session["email"] = email

                    return redirect("Home:home")

    else:
        form = loginform()

    return render(request,temp,{"form":form})







def proshow(request):
    temp = "jakaas.html"
    show = profile.objects.all()
    return render(request,temp,{"show":show})


def showbyorder(request):
    temp = "orderby.html"
    show = profile.objects.order_by('birthdate')
    return render(request,temp,{"show":show})


def hey(request):
    temp = "signin.html"
    return render(request,temp)

def logoutuser(request):
    temp = "logout.html"
    if request.session.get('email') == None:
       return redirect("Home:loginuser")


    return render(request,temp)


def logoutdone(request):

    if request.session.get("email") != None:
        del request.session["email"]
        return redirect("Home:loginuser")

    else:
        return redirect("Home:loginuser")





