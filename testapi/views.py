from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .serializers import NewPersonHeroSerializer
from .models import NewPerson


def main(request):
    return HttpResponse("It's work")


class NewPersonViewsets(viewsets.ModelViewSet):
    queryset = NewPerson.objects.all().order_by('first_name')
    serializer_class = NewPersonHeroSerializer
    lookup_field = 'first_name'
