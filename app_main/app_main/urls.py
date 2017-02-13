# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from auth_users.views import AuthUserModelViewSet
from identification_documents.views import IdentificationDocumentModelViewSet
from civil_states.views import CivilStateModelViewSet
from blood_groups.views import BloodGroupModelViewSet
from countries.views import CountryModelViewSet
from departments.views import DepartmentModelViewSet
from provinces.views import ProvinceModelViewSet
from districts.views import DistrictModelViewSet

router = routers.DefaultRouter()

#Assist Control
router.register(r'auth-users', AuthUserModelViewSet)
router.register(r'identification-documents', IdentificationDocumentModelViewSet)
router.register(r'civil-states', CivilStateModelViewSet)
router.register(r'blood-groups', BloodGroupModelViewSet)
router.register(r'countries', CountryModelViewSet)
router.register(r'departments', DepartmentModelViewSet)
router.register(r'provinces', ProvinceModelViewSet)
router.register(r'districts', DistrictModelViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',                           include('index.urls', namespace='index')),
    #Auth Social
    url(r'^',                           include('social.apps.django_app.urls', namespace='social')),
    #A.P.I - R.E.S.T.
    url(r'^api/', 						include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

