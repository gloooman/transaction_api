from rest_framework.routers import DefaultRouter
from .viewsets import TransactionViewSet


router = DefaultRouter()
router.register('transaction', TransactionViewSet)


urlpatterns = []

urlpatterns += router.urls
