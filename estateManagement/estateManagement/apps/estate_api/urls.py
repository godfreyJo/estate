from django.urls import path, include
from estate_api import views

urlpatterns = [

    # path('', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.HouseListCreateView.as_view(), name='house-list-create'),
    path('houses/<int:pk>/', views.HouseRetrieveUpdateDestroyView.as_view(), name='house-retrieve-update-destroy'),
    path('salesPersons/', views.SalesPersonListCreateView.as_view(), name='salesPersons-list-create'),
    path('salesPersons/<int:pk>/', views.SalesPersonRetrieveUpdateDestroyView.as_view(), name='salesPersons-retrieve-update-destroy'),
    path('contacts/', views.ContactListCreateView.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', views.ContactRetrieveUpdateDestroyView.as_view(), name='contact-retrieve-update-destroy'),
]
