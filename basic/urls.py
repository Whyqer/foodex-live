from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

# Над названиями можно подумать
urlpatterns = [
    path('', views.mainPage, name = 'home'), 
    path('login/', views.loginPage, name = 'login'), 
    path('logout/', views.logoutUser, name = 'logout'), 
    path('registration/', views.registerPage, name = 'register'), 
    path('restaurateur_registration/', views.restRegPage, name = 'restregister'), 
    path('add_restaurant/', views.addRestaurant, name = 'addrest'), 
    path('all/change/add_menu/<str:pk>', views.addMenu, name = 'addmenu'), 
    path('restaurant/<str:pk_test>/', views.restaurant, name = 'restaurant'), 
    path('all/',views.change, name = 'change'),
    path('all/change/<str:pk>', views.redaction, name = 'redaction'),

    path('settings/', views.accountSetting, name='settings'), 
    path('cart/', views.cart, name = 'cart'),
    path('update_menu/',views.updatemenu, name = "update_menu"),

    path('delete_menu/<str:pk_m>',views.deleteMenu, name="delete_menu"),

    path ('reset_password/', auth_views.PasswordResetView.as_view( template_name = "basic/password_reset.html"), name = "reset_password"),
    path ('reset_password_sent/', auth_views.PasswordResetDoneView.as_view( template_name = "basic/password_sent.html"), name="password_reset_done"),
    path ('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "basic/password_change.html"), name = "password_reset_confirm"),
    path ('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view( template_name = "basic/password_complete.html"), name = "password_reset_complete"),
]