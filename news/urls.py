from django.urls import path
from . import views


urlpatterns = [
    path('', views.NewsListAPIView.as_view(), name="news"),
    path('<int:id>', views.NewsDetailAPIView.as_view(), name="newse"),
]
