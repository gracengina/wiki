from django.shortcuts import render
from .models import Flight,Passengers
from django.http import HttpResponseRedirect
from django.urls import reverse 
# Create your views here.
def index(request):
    return render(request ,'flights/index.html',{"flights":Flight.objects.all()}) 

def flight(request , flight_id, Passenger):
    flight=Flight.objects.get(pk=flight_id)
    Passenger=flight.passengers.all()
    return render (request,"flights/flight_id.html", {
        "flight":flight,
        "passengers":Passenger,
        "none_passengers":Passengers.objects.exclude(flight=Flight.objects.all())})

    

def book(request ,  flight_id):
    if request.method=="POST":
        flight=Flight.objects.get(pk=flight_id)
        passenger=Passengers.objects.get(pk=int(request.POST["passenger"]))
        passenger.flight.add(flight)
        return HttpResponseRedirect(reverse("flights", args=(flight.id,)))
        
