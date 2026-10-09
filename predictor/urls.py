from django.urls import path
from .views import predict_burnout


urlpatterns = [
    path("", predict_burnout, name="predict_burnout"),
]