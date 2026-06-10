from django.urls import path,include
from .views import StudentListview
urlpatterns = [
    
    path('student/',StudentListview.as_view(),name='student-list'),
]
