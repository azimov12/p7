from django.urls import path
from .views import summer, winter, spring, autumn

urlpatterns = [
    path('summer/', summer),
    path('winter/', winter),
    path('spring/', spring),
    path('autumn/', autumn),
]