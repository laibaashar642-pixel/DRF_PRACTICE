
from django.urls import path
from home.views import StudentListView

urlpatterns = [
    path('home/', StudentListView.as_view(), name='student-list'),
]
