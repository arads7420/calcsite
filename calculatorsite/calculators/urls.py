from django.urls import path
from . import views


urlpatterns = [
    path('', views.calculators, name='calculators'),
    path('addmatrices2x2/', views.addmatrices2x2, name="addmatrices2x2"),
    path('addmatrices3x3/', views.addmatrices3x3, name="addmatrices3x3"),
    path('addmatrices4x4/', views.addmatrices4x4, name="addmatrices4x4"),
    path('addmatrices5x5/', views.addmatrices5x5, name="addmatrices5x5"),
    path('multiplymatrices2x2/', views.multiplymatrices2x2, name="multiplymatrices2x2"),
    path('multiplymatrices3x3/', views.multiplymatrices3x3, name="multiplymatrices3x3"),
    path('multiplymatrices4x4/', views.multiplymatrices4x4, name="multiplymatrices4x4"),
    path('determinant2x2/', views.determinant2x2, name="determinant2x2"),
    path('determinant3x3/', views.determinant3x3, name="determinant3x3"),
    path('eigenvalues2x2/', views.eigenvalues2x2, name="eigenvalues2x2"),
    path('eigenvalues3x3/', views.eigenvalues3x3, name="eigenvalues3x3"),
]