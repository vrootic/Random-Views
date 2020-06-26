from django.shortcuts import redirect


def index(request):
    response = redirect('https://www.instagram.com/meetjuthere')
    return response
