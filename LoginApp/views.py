from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.
def login(request):
    username=request.POST['txtName']
    password=request.POST['txtPwd']
    record=User.objects.get(email=username)
    name=record.email
    if username==record.email and password==record.password:
            return  render(request,'index.html',{'name':name})
    else:
            return HttpResponse("Sorry Invalid")
def success(request):
    email=request.POST['txtName']
    password=request.POST['txtPwd']
    mobile=request.POST['txtMob']
    qstn=request.POST['txtQstn']
    ans=request.POST['txtAns']
    data=User(email=email,password=password,mobile=mobile,qstn=qstn,ans=ans)
    data.save()
    return render(request,'login.html')
def signup(request):
    return render(request,'sign.html')
def loginform(request):
    return render(request,'login.html')
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'homepage.html')
def back(request):
    return render(request,'background.html')
