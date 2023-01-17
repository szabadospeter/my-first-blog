from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]