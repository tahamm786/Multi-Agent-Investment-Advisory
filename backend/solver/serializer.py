from rest_framework import serializers
from .models import Challenge,SolveSession

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Challenge
        fields=['id','name','challenge_type','target_url','description','created_at']


class SolveSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model=SolveSession
        fields=['id','challenge','status','created_at']



