from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from products import views

urlpatterns = [
    path('', views.home_view, name='home_view'),  # Display dashboard when running the project
    path('products/', views.customer_view, name='customer_view'),  
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('admin/', views.product_dashboard, name='product_dashboard'),
    path('product/new/', views.product_create, name='product_create'),
    path('product/<int:pk>/edit/', views.product_update, name='product_update'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('category/<str:category>/', views.category_view, name='category_view'),
]

# Add this to serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
