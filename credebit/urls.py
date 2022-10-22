from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    
] + i18n_patterns(
    
    path('i18n/', include('django.conf.urls.i18n')),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    path('', index, name='index'),
    
    path('about/', about, name="about"),
    path('contacts/', contacts, name="contacts"),
    
    
    # Auth
    path('auth/', include('app_auth.urls')),
        
)

urlpatterns  +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)