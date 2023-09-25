from django.shortcuts import render
from Invoiceapp.models import Invoice, InvoiceDetail
from Invoiceapp.serializers import InvoiceSerializer, InvoiceDetailSerializer
from  rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

#Create your views here.

class InvoiceListCreate(ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class=InvoiceSerializer

class InvoiceDetailListCreate(ListCreateAPIView):
    queryset=InvoiceDetail.objects.all()
    serializer_class=InvoiceDetailSerializer

class InvoiceRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class=InvoiceSerializer
    lookup_field='id'

class InvoiceDetailRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=InvoiceDetail.objects.all()
    serializer_class=InvoiceDetailSerializer
    lookup_field='id'
