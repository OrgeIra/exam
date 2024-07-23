from django.urls import path
from .views import index, cart, checkout, contact, shop, shop_detail, testimonial, error_404

urlpatterns = [
    path('', index, name='index'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('contact/', contact, name='contact'),
    path('shop/', shop, name='shop'),
    path('shop-detail/', shop_detail, name='shop_detail'),
    path('testimonial/', testimonial, name='testimonial'),
]

handler404 = 'app.views.error_404'
