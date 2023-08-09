from rest_framework import generics
from rest_framework import permissions
from .serializers import ContactSerializer
from .models import Contact

class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAdminUser]