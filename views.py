from __future__ import division
from __future__ import unicode_literals

import requests

from django.shortcuts import redirect
from django.shortcuts import render

def show_equation_list(request):
    
    r = requests.get('http://django-apps-dulrich15.c9.io/eqns/api/equations/')
    json = r.json()

    context = { 'json': json }
    template = 'show_equation_list.html'
    return render(request, template, context)
