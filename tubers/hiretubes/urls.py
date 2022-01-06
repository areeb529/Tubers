from django.urls import path


from . import views

urlpatterns = [
    path('hiretube', views.hiretube, name="hiretube"),

]