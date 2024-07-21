from rest_framework.routers import DefaultRouter
from .views import JogsViewSet

jog_router = DefaultRouter()
jog_router.register(r'jog', JogsViewSet)