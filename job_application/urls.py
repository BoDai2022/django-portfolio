from django.urls import path
from . import views

urlpatterns = [
    path('<uuid:uuid>/', views.JobApplicationDetailAPIView.as_view(),name="job-application-detail"),    
    path('factors/', views.FactorListCreateAPIView.as_view(),name="factor-list"),  
    path('feedbacks/',views.FeedbackListCreateAPIView.as_view(),name="feedback-list"),
]