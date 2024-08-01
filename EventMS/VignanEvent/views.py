from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import UsForm, Eventform
from django.contrib import messages
from .models import EventModel
# Create your views here.
def home(request):
    return render(request,'htmlfiles/home.html')

def About(request):
    return render(request,'htmlfiles/About.html')

def Login(request):
    return render(request,'htmlfiles/Login.html')

def Sidebar(request):
    return render(request, 'htmlfiles/sidebar.html')
    
def First(request):
    return render(request, 'htmlfiles/First.html')

def Events(request):
    k = EventModel.objects.all()
    return render(request, 'htmlfiles/Eventlist.html',{'em':k})

def AddEvent(request):
    if request.method == "POST":
        e = Eventform(request.POST)
        if e.is_valid():
            m = e.save(commit = False)
            m.save() 
            return HttpResponseRedirect('?submitted=True')
    else:
        e = Eventform()
    submitted = 'submitted' in request.GET
    return render(request, 'htmlfiles/AddEvent.html', {'us':e, 'submitted':submitted})

def Register(request):
    if request.method == "POST":
        u = UsForm(request.POST)
        if u.is_valid():
            d = u.save(commit = False)
            messages.success(request, f"{d.username} User created successfully")
            d.save()
            return redirect('/Register') 
            
    else:
        u = UsForm()
    return render(request,'htmlfiles/Register.html', {'us':u})

def Farewell(request):
    return render(request, 'htmlfiles/Farewell.html')

def OfficeBearers(request):
    return render(request, 'htmlfiles/Organizers.html')

def Culturals(request):
    return render(request, 'htmlfiles/culturals.html')


