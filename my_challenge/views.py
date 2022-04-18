from django.shortcuts import render


def home(request):

    data = {}
    return render(request, "home.html", data)
