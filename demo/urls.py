from django.urls import path, include
from . import views
#from .views import Another
from rest_framework import routers
from .views import BookViewSet


router = routers.DefaultRouter()
router.register('books',BookViewSet)


urlpatterns = [
    #path('first', views.first),
    # path('another', Another.as_view()),
    path('',include(router.urls))
]
