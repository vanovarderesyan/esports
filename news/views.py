from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import NewsSerializer
from .models import News
from rest_framework import permissions
from .permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend


class NewsListAPIView(ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'formats', 'events']
    # permission_classes = (IsOwner,)

    # def perform_create(self, serializer):
    #     return serializer.save(owner=self.request.user)
    #
    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)


class NewsDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = NewsSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = News.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
