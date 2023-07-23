"""cars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from engineering import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = routers.DefaultRouter()
# router.register(r'customer', views.UserViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'last_five', views.LastFive)
router.register(r'sale', views.Sale)
router.register(r'tour', views.TourViewSet)
router.register(r'review', views.ReviewViewSet)
router.register(r'book', views.BookingViewSet)
router.register(r'clicks', views.ClicksView)
router.register(r'country', views.CountryViewSet)
router.register(r'categoryHot', views.CategoryHotelViewSet)
router.register(r'hotel', views.HotelViewSet)
router.register(r'attrac', views.AttractionViewSet)
router.register(r'diy', views.DiyViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('drf_auth', include('rest_framework.urls')),
    path('api/auth', include('djoser.urls')),
    re_path(r'^auth', include('djoser.urls.authtoken')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('users/', views.UserListView.as_view(), name='user-list'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

