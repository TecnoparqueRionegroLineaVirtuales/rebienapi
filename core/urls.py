from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="APIREST (PROYECTO TIPO) - TECNOPARQUE RIONEGRO",
        default_version='v1',
        description="Proyecto para la gestión de portales turísticos y contenidos",
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ingejeisson@gmail.com"),
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('druna/', admin.site.urls),
    path('api/', include('app.api.routers')),
    path('api/documentation/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
