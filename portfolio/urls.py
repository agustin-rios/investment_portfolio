from django.urls import path
from . import views

urlpatterns = [
    path('portfolios/<int:portfolio_id>/history/', views.portfolio_history, name='portfolio_history'),
]
