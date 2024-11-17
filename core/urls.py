# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include  # add this
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls")), 


]

urlpatterns += staticfiles_urlpatterns()
