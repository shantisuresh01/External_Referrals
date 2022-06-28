'''
Created on May 26, 2019

@author: shanti
'''
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
import datetime
import time

class LandingView(TemplateView):
    template_name = 'registration/welcome.html'
    page_name = "WelcomePage"
    
class AboutTheProgramView(TemplateView):
    template_name = 'registration/about.html'
    page_name = 'AboutOurProgram'

class BravoView(TemplateView):
    template_name = 'registration/bravo.html'
    page_name = "WelcomePage"

def whereto(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('welcome')

    if user.is_active and user.is_authenticated:
        return redirect('bravo_page')

def first_login(user):
    now = datetime.datetime.now()
#    if time.strptime(user.date_joined,'%Y-%m-%d  %X.%f') <