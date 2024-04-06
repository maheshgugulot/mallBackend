# urls.py

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from . import views
from .views import login_view, logout_view
from .views import signup
from billingsystem.views import ProductListCreateView, ProductRetrieveUpdateDestroyView, \
                                 CustomerListCreateView, CustomerRetrieveUpdateDestroyView, \
                                 EmployeeListCreateView, EmployeeRetrieveUpdateDestroyView, \
                                 SaleListCreateView, AnalyticsAPIView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('signuppage/', login_view, name='signuppage'),
    path('logout/', logout_view, name='logout'),

    path('api/token/', obtain_auth_token, name='token_obtain_pair'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    path('api/products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),

    path('api/customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('api/customers/<int:pk>/', CustomerRetrieveUpdateDestroyView.as_view(), name='customer-detail'),

    path('api/employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('api/employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-detail'),

    path('api/sales/', SaleListCreateView.as_view(), name='sale-list-create'),
    path('api/analytics/', AnalyticsAPIView.as_view(), name='analytics'),
]
