from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from django.urls import reverse

from apps.users.forms import LoginForm
# Create your views here.


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        user_name = request.POST.get("username","")
        password = request.POST.get("password","")

        # from verification
        login_form =LoginForm(request.POST)

        if login_form.is_valid():
            user_name = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=user_name, password=password)
            if user is not None:
                # find the user and password
                login(request, user)
                # after login, return to page
                return HttpResponseRedirect(reverse("index"))

            else:
             return render(request, "login.html", {"msg": "username or password incorrect","login_form":login_form})
        #
        else:
            return render(request,"login.html",{"login_form":login_form})
