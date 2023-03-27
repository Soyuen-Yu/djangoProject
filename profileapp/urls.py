from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = "profileapp" #appname을 명시하여 경로를 편리하게 설정할 수 있다.


urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
    path('update/', ProfileUpdateView.as_view(), name='update'),
]