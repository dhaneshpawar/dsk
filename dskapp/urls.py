from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.about),
    path('login',views.login),
    path('logs',views.logs),
    path('dellogs',views.dellogs),
]

handler404 = views.error_404_view
urlpatterns += staticfiles_urlpatterns()
