from django.contrib import admin
from django.urls import path
from AppCoder.views import home, search, model1_create, model1_search, model2_create, model2_search, model3_create, model3_search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('search/', search, name='search'),
    path('model1/create/', model1_create, name='model1_create'),
    path('model1/search/', model1_search, name='model1_search'),
    path('model2/create/', model2_create, name='model2_create'),
    path('model2/search/', model2_search, name='model2_search'),
    path('model3/create/', model3_create, name='model3_create'),
    path('model3/search/', model3_search, name='model3_search'),
]
