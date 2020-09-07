from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def ranking(request):
    return render(request, 'ranking.html')

def login(request) :
    return render(request, 'login.html')

def signup(request) :
    return render(request, 'signup.html')

def findid(request) :
    return render(request, 'findid.html')

def findidofphone(request) :
    return render(request, 'findidofphone.html')

def findpw(request) :
    return render(request, 'findpw.html')  

def findpwofphone(request) :
    return render(request, 'findpwofphone.html')    

