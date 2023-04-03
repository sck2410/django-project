from django.urls import path
from myapp import views

# url ຂອງຟັງຊັ່ນທີ່ຢາກນຳມາສະແດງຜົນຢູ່ໜ້າເວັບ
urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('form', views.form)
]