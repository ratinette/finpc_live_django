"""quiz_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from app.views import get_quiz, get_404_page, check_quiz_answer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/<int:quiz_id>', get_quiz, name="get_quiz"),
    path('quiz/<int:quiz_id>/options/<int:option_id>/check', check_quiz_answer, name="check_quiz_answer"),
    path('404', get_404_page, name="get_404_page")
]
