from django.urls import path
from tutorial.quickstart import views

urlpatterns = [
    path('federal_states/', views.federal_state_list),
    path('federal_states/<int:pk>/', views.federal_state_detail),
]
