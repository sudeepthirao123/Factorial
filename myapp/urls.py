from django.urls import path
from . import view

urlpatterns = [
    path('', view.number_view, name='number-view'),
]
