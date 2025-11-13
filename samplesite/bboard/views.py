from django.http import HttpResponse

# from django.shortcuts import render
from .models import Bb

# Create your views here.

def index(request):
    s = "Объявления\r\n\r\n\r\n"

    for bb in Bb.objects.order_by('-published'):
        s += f"{bb.title}\r\n{bb.content}\r\n\r\n"

    return HttpResponse(s, content_type="text/plain; charset=utf-8")


