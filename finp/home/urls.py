from django.urls import path

from home.views import Views

urlpatterns = [
    path('login/', Views.login, name='login')
]