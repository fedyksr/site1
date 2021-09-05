from django.urls import path
from .views import *
from cuhc import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "cuhc"
urlpatterns = [
    path('',views.cuhcpage,name='home'),
     path("register/",
          EtudiantRegistrationView.as_view(), name="etudiantregistration"),

    path("logout/", EtudiantLogoutView.as_view(), name="etudiantlogout"),
    path("login/", EtudiantLoginView.as_view(), name="etudiantlogin"),

]

if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)