from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls.base import reverse_lazy
from django.views.generic.base import View
from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django.views.generic.edit import CreateView, FormView
from .models import *
from .forms import *

# Create your views here.
def cuhcpage(request):
    list_article=article.objects.all()
    context={"liste_articles":list_article}
    return render(request,'index1.html',context)

class EtudiantRegistrationView(CreateView):
    template_name = "etudiantregistration.html"
    form_class = EtudiantRegistrationForm
    success_url = reverse_lazy('cuhc:home')

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        user = User.objects.create_user(username, email, password)
        form.instance.user = user
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url
class  EtudiantLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('cuhc:home')


class  EtudiantLoginView(FormView):
    template_name = "etudiantlogin.html"
    form_class = EtudiantLoginForm
    success_url = reverse_lazy('cuhc:home')

    # form_valid method is a type of post method and is available in createview formview and updateview
    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Etudiant.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Invalid credentials"})

        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url
