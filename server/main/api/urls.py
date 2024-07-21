from rest_framework.routers import DefaultRouter
from django.urls import path, include
from goals.api.urls import person_router
from jogs.api.urls import jog_router
from journal.api.urls import journal_router

router = DefaultRouter()

# app 1
# app 2
# goals

router.registry.extend(journal_router.registry)
router.registry.extend(jog_router.registry)
router.registry.extend(person_router.registry)
urlpatterns = [
    path('', include(router.urls)),
]


# jogs

