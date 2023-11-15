from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from dashboard.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserSetPasswordForm, \
    UserPasswordChangeForm
from django.contrib.auth import logout

# 在 views.py 文件中
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class DashboardView(LoginRequiredMixin, View):
    """
    仪表板视图
    """
    login_url = '/dashboard/accounts/login/'
    redirect_field_name = 'next'
    template_name = 'dashboard/index.html'

    def get(self, request, *args, **kwargs):
        """
        跳转到仪表板主页面
        """
        return render(request, self.template_name, {'segment': 'index'}, *args, **kwargs)


# Dashboard

def billing(request):
    return render(request, 'dashboard/billing.html', {'segment': 'billing'})


def tables(request):
    return render(request, 'dashboard/tables.html', {'segment': 'tables'})


def vr(request):
    return render(request, 'dashboard/virtual-reality.html', {'segment': 'vr'})


def rtl(request):
    return render(request, 'dashboard/rtl.html', {'segment': 'rtl'})


def profile(request):
    return render(request, 'dashboard/profile.html', {'segment': 'profile'})


# Authentication
class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print('Account created successfully!')
            return redirect('/accounts/login/')
        else:
            print('Register failed!')
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')


class UserPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
    form_class = UserPasswordResetForm


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    form_class = UserSetPasswordForm


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    form_class = UserPasswordChangeForm
