from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/<int:letting_id>/', views.letting, name='letting'),
    path('sentry-debug/', views.trigger_error)
]
