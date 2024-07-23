from django.shortcuts import render, redirect
from register.models import reg
# Create your views here.

def register(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if reg.objects.filter(username=username).exists():
            print('username taken')
        elif reg.objects.filter(email=email).exists():
            print('email taken')
        else:
            user= reg.objects.create( email=email,username=username,password=password,name=name)
            user.save()
            print('user created')
            return render(request,'login.html')

    else:
        return render(request,'register.html')



