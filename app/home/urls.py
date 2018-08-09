from django.conf.urls import patterns, url

from app.home import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^item-list/$', views.item_list, name='item_list'),
    url(r'^add-menu/$', views.add_menu, name='add_menu'),
    url(r'^edit-menu/$', views.edit_menu, name='edit_menu'),
    url(r'^item-details/$', views.item_details, name='item_details'),

    # url(r'abc/$', views.faq, name='index'),
    # url(r'about/$', views.about, name='index'),
    # url(r'terms_and_conditions/$', views.terms_and_conditions, name='index'),
)