from rest_framework import serializers
from registry.models import Report,Profile

        

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id','report_name','description','image','author')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','username','bio','contact','avatar')