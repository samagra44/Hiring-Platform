from django.urls import path
from candidate import views

urlpatterns = [
    path("candidate-dashbordh/", views.candidate_dashbordh,name='candidate_dashbordh'),
    path('my-job-list/',views.myJobListViews,name='myJobListViews'),
    path('apply-for-job/<int:pk>/', views.applyforjob,name='applyforjob')
]