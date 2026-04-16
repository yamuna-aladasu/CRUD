from django.urls import path
from .views import Createlist,Productupdate,Productdeletion,Productpartialupdate
urlpatterns=[
    path('productcreated/',Createlist.as_view(),name='productcreation'),
    path('products/',Createlist.as_view(),name='productdisplay'),
    path('updateproduct/<int:pk>/',Productupdate.as_view(),name='updation'),
    path('productdelete/<int:pk>/',Productdeletion.as_view(),name='deletion'),
    path('productpatch/<int:pk>/',Productpartialupdate.as_view(),name='partial')
]

