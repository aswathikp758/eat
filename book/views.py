from django.shortcuts import render, redirect
from .models import booking


def book(request):
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        persons = request.POST['persons']
        date = request.POST['date']
        time = request.POST['time']

        user = booking.objects.create(name=name, number=number, persons=persons, date=date ,time=time,)
        user.save()
        print('Table Reserved')
        return redirect('/home/home')
    else:
        return render(request,'book.html')