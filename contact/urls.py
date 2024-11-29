from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static
# import state

app_name='contact'

urlpatterns = [
    path('', views.ContactView.as_view(), name = 'contact_choco'),

# ]+ state(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )