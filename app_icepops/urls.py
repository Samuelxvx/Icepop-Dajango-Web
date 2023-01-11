from django.urls import path
from . import views

urlpatterns = [
    path('', views.icepops, name='icepops'),
    path('<int:icepop_id>', views.icepop, name='icepop')
]

