from rest_framework import generics
from .models import House, SalesPerson, Contact
from .serializers import HouseSerializer, SalesPersonSerializer, ContactSerializer


# Create your views here.

class HouseListCreateView(generics.ListCreateAPIView):
    queryset = House.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return HouseSerializer
        else:
            return HouseSerializer

class  HouseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.all()
    serializers_class = HouseSerializer

class SalesPersonListCreateView(generics.ListCreateAPIView):
    queryset = SalesPerson.objects.all()
    serializer_class = SalesPersonSerializer

class SalesPersonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesPerson.objects.all()
    serializer_class = SalesPersonSerializer

class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer