from api_ttc.viewsets import CatergoriesViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categories', CatergoriesViewset)