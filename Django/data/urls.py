from django.conf.urls import url
from django.urls import path, include

from data import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'customers', views.CustViewSet)

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^links/$', views.LinksPageView.as_view()),
    url(r'^getcust/$',views.Customers.getCust),
    url(r'^apitest/$',views.CalcTest),
]