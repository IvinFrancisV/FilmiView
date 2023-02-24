from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Film_viewing_app.models import SubscriptionPlan, CustomUser, Administrator
from Film_viewing_app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import get_user_model, authenticate, login, logout
User = get_user_model()


def REGISTER(request):
    subscription_plan = SubscriptionPlan.objects.all()
    context = {
        'subscription_plan': subscription_plan,
    }

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.warning(request, "An account with this E-Mail has already been registered. Please try Logging In")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.warning(request, "This username is already taken! Please try another one.")
            return redirect('register')

        user = User(
            username = username,
            email = email,
            user_type = 2,
        )
        user.set_password(password)
        user.save()
        return redirect('View_subscription_plans_user')
    return render(request, "registration/registration.html", context)


def ADMIN_REGISTRATION(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "An account with this E-Mail has already been registered. Please try Logging In")
            return redirect('register')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "This username is already taken! Please try another one.")
            return redirect('register')

        user = CustomUser(
            username = username,
            email = email,
            user_type = 1,
            is_admin = True,
        )
        user.set_password(password)
        user.save()

    return render(request, "registration/Admin_registration.html")



def DO_LOGIN(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'))
        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type != "2":
                return redirect('Administrator_home')
            else:
                return redirect('User_home')
        else:
            return redirect('login')

    else:
        return HttpResponse("Method not allowed")


def PROFILE(request):
    return render(request, "registration/profile.html")


def LOGOUT(request):
    logout(request)
    return redirect('Home_page')


def PROFILE_UPDATE(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id

        user = User.objects.get(id = user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        user.save()
        messages.success(request, "Profile Updated Successfully")
        return redirect('profile')
