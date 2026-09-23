from django.urls import path
from .views import ChallengeListCreateView, ChallengeDetailView

urlpatterns=[
    path('challenges/',ChallengeListCreateView.as_view(),name='challenge-list-create'),
    path('challenges/<int:pk>/',ChallengeDetailView.as_view(),name='challenge-detail'), # pk expected variable to hold the integer, can be changed to anything , just add lookup field = "variable you chose"
]