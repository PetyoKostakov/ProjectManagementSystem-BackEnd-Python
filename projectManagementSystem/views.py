__author__ = 'Petyo'

from django.views.generic.base import View
from django.http import HttpResponse

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello, World!")