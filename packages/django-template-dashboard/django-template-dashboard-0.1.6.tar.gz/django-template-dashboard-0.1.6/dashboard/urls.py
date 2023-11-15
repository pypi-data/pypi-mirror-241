from django.urls import path
from dashboard import views as dashboard_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', dashboard_views.DashboardView.as_view(), name='index'),
    path('billing/', dashboard_views.billing, name='billing'),
    path('tables/', dashboard_views.tables, name='tables'),
    path('vr/', dashboard_views.vr, name='vr'),
    path('rtl/', dashboard_views.rtl, name='rtl'),
    path('profile/', dashboard_views.profile, name='profile'),

    # Authentication
    path('accounts/login/', dashboard_views.UserLoginView.as_view(), name='login'),
    path('accounts/logout/', dashboard_views.logout_view, name='logout'),
    path('accounts/register/', dashboard_views.register, name='register'),
    path('accounts/password-change/', dashboard_views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name='password_change_done'),
    path('accounts/password-reset/', dashboard_views.UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/',
         dashboard_views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),
]
