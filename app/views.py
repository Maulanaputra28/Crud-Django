from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import users
from django.contrib import messages
from django.db.models import Q
import json

# Create your views here.

def index(request):
    context={
        'name':'dimas pasha ramadhan'
    }
    return render(request, 'index.html',context)

def admin(request):
    data_user = users.objects.all()
    context = {
        'data_user' : data_user
    }
    return render(request, 'admin.html', context)

def login(request):
    context={
        'text' : 'login'
    }
    return render(request, 'login.html',context)

def tambah_user(request):
    return render(request, 'tambah_user.html')

def post_user(request):
    username = request.POST['username']
    password = request.POST['password']
    alamat = request.POST['alamat']

    tambah_user = users(
        username = username,
        password = password,
        alamat = alamat
    )
    tambah_user.save()
    messages.success(request, 'berhasil input')
    return redirect('/admin')

def update_user(request, id):
    data_user = users.objects.get(id=id)
    context = {
        'data_user' : data_user
    }
    return render(request, 'update_user.html', context)

def delete_user(request, id):
    user = users.objects.get(id=id).delete()
    messages.success(request, 'BERHASIL DELETE AKUN')
    return redirect(request.META.get('HTTP_REFERER', '/'))

def postupdate_user(request, id):
    username = request.POST['username']
    password = request.POST['password']
    alamat = request.POST['alamat']

    user = users.objects.get(id=id)
    user.username = username
    user.password = password
    user.alamat = alamat
    user.save()

    messages.success(request, 'BERHASIL UPDATE USER')
    return redirect('/admin')