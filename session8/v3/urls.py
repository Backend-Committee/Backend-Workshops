from django.urls import path,include
# from rest_framework import urlpatterns
from .views import BlogListCreateView, BlogRetrieveUpdateDestroyView, BlogViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'blogs2',BlogViewSet , basename='blog-list-create')
urlpatterns=[
    path('blogs/', BlogListCreateView.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', BlogRetrieveUpdateDestroyView.as_view(), name='blog-retrieve-update-destroy'),
    path('', include(router.urls))
]