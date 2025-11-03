from django.urls import path 
from .views import MessageView, Home2View, Home3View  

urlpatterns = [
                                                                                                    path('', MessageView.as_view(), name='message'),
                                                                                                    path('home2/', Home2View.as_view(),name='home2'),
                                                                                                    path('home3/', Hone3View.as_view(), name='home3'),  
]