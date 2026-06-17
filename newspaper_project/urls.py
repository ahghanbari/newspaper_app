from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

#from django.views.generic.base import TemplateView


urlpatterns = [
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('', include('pages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
