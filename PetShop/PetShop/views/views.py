# -*- coding: utf-8 -*-
__author__ = 'daniel.anselmo'

import os
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

def show_homepage(request):
    return render(request, 'base.html')

def show(request):
    #BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #return HttpResponse(os.path.join(BASE_DIR, "templates").replace('\\', '/'))
    BASE_DIR = os.path.join(os.path.dirname(__file__), 'static', )
    return HttpResponse(BASE_DIR)

def homepage(request):
    return render(request, 'home.html')