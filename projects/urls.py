from django.url import path,include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('propertyeval.urls')),
    
]