# dappx/urls.py
from django.conf.urls import url
from django.urls import include, path
from dappx import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Names', views.UserProfileInfoViewSet)

# SET THE NAMESPACE!
app_name = 'dappx'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]