from django.urls import path
from . import views
urlpatterns = [
    path('' , views.index , name="index"),
    path('addtocart/<int:id>' , views.addtocart, name='addtocart'),
    path('addtocart2/<int:id>' , views.addtocart2, name='addtocart2'),
    path('deletefromcart/<int:id>' , views.deletefromcart, name='deletefromcart'),
    path('upgradefromcart/<int:id>' , views.upgradefromcart, name='upgradefromcart'),
    path('lessfromcart/<int:id>' , views.lessfromcart, name='lessfromcart'),
]