from django.urls import path

from .views import *


urlpatterns = [
    path('',AvailabilityView.as_view()),
    path('slots/',AvailableSlotView.as_view()),

]