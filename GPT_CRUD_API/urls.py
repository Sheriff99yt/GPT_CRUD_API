# GPT_CRUD_API/urls.py
from django.contrib import admin
from django.urls import path, include
from filehandler.views import home

urlpatterns = [
    path('', home, name='home'),  # Add the home view here
    path('admin/', admin.site.urls),
    path('api/', include('filehandler.urls')),
]
