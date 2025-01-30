from django.urls import path
from .views import loan_calculator

urlpatterns = [
    path("calculate-loan/", loan_calculator, name="loan-calculator"),
]
