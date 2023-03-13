from django.urls import path

from accountapp.views import hello_world

app_name = "accountapp" #appname을 명시하여 경로를 편리하게 설정할 수 있다.

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]