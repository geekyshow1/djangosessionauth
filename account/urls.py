from django.urls import path
from account.views import RegistrationView, ActivateView, ActivationConfirm, GetCSRFToken,CheckAuthenticatedView, LoginView, UserDetailView, ChangePasswordView, DeleteAccountView, LogoutView, ResetPasswordEmailView, ResetPasswordView, ResetPasswordConfirmView

urlpatterns = [
    path('account/csrf_cookie/', GetCSRFToken.as_view(), name='csrf_cookie'),
    path('account/checkauth/', CheckAuthenticatedView.as_view(), name='check_auth'),
    path('account/registration/', RegistrationView.as_view(), name='register'),
    path('account/activate/<str:uid>/<str:token>/', ActivateView.as_view(), name='activate'),
    path('account/activate/', ActivationConfirm.as_view(), name='activation_confirm'),
    path('account/login/', LoginView.as_view(), name='login'),
    path('account/user/', UserDetailView.as_view(), name='user_detail'),
    path('account/change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('account/delete/', DeleteAccountView.as_view(), name='user_delete'),
    path('account/logout/', LogoutView.as_view(), name='logout'),
    path('account/reset_password/', ResetPasswordEmailView.as_view(), name='reset_password_email'),
    path('account/reset_password/<str:uid>/<str:token>/', ResetPasswordView.as_view(), name='reset_password'),
    path('account/reset_password_confirm/', ResetPasswordConfirmView.as_view(), name='reset_password_confirm'),
]