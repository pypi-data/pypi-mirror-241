from django.urls import path

from . import views

app_name = "drifters"

urlpatterns = [
    path("", views.index, name="index"),
    path("motd", views.motd, name="motd"),
    path("scout", views.scout, name="scout"),
    path("scout/region/<int:region_id>/", views.scout_region, name="scout_region"),
    path("scout/complex/<str:complex>/", views.scout_complex, name="scout_complex"),
]
