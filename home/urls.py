
from django.urls import path
from home.views import StudentListView,StudentDetailView


urlpatterns = [
    path('home/', StudentListView.as_view(), name='student-list'),
    path('home/<int:pk>/',StudentDetailView.as_view(),name='student-detail')
    
]
