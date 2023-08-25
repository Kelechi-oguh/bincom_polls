"""
URL configuration for bincom_polls project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from polls.views import home, polling_unit_result, lga_result_sum, new_polling_unit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('unit/<int:unitid>/', polling_unit_result, name='polling_unit'),
    path('unit/new/', new_polling_unit, name='new_unit'),
    path('lga/<int:_id>/', lga_result_sum, name='lga_sum')
]
