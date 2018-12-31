from django.conf.urls import url, include
from django.contrib import admin
from learn import views
from learn.views import front_page
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
from django_private_chat import urls as django_private_chat_urls
# from rest_framework import routers, serializers, viewsets

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'is_staff')
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    # this url is for admin page "/admin/"
    url(r'^admin/', admin.site.urls),
    # this is for user loggin in page "/"
    url(r'^$', front_page.as_view(), name='front_page'),
    # url(r'^', include(router.urls)),
    url(r'^phoics/', include('learn.urls')),
    url(r'^', include('django_private_chat.urls')),
    # url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^conversation/', include('conversation.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.error404
handler400 = views.error400
handler500 = views.error500
handler403 = views.error403
