# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework import generics
# from .models import Deal
# from .serializers import DealSerializer

# Create your views here.

# class DealListCreate(generics.ListCreateAPIView):
#     queryset = Deal.objects.all()
#     serializer_class = DealSerializer

# class DealRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Deal.objects.all()
#     serializer_class = DealSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Deal
from .serializers import DealSerializer

class DealList(APIView):
    def get(self, request):
        queryset = Deal.objects.all()
        serializer = DealSerializer(queryset, many=True)
        return Response({'message': 'Data successfully retrieved', 'deals': serializer.data})

    def post(self, request):
        serializer = DealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Deal created successfully')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DealDetail(APIView):
    def get_object(self, pk):
        try:
            return Deal.objects.get(pk=pk)
        except Deal.DoesNotExist:
            return Response('Deal not found')
        
    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = DealSerializer(queryset)
        return Response('Data successfully retrieved')

    def put(self, request, pk):
        queryset = self.get_object(pk)
        serializer = DealSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Deal updated successfully')
        return Response(serializer.errors)

    def delete(self, request, pk):
        queryset = self.get_object(pk)
        # queryset = Deal.objects.get(pk=pk)
        queryset.delete()
        return Response("Deleted")

