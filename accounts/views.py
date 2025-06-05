import django.contrib.auth as django_auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseNotAllowed
from django.shortcuts import redirect, render
from .forms import UserRegistrationForm, BlogUserLogInForm
from .ban_api import validate_address


def register(request: HttpRequest):
    match request.method:
        case "GET":
            form = UserRegistrationForm()

            return render(request, "register.jinja", {
                "form": form
            })
        case "POST":
            address = request.POST.get("address")
            address_validation = validate_address(str(address))

            if not address_validation["valid"]:
                messages.error(request, "Adresse invalide.")
                return redirect("app_home")

            form = UserRegistrationForm(request.POST)

            if form.is_valid():
                user = form.save()
                user.profile.phone = form.cleaned_data.get("phone")
                user.profile.address = address_validation["la"]
                user.profile.save()

            return redirect("app_home")
        case _:
            return HttpResponseNotAllowed(["GET", "POST"])


def login(request: HttpRequest):
    match request.method:
        case "GET":
            return render(request, "log-in.jinja", {
                "form": BlogUserLogInForm()
            })
        case "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = django_auth.authenticate(
                request,
                username=username,
                password=password
            )

            if user is None:
                messages.error(request, "Invalid credentials")
                return redirect(request.build_absolute_uri())

            django_auth.login(request, user)
            return redirect("app_home")
        case _:
            return HttpResponseNotAllowed(["GET", "POST"])


def logout(request: HttpRequest):
    django_auth.logout(request)
    messages.info(request, "You logged out.")
    return redirect("app_home")


@login_required
def profile(request: HttpRequest):
    return render(request, "profile.jinja")
