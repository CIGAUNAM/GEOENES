from django.conf.urls import url
from . views import *

urlpatterns = [
    url(r'', SuelosIndex.as_view())
]