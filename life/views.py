from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from life.models import Flight, Aircraft
from life.forms import NewFlightForm

def index(request):
    return render(request, 'life/index.html')

def add(request):
    if request.method == 'POST':
        form = NewFlightForm(request.POST)
        if form.is_valid():
            # find if aircraft already exists, otherwise make new aircraft
            # form.cleaned_data
            flight = Flight()
            return JsonResponse({'status':'success'},status=200)        
    else:
        form = NewFlightForm()
    return render(request, 'life/add.html', {'form': form})

def display(request):
    #import pdb
    #pdb.settrace()
    print(Flight.objects.all())
    return render(request, 'life/display.html', {'flights': Aircraft.objects.all(), 'aircraft': Flight.objects.all()})