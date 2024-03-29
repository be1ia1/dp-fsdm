from django.shortcuts import render, redirect
from . import models
from django.urls import reverse

# Create your views here.
def list(request):
    all_cars = models.Car.objects.all()
    contex = {'all_cars':all_cars}
    return render(request, 'cars/list.html', context=contex)

def add(request):
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
        models.Car.objects.create(brand=brand, year=year)
        return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/add.html')

def delete(request):
    if request.POST:
        pk = request.POST['pk']
        try:
            models.Car.objects.get(pk=pk).delete()
            return redirect(reverse('cars:list'))
        except:
            print('PK not found!')
            return redirect(reverse('cars:list'))

    else:
        return render(request, 'cars/delete.html')