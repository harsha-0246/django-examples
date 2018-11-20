from django.urls import path
from . import views

"""
Assign a view called post_list to the root URL
Pattern match the empty URL which replace the local host
Name of the URL used to identify the view
"""
"""
post/ means that the URL should begin with the word post followed by a /. So far so good.
<int:pk> – this part is trickier. It means that Django expects an integer 
    value and will transfer it to a view as a variable called pk.
/ – then we need a / again before finishing the URL.

"""

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]