from django.urls import path, include
from . import views
app_name = '[DataCollection]'
urlpatterns = [
    path('^HomePage/', views.HomePage),
]
