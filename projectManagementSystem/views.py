from rest_framework.authentication import BasicAuthentication
from projectManagementSystem.settings import SessionCsrfExemptAuthentication

__author__ = 'Petyo'
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.views.generic.base import View
from django.http import HttpResponse
from .models import Task
from .serializers import TaskSerializer

authentication_classes = (SessionCsrfExemptAuthentication, BasicAuthentication)

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello, World!")


class TaskMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskList(TaskMixin, ListCreateAPIView):
    """
    Return a list of all the tasks, or
    create new ones
    """
    pass


class TaskDetail(TaskMixin, RetrieveUpdateDestroyAPIView):
    """
    Return a specific task, update it, or delete it.
    """
    pass