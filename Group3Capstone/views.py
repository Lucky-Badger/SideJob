from django.shortcuts import render, redirect
from django.views import View
from .models import User #create and add user models
from .classes.administrator import Admin
# Create your views here.

class Home(View):
    def get(self, request):
        request.session.pop("username", None)
        return render(request, "home.html", {})
    def post(self, request):
        noSuchUser = False
        badPassword = False
        try:
            m = User.objects.get(username=request.POST['username'])
            badPassword = (m.User_Password != request.POST['password'])
        except:
            noSuchUser = True
        if noSuchUser:
            return render(request, "home.html", {"message":"user does not exist"})
        elif badPassword:
            return render(request, "home.html", {"message":"bad password"})
        else:
            request.session["username"] = m.username
            return redirect("/dashboard/")

class Dashboard(View):
    def get(self, request):
        if not request.session.get("username"):
            return redirect("/")
        u = User.objects.get(username=request.session['username'])
        return render(request, "dashboard.html", {"username": u.username})

class Account(View):
    def get(self, request):
     if not request.session.get("username"):
       return redirect("/")
     u = User.objects.get(username=request.session['username'])
     return render(request, "account.html",
                   {"User_ID": u.User_ID, "User_Password": u.User_Password, "User_FName": u.User_FName,
                    "User_LName": u.User_LName,
                    "User_DOB": u.User_DOB, "User_Address": u.User_Address, "User_Phone": u.User_Phone,
                    "UserName": u.UserName, "User_Email": u.User_Email, "Account_type": u.Account_type})

    def post(self, request):
        u = User.objects.get(username=request.session["username"])
        return render(request, "account.html",
                      {"User_ID": u.User_ID, "User_Password": u.User_Password, "User_FName": u.User_FName,
                       "User_LName": u.User_LName,
                       "User_DOB": u.User_DOB, "User_Address": u.User_Address, "User_Phone": u.User_Phone,
                       "UserName": u.UserName, "User_Email": u.User_Email, "Account_type": u.Account_type})