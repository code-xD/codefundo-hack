from rest_framework import serializers
from .models import VoterDetail


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoterDetail
        fields = ['voter_name', 'gender', 'age', 'd_code', 'c_code',
                  's_code', 'pin', 'aLine1', 'aLine2', 'aadhar_no']
