from rest_framework import serializers
from .models import Factor,Feedback,JobApplication


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = "__all__"
class FactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factor
        fields = [
            'id',
            'name',
            'description'
        ]

class FeedbackSerializer(serializers.ModelSerializer):
    # factors = FactorSerializer(many=True, read_only=True)  # Nested serializer for factors
    # job_application = JobApplicationSerializer(read_only = True)
    class Meta:
        model = Feedback
        fields = [
            'job_application',
            'date',
            'detailed_feedback',
            'factors',
        ]