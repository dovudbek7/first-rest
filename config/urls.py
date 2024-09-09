from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.views import AuthorModelViewSet, CategoryModelViewSet, BookModelViewSet
from django.contrib import admin

router = DefaultRouter()
router.register(r'authors', AuthorModelViewSet)
router.register(r'categories', CategoryModelViewSet)
router.register(r'books', BookModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
