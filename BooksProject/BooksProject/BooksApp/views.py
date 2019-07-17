from django.shortcuts import render
from .form import contactForm,BookForm,UserForm,ProfileForm,LoginForm
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.urls import reverse
from django.contrib import messages
from .models import Book
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate,login,logout
@login_required
def SetContact(req):
    form = contactForm()
    if req.method =='POST':
        form = contactForm(req.POST)
        if form.is_valid():
            form.save(commit =True)
            messages.success(req,"Thank you")
            return HttpResponseRedirect(reverse('contact'))
    return render(req,"contact.html",context={"form":form})
@login_required
def addBook(req):
    form = BookForm()
    if req.method == 'POST':
        form = BookForm(req.POST)
        if form.is_valid():
            data = form.save(commit=False)
            if 'picture' in req.FILES:
               data.picture = req.FILES['picture']
            data.save()
            messages.success(req,'Thank you for Add Book')
            return HttpResponseRedirect(reverse('addbook'))
    return render(req,'Book.html',context={"form":form})

def index(req):
    data =Book.objects.all()
    return render(req,'home.html',context={'data':data})

def details(req,pk):
    try:
        data = Book.objects.get(id =pk)
    except:
        raise Http404()
    return render(req,'details.html',context={'data':data})

def register(req):
    UserF = UserForm()
    ProfileF = ProfileForm()
    if req.method =="POST":
        UserF = UserForm(req.POST)
        ProfileF = ProfileForm(req.POST)
        if UserF.is_valid() and ProfileF.is_valid():
            datau = UserF.save(commit=False)
            datau.set_password(datau.password)
            datau.save()
            datap = ProfileF.save(commit=False)
            datap.user = datau
            datap.save()
            messages.success(req,'successfully register')
        return HttpResponseRedirect(reverse('home'))
    return render(req,'register.html',context={'UForm':UserF, 'PForm':ProfileF})


def user_login(req):
    form = LoginForm()
    if req.method =='POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username,password=password)
            if user:
                if user.is_active:
                    login(req,user)
                    return HttpResponseRedirect(reverse('home'))
                else:
                    messages.error(req,"user is not active")
            else:
                messages.error(req,"invalid username or password, Try Again")
    return render(req,'login.html',{'form':form})
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))