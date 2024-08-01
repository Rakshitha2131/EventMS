from django.urls import path
from VignanEvent import views 
from django.contrib.auth import views as v

urlpatterns = [
    path('',views.home, name = "hm"),
    path('about/',views.About, name = "ab"),
    path('Register',views.Register, name = "reg"),
    path('Connect/',views.Sidebar, name="side"),
    path('login/',v.LoginView.as_view(template_name = "htmlfiles/login.html"),name = "lgn"),
    path('logout/',v.LogoutView.as_view(template_name = "htmlfiles/logout.html"),name = "lgout"),
    path('Firstpage/',views.First, name = "fp"),
    path('Eventlist/', views.Events, name = "evtli"),
    path('AddEvent/',views.AddEvent, name = "add"),
    path('Farewell/',views.Farewell, name = "fw"),
    path('Organizers',views.OfficeBearers, name = "ofc"),
    path('Culturals',views.Culturals, name = "cul"),
]