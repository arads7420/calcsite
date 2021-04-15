from django.urls import path
from . import views


urlpatterns = [
    path('', views.calculators, name='calculators'),
    path('addmatrices2x2/', views.addmatrices2x2, name="addmatrices2x2"),
    path('addmatrices3x3/', views.addmatrices3x3, name="addmatrices3x3"),
    path('multiplymatrices2x2/', views.multiplymatrices2x2, name="multiplymatrices2x2"),
    path('multiplymatrices3x3/', views.multiplymatrices3x3, name="multiplymatrices3x3"),
]