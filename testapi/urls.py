from django.urls import path, include

from .serializers import NewPersonHeroSerializer
from .views import NewPersonViewsets, UsersView, FindUserOne, UserApiViewList, UserUpdateList, GetUserOne, \
     RegisterView, FindUser, AllUsersViewSet, ContactsUsersView
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('person', NewPersonViewsets, basename='person')
router.register('p', AllUsersViewSet, basename='p')
router.register('contact', ContactsUsersView, basename='contact')

urlpatterns = [
                  path("", include(router.urls)),
                  path('', views.main, name='main'),
                  path('auth/', include('djoser.urls')),
                  path('auth/', include('djoser.urls.jwt')),
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
                  path('register/', RegisterView.as_view()),
                  path('all/', UsersView.as_view()),
                  path('all/<int:pk>/', UsersView.as_view()),
                  path('finduser/<int:pk>/', FindUserOne.as_view()),
                  path('finduser/', FindUser.as_view()),
                  path('getpostlist/', UserApiViewList.as_view()),
                  path('getpostlist/<int:pk>/', UserUpdateList.as_view()),
                  path('ge/<int:pk>/', GetUserOne.as_view()),
                  path("ckeditor/", include('ckeditor_uploader.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
