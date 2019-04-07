from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from api.serializers import SignalSerializer
from api.models import SpaceSignal
from django.utils import timezone


class Signals(generics.ListCreateAPIView):
    serializer_class = SignalSerializer

    def post(self, request, *args, **kwargs):
        serializer = SignalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        system = self.request.query_params.get('system', None)
        queryset = SpaceSignal.objects.filter(system=system, publish_date__lt=timezone.now()).order_by('-publish_date')
        return queryset

    def list(self, request, *args, **kwargs):
        system = request.query_params.get('system')

        if not system:
            return Response({'error': 'Attribute "system" is required.'}, status.HTTP_400_BAD_REQUEST)

        queryset = self.get_queryset()
        if queryset.count() == 0:
            return Response(data=[], status=status.HTTP_404_NOT_FOUND)
        serializer = SignalSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
