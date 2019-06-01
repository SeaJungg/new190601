from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showblog, name='index'),
    path('blog/<int:blog_id>', views.detail, name="detail" ),
    path('blog/new/', views.new, name="new"),
    path('blog/create/', views.create, name="create"),
]
# 여러객체를 다룰때 blog/<int:blog_id(그냥변수이름)> 사용함 blog/1 같은거
