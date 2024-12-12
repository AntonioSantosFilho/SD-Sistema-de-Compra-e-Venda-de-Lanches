from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('marketplace/', include('marketplace.urls')),  
    path('', include('registro.urls')),
    path('pagamentos/', include('pagamentos.urls')),
]
