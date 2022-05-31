from django.urls import path
from ashAPP import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.aboutme, name="about"),
    path("mywork", views.mywork, name="mywork"),
    path("myblog", views.myblog, name="myblog"),
    path("contact", views.contact, name="contact")
]