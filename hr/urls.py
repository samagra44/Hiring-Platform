from django.urls import path
from hr import views

urlpatterns = [
    path("hrdash/", views.hrHome_views,name='hr_dash'),
    path('post-job/',views.post_job_views,name='post_job'),
    path('candidate-details/<int:pk>/', views.candidate_view, name='candidate_details'),
    path('select-cadidate/',views.selectCandidate,name='selectCandidate'),
    path('delete-cadidate/', views.deleteCandidate, name='deleteCand'),
]