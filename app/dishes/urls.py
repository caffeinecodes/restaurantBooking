from django.conf.urls import url

from app.dishes import views

urlpatterns = [
    url(r'^dishes/$', views.dish_list),
    url(r'^categories/$', views.categories),
    url(r'^dish-quantity/$', views.dish_quantity),
]
