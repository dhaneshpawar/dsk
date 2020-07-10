from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dskapp.urls')),
    # path('url', views.thisr),
    # # path('scrap', views.scrap),
    # path('login',views.login),
    # path('fileput',views.fileput),
    # path('form',views.form)
]

urlpatterns += staticfiles_urlpatterns()
handler404 = views.error_404_view