from . import views
from django.urls import path
app_name='bank'
urlpatterns=[

    path('but/',views.but,name='but'),
    path('form/',views.form,name='form'),
    path('formm/',views.formm,name='formm'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout')
]