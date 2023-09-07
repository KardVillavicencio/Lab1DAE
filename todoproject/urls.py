from django.urls import path
from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('/app/sumar/18/19/'), name='root_redirect'),
    path('app/', include('calculator.urls')),
]
