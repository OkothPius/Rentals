from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from backend.apps.accounts import views as user_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.apps.core.urls')),
    path('invoice/', include('backend.apps.invoice.urls')),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
