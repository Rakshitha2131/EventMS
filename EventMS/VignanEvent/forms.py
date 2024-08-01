from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import EventModel
class UsForm(UserCreationForm):
    password1 = forms.CharField(widget = forms.PasswordInput(attrs = {"class":"form-control my-2", "placeholder":"Enter password"}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs = {"class":"form-control my-2", "placeholder":"Confirm password"}))

    class Meta:
        model = User 
        fields = ["username"]
        widgets = {
            "username":forms.TextInput(attrs = {
                "class":"form-control my-2",
                "placeholder":"Username",
            }),
        }

class Eventform(forms.ModelForm):
    class Meta:
        model = EventModel 
        fields = ["Event_name","date","venue_name"]
        widgets = {
            "Event_name":forms.TextInput(attrs = {
                "class":"form-control my-2",
                "placeholder":"Enter the name of the event",}),

            "date":forms.TextInput(attrs = {
                "class":"form-control my-2",
                "placeholder":"Enter the date of the event",}),
            
            "venue_name":forms.TextInput(attrs = {
                "class":"form-control my-2",
                "placeholder":"Enter the venue of the event",}) 
            
            

        }