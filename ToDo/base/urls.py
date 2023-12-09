from django.urls import path
from base.views import *

urlpatterns = [
    path('home/',home,name='home'),
    path('create/',create,name='create'),
    path('edit/<int:pk>',edit,name='edit'),# pk vaneko chai paramater pass gareko yesma garesi views ma pni paramater pass garnu parxa
    
]