from django.urls import path
from .views import index, personas,detallepersona, crearpersona

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name='index'),
    path('personas/',personas, name='personas'),
    path('detallepersona/<id>',detallepersona,name='detallepersona'),
    path('crearpersona/',crearpersona,name='crearpersona')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)