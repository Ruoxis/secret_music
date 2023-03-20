import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


# Create your views here.

def message(request):
    return HttpResponse("AAAAAA")


class Templates(View):
    def get(self, request):
        return HttpResponse('Holle django')
