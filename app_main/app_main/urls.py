# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from auth_users.views import AuthUserModelViewSet
from identification_documents.views import IdentificationDocumentsModelViewSet
from civil_states.views import CivilStateModelViewSet
from blood_groups.views import BloodGroupModelViewSet


router = routers.DefaultRouter()

router.register(r'auth-users', AuthUserModelViewSet)
router.register(r'identification-documents', IdentificationDocumentsModelViewSet)
router.register(r'civil-states', CivilStateModelViewSet)
router.register(r'blood_groups', BloodGroupModelViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',                           include('index.urls', namespace='index')),
    #Auth Social
    url(r'^',                           include('social.apps.django_app.urls', namespace='social')),
    #A.P.I - R.E.S.T.
    url(r'^api/', 						include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

