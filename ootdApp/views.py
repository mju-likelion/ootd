from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Image
from .form import createForm
from django.core.paginator import Paginator


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

def feedback(request):
    images = Image.objects

    posts = Image.objects.all()
    paginator = Paginator(posts, 8)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)

    page_numbers_range = 10

    max_index = len(paginator.page_range)
    current_page = int(page) if page else 1
    start_index = int((current_page -1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range

    if end_index >= max_index:
        end_index = max_index
    paginator_range = paginator.page_range[start_index:end_index]

    return render(request, 'feedback.html', {'images': images, 'posts': posts, 'paginator_range': paginator_range})

def createPage(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        form = createForm()
        return render(request, 'create.html', {"form": form})


def createFuction(request):
    images = Image()
    images.title = request.POST.get('title', False)
    images.description = request.POST.get('description', False)
    images.src = request.FILES.get('photo', False)
    images.save()
    messages.info(request, 'ADD')
    return redirect('feedbackPage')


def updatePage(request, update_id):
    update = get_object_or_404(Image, pk=update_id)
    form = createForm()
    return render(request, 'update.html', {'content': update, "form": form})


def updateFuction(request, update_id):
    update = get_object_or_404(Image, pk=update_id)
    if request.method == "POST":
        update.title = request.POST.get('title', False)
        update.description = request.POST.get('description', False)
        update.src = request.FILES.get('photo', False)
        update.save()
        messages.info(request, 'UPDATE')
        return redirect('feedbackPage')


def deleteFuction(request, delete_id):
    image = get_object_or_404(Image, pk=delete_id)
    if request.method == "GET":
        image.delete()
        messages.info(request, 'DELETE')
        return redirect('feedbackPage')
    else:
        pass

def detailPage(request, detail_id):
    detail = get_object_or_404(Image, pk=detail_id)
    return render(request, 'detail.html', {'detail': detail})