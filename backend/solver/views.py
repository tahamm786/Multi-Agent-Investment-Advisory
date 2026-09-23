from django.shortcuts import render
from rest_framework import generics
from .models import Challenge,SolveSession
from .serializer import ChallengeSerializer,SolveSessionSerializer


class ChallengeListCreateView(generics.ListCreateAPIView): # TO HANDLE VIEWING AND ADDING CHALLENGES - BASICALLY GET AND POST
    queryset= Challenge.objects.all()
    serializer_class= ChallengeSerializer

class ChallengeDetailView(generics.RetrieveUpdateDestroyAPIView): # TO HANDLE PARTICULAR CHALLENGES
    queryset= Challenge.objects.all()
    serializer_class= ChallengeSerializer




