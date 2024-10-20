from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser, UsersProfile
from .forms import CustomUserForm, UsersProfileForm


# Create your views here.
def signup(request):
    form = CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            UsersProfile.objects.create(user=user)
            messages.success(request, "Account created successfully!")
            return redirect("login")
    context = {"form": form}
    return render(request, "Users/signup.html", context)


def update_profile(request):
    user = request.user
    profile = UsersProfile.objects.get(user=user)
    form = UsersProfileForm(instance=profile)
    if request.method == "POST":
        form = UsersProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("profile")
    context = {"form": form}
    return render(request, "Users/update_profile.html", context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    next_url = request.GET.get("next")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            if next_url:
                return redirect(next_url)
            return redirect("home")
        else:
            messages.error(request, "Invalid email or password")

    context = {"next": next_url}
    return render(request, "Users/login.html", context)


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("login")
    return redirect("login")
