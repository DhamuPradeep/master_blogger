from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import WritingForm,UpdateUserForm
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'posts':posts})

def post(request,pk):
    post = Post.objects.get(id=pk)
    return render(request,'post.html',{'post':post})

def register(request):
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        conform_password = request.POST["conform_password"]
        if password == conform_password:
            if User.objects.filter(email = email).exists():
                messages.info(request,'Email already exist')
                return redirect('register')
            elif User.objects.filter(username = username).exists():
                messages.info(request,'Username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save()
                messages.info(request,'Account created successfully')
                return redirect('/')
        else:
            messages.info(request, 'Passwords are not same')
            return redirect('register')
    else:
        return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Email ID or Password")
            return redirect('login')
    else:
        return render(request,'login.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        #profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid():
            user_form.save()
            #profile_form.save()
            #messages.success(request, 'Your profile is updated successfully')
            return redirect('user_profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        #profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'edit_profile.html', {'user_form': user_form})

def writingposts(request):
    if request.method == 'POST':
        form = WritingForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = WritingForm()
    return render(request,"writingposts.html",{'form' : form})

def user_profile(request):
    return render(request,'user_profile.html')



def logout(request):
    auth.logout(request)
    return redirect('/')