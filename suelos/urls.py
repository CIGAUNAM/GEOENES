from django.conf.urls import url
from . views import *

urlpatterns = [
    url(r'styles/polygon.sld$', PolygonSLD.as_view()),
    url(r'styles/images/(?P<pk>[\w\-]+)$', StyleImage.as_view()),
    url(r'', SuelosIndex.as_view())
]