from django.urls import path
from . import views

"""
Assign a view called post_list to the root URL
Pattern match the empty URL which replace the local host
Name of the URL used to identify the view
"""


urlpatterns = [
    path('', views.post_list, name='post_list'),
]