from random import sample
from django.shortcuts import render
from .serializers import AnimalFactSerializer
from .models import AnimalFact
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from random import *

# Create your views here.
class ListAnimalFact(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = AnimalFact.objects.all()

    serializer_class = AnimalFactSerializer

class ListAnimalFactDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = AnimalFact.objects.all()

    serializer_class = AnimalFactSerializer

# function based views
@api_view(['GET'])
def list_animal_fact(request, format=None):

    if request.method == 'GET':

        facts = AnimalFact.objects.all()

        serializer = AnimalFactSerializer(facts, many=True)

        return Response(serializer.data)

@api_view(['GET'])
def list_animal_fact_detail(request, pk, format=None):

    try:

        fact = AnimalFact.objects.get(id=pk)

    except AnimalFact.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = AnimalFactSerializer(fact)

        return Response(serializer.data)

@api_view(['GET'])
def search_animal(request, format=None):

    if request.method == 'GET':

        query = request.GET.get('q')

        try:

            fact = AnimalFact.objects.get(
                Q(animal__icontains=query) | 
                Q(setup__icontains=query) | 
                Q(delivery__icontains=query)
            )

        except AnimalFact.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AnimalFactSerializer(fact)

        return Response(serializer.data)

@api_view(['GET'])
def random_fact(request, format=None):

    if request.method == 'GET':

        all_fact_count = len(AnimalFact.objects.all())

        random_id = randint(1,all_fact_count)

        try:

            fact = AnimalFact.objects.get(id=random_id)

        except AnimalFact.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AnimalFactSerializer(fact)

        return Response(serializer.data)