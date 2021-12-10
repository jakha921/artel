from django.db import router
from django.urls import path, include
from .views import *
from rest_framework.routers import \
        DefaultRouter, SimpleRouter


# drf_yasg 
"""
https://drf-yasg.readthedocs.io/en/stable/readme.html
"""
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



# drf 
schema_view = get_schema_view(
openapi.Info(
    title="Artel APIs",
    default_version='v1',
    description="",
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="contact@snippets.local"),
    license=openapi.License(name="BSD License"),
),
public=True,
permission_classes=(permissions.AllowAny,),
)


# Simple JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)


# urls for API   
"""
URL pattern: ^users/$ Name: 'user-list'
URL pattern: ^users/{pk}/$ Name: 'user-detail'
https://www.django-rest-framework.org/api-guide/routers/
"""
router = DefaultRouter()
router.register('languagesAPI', languageAPIView, basename="languagesAPI")
router.register('categoriesAPI', categorieAPIView, basename="categoriesAPI")
router.register('goodsAPI', goodAPIView, basename="goodsAPI")
router.register('goodImageAPI', goodImageAPIView, basename="goodImageAPI")
router.register('companiesAPI', companiesAPIView, basename="companiesAPI")
router.register('infoAPI', infoAPIView, basename="infoAPI")
router.register('partnersAPI', partnersAPIView, basename="partnersAPI")
router.register('exportsAPI', exportsAPIView, basename="exportsAPI")
router.register('ecologyAPI', ecologiesAPIView, basename="ecologyAPI")
router.register('innovationsAPI', innovationsAPIView, basename="innovationsAPI")
router.register('feedbacksAPI', feedbacksAPIView, basename="feedbacksAPI")
router.register('product_basesAPI', productBasesAPIView, basename="product_basesAPI")
router.register('servicesAPI', servicesAPIView, basename="servicesAPI")
router.register('reportsLanguageAPI', reportOfLanguageAPIView, basename="reportsOfLanguageAPI")
router.register('reportsCategoryAPI', reportOfCategoryAPIView, basename="reportsOfCategoryAPI")
router.register('reportsOfGoodAPI', reportOfGoodAPIView, basename="reportsOfGoodAPI")
router.register('stocksAPI', stocksAPIView, basename="stocksAPI")
router.register('usersAPI', userAPIView, basename="usersAPI")


urlpatterns = [
        # APIs urls
    path('api/', include(router.urls)),
        # drf
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
        # JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        # view
    path('', index, name='index'),
    path('report/', report, name='report'),
    path('category/', category, name='category'),
    path('category/update/<int:pk>/', updateCategorie, name='updateCategory'),
    path('category/delete/<int:pk>/', deleteCategorie, name='deleteCategory'),
    path('good/', good, name='good'),
    path('good/update/<int:pk>/', updateGoods, name='updateGood'),
    path('good/delete/<int:pk>/', deleteGoods, name='deleteGood'),
    path('feedbacks/', feedbacks, name='feedbacks'),
    path('stock/', stock, name='stock'),
    path('stock/update/<int:pk>/', updateStocks, name='updateStocks'),
    path('stock/delete/<int:pk>/', deleteStocks, name='deleteStocks'),
]