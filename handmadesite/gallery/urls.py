from django.conf.urls import url
from .views import GalleryView

urlpatterns = [
    url('^$', GalleryView.as_view(), name='gallery')
]