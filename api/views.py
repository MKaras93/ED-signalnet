from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from api.serializers import SignalSerializer


class Signals(generics.ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = SignalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)