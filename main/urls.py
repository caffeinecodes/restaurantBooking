from django.conf.urls import include, url
from app.home.views import index, item_list
from django.contrib import admin

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', include('app.home.urls')),
    url(r'^api/', include('app.dishes.urls')),
    url(r'^api/', include('app.accounts.urls')),
]