"""project5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from app5 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('view_all_http_res/',views.View_all_http_res.as_view()),
    path('view_all_json_res/',views.View_all_json_res.as_view()),
    path('view_all_ser/', views.View_all_ser.as_view()),

    path('view_one/<int:product_no>',views.View_one.as_view()),
    path('view_one_ser/<int:product_no>', views.View_one_ser.as_view())
]
