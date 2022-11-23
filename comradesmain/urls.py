from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
#from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('ecommerce_platform.urls')),
    #url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
