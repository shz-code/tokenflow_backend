from django.shortcuts import render
from django.http import HttpResponse

# Handle server errors


def handle_page_not_found(request, exception):
    msg = "404 - Requested page not found."
    return render(request, "error.html", {
        "msg":  msg
    })


def handle_server_error(request):
    msg = "500 - Internal Server Error."
    return render(request, "error.html", {
        "msg": msg
    })


def handle_bad_request(request, exception):
    msg = "400 - Bad Request."
    return render(request, "error.html", {
        "msg": msg
    })


def index(request):
    return render(request, "index.html")
