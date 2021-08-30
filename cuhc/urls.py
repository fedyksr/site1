from django.urls import path
from .views import *
from cuhc import views


app_name = "cuhc"
urlpatterns = [

     path("register/",
          EtudiantRegistrationView.as_view(), name="etudiantregistration"),

    path("logout/", EtudiantLogoutView.as_view(), name="etudiantlogout"),
    path("login/", EtudiantLoginView.as_view(), name="etudiantlogin"),

]

