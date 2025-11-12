from django.urls import path 
from .views import LoginView, Home1View, Home2View, Home3View   

urlpatterns = [
                                                                                                    path('', LoginView.as_view(), name='login'),
                                                                                                    path('home1/', Home1View.as_view(), name='home1'),
                                                                                                    path('home2/', Home2View.as_view(),name='home2'),
                                                                                                    path('home3/', Home3View.as_view(), name='home3'),  
]