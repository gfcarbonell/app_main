# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from web_sites.views import WebSiteModelViewSet
from web_headers.views import WebHeaderModelViewSet
from web_sections.views import WebSectionModelViewSet
from web_slides.views import WebSlideModelViewSet
from web_sliders.views import WebSliderModelViewSet
router = routers.DefaultRouter()

router.register(r'web-sites', WebSiteModelViewSet)
router.register(r'web-headers', WebHeaderModelViewSet)
router.register(r'web-sections', WebSectionModelViewSet)
router.register(r'web-slides', WebSlideModelViewSet)
router.register(r'web-sliders', WebSliderModelViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',                           include('index.urls', namespace='index')),
    #Auth Social
    url(r'^',                           include('social.apps.django_app.urls', namespace='social')),
    #A.P.I - R.E.S.T.
    url(r'^api/', 						include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

