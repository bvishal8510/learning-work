from django.conf.urls import url, include
from django.contrib.auth import views as built_views
# from django.contrib import admin
from learn import views
from learn.views import home,newsfeed,comment
from django.contrib.auth.views import password_reset
# from django.conf import settings
# from django.conf.urls.static import static
# from django_filters.views import FilterView
urlpatterns = [

    # url(r'^$', views.home, name='profile'),
    url(r'^$', newsfeed.as_view(), name='newsfeed'),

    url(r'^profile/(?P<username>\w+)/$', home.as_view(), name='profile'),

    url(r'^upload/(?P<username>\w+)/$', views.model_form_upload, name='model_form_upload'),

    url(r'^login/$', views.check_login, name='login'),

    # if user will logout it will render to login page
    url(r'^logout/$', built_views.logout, {'next_page': 'newsfeed'}, name='logout'),

    url(r'^information/(?P<username>\w+)/$', views.user_info, name="user_info"),


    url(r'^signup/$', views.signup, name='signup'),

    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate,
        name='activate'),

    # url(r'^frontpage/$', views.front_page, name='front_page'),

    url(r'^passwordreset/$', password_reset,
        {'template_name': 'forget/password_reset_form.html'},
        name='password_reset'),

    url(r'^passwordreset/done/$', built_views.password_reset_done,
        {'template_name': 'forget/password_reset_done.html'},
        name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        built_views.password_reset_confirm,
        {'template_name': 'forget/password_reset_confirm.html',
         'post_reset_redirect': 'login'},
        name='password_reset_confirm'),

    url(r'^profile/(?P<username>\w+)/edit/(?P<pk>\d+)$', views.doc_update, name='Doc_edit'),

    # url(r'^profile/(?P<username>\w+)/delete/(?P<pk>\d+)$', views.doc_delete, name='Doc_delete'),
    url(r'^delete/$', views.doc_delete, name='Doc_delete'),

    url(r'comment/$', comment.as_view(), name='comment'),

    url(r'^like/$', views.like, name='like'),
    url(r'^user_list/$', views.list_of_user, name='user_list'),
    url(r'^validate_username/$', views.validate_username, name='validate_username'),
    url(r'^validate_email/$', views.validate_emailid, name='validate_email'),
    url(r'^edit_image/rotate/$', views.rotate_image, name='rotate_image'),
    url(r'^edit_image/blur/$', views.blur_image, name='blur_image'),
    url(r'^edit_image/flip/$', views.flip_image, name='flip_image'),
    url(r'^edit_image/height/$', views.height_image, name='height_image'),
    url(r'^edit_image/width/$', views.width_image, name='width_image'),
    url(r'^edit_image/effect/$', views.effect_image, name='effect_image'),
    url(r'^search/$', views.search, name='search'),

   ]
