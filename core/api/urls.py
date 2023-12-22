from django.urls import path

from . import views

urlpatterns = [
    path('links/', views.LinkItemList.as_view()),
    path('photos/', views.SleepingModePhotoList.as_view())
]

