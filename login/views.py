from django.contrib import messages
from django.shortcuts import render, redirect
from register.models import reg

def login(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        user = reg.objects.filter(name=name, password=password)
        if user:
            user_details = reg.objects.get(name=name, password=password)
            id = user_details.id
            name = user_details.name
            request.session['id'] = id
            request.session['name'] = name
            return redirect('/home/home')
        else:
            return render(request,'register.html')
    else:
        return render(request, 'login.html')

def logout(request):
    return render(request,'login.html')