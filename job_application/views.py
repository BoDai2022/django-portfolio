from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .models import Factor, Feedback,JobApplication
from .serializers import FactorSerializer,FeedbackSerializer,JobApplicationSerializer
from django.db.models import Q

# Create your views here.
class FactorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Factor.objects.all()
    serializer_class = FactorSerializer

    def create(self, request, *args, **kwargs):
        """
        Check if a Factor with same name exists before creating, if not then create.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Case-insensitive check for the 'name' field
        name = serializer.validated_data['name']
        instance = Factor.objects.filter(Q(name__iexact=name)).first()
        print(instance)
        if instance:
            return Response(FactorSerializer(instance).data, status=status.HTTP_200_OK)
        else:
            # Create new object since it doesn't exist
            instance = Factor.objects.create(**serializer.validated_data)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
class FeedbackListCreateAPIView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [AllowAny] # so that the hiring manager can give feedback without authentication
    def perform_create(self, serializer):
        job_application_id = self.request.data.get('job_application')
        job_application = get_object_or_404(JobApplication, id= job_application_id)
        serializer.save(job_application=job_application)
        # return super().perform_create(serializer)

class JobApplicationDetailAPIView(generics.RetrieveAPIView):
    # queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    def get_object(self):
        uuid = self.kwargs.get('uuid')
        return get_object_or_404(JobApplication, feedback_link_uuid=uuid)    