from django.urls import path

from measurement.views import SensorList, SensorDetail, MeasurementCreate

urlpatterns = [
    path('sensors/', SensorList.as_view(), name='sensor-list'),
    path('sensors/<int:pk>/', SensorDetail.as_view(), name='sensor-detail'),
    path('measurements/', MeasurementCreate.as_view(), name='measurement-create'),
]
