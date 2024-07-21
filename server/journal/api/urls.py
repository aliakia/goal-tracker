from rest_framework.routers import DefaultRouter
from .views import JournalViewSet

journal_router = DefaultRouter()
journal_router.register(r'journal', JournalViewSet)