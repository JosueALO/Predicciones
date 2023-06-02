from django.contrib import admin
from django.urls import path
from predicciones_app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]
