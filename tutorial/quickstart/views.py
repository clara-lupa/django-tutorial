from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer, FederalStateSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from tutorial.quickstart.models import FederalState



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined') # defines the data to be shown
    serializer_class = UserSerializer # tells the computer how to (de-)serialize this model
    permission_classes = [permissions.IsAuthenticated] # defines where the authentication is tanking place?


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

@csrf_exempt # this suppresses authentification

def federal_state_list(request):
    """
    List all code federal_states, or create a new federal_state.
    """
    if request.method == 'GET':
        federal_states = FederalState.objects.all()
        serializer = FederalStateSerializer(federal_states, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FederalStateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def federal_state_detail(request, pk):
    """
    Retrieve, update or delete a federal_state.
    """
    try:
        federal_state = FederalState.objects.get(pk=pk)
    except FederalState.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FederalStateSerializer(federal_state)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FederalStateSerializer(federal_state, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        federal_state.delete()
        return HttpResponse(status=204)
