from django.conf.urls import include, url
from app.home.views import index
from django.contrib import admin

urlpatterns = [
    url(r'^$', index),
    url(r'^api/', include('app.dishes.urls')),
    url(r'^api/', include('app.accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
]