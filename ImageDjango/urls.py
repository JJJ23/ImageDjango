"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from AzureImage import views
from AzureImage import ImgDetectViews
from AzureImage import learningView

urlpatterns = [
    #path('', include('AzureImage.urls')),
    path('', views.IndexPageView.as_view()),
    path('detect', ImgDetectViews.ImageDetectView.as_view(), name='detect'),
    path('learning', learningView.ImageLearningView.as_view(), name='learning'),
    path('admin/', admin.site.urls),
]