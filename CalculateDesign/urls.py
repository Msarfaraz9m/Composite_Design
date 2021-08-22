from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('modulus_of_elasticity', modulus_of_elasticity),
    path('critical_fiber_length', critical_fiber_length),
    path('stress', stress),
    path('elasticity', elasticity),
]
