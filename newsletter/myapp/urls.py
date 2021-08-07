from django.urls import include, path
from rest_framework import routers
from django.conf.urls import url
from . import views

router = routers.DefaultRouter()
# router.register(r'', views.SubscriptionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'subscribe', views.subscriptions_list),
    url(r'subscriptions', views.subscriptions_list)
]