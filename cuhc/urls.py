from os import name
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
urlpatterns = [
    path('',views.cuhcpage,name='cuhcpage'),
    path('cuhcsecpage',views.cuhcsecpage,name='cuhcsecpage'),
    path('cuhcthirdpage',views.cuhcthirdpage,name='cuhcthirdpage'),
    path('myimgpage',views.myimgpage,name='myimgpage'),

]
