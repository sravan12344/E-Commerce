from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.messages.views import SuccessMessageMixin


def register(request):
    if request.method == "POST":
        fullname=request.POST.get('fullname')
        username = request.POST.get("username")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                print("Username Exists.......! Try with another name")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    print("Email Already is taken, Try Another one")
                else:
                    if User.objects.filter(mobile=mobile).exists():
                        print("Email Already is taken, Try Another one")
                    else:
                        
                        user = User.objects.create_user(
                                username=username, email=email, password=password,mobile=mobile
                            )# Create a new user using the User model
                        user.save()  # send the data to the data save

                    return redirect("login")
        else:
            print("***Password did not match***")
            return redirect("register")
    else:
        return render(request, "accounts/register.html")


def login(request):
    if (
        request.method == "POST"
    ):  # if the condition is true it should enter into the if condition
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username=username, password=password) # Authenticate the user using the provided 'username' and 'password'

        if user is not None:
            auth.login(request, user)
            print("Login is Successfull")
            return redirect("show")

        else:
            print("Invalid Credentials")
            return redirect("login")
    else:
        return render(request, "accounts/login.html")

def logout(request):
    if request.method=="POST":
        auth.logout(request) # Log out the user using the auth.logout function
        print("Logout Succesfully....")
        return redirect('login')