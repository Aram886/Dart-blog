from django.urls import path
from .views import *

urlpatterns = [
    path('', tree, name='tree'),
    path('rubric/<int:pk>', get_rubric, name="rubric" )
]