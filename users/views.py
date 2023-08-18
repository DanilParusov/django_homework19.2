import random

from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from django.conf import settings

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        self.object = form.save()
        if form.is_valid():
            code = ''.join([str(random.randint(0, 9)) for _ in range(12)])
            self.object.verification_code = code
            self.object.save()
            send_mail(
                'email verification',
                f'Your password - {code}',
                settings.EMAIL_HOST_USER,
                [self.object.email]
            )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('users:verify_email', kwargs={'email': self.object.email})

class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('user:profile')

    def get_object(self, queryset=None):
        return self.request.user

def verify_email(request, email):
    if request.method == 'POST':
        code_to_check = request.POST.get('verification_code')
        user = User.objects.get(email=email)
        if user.verification_code == code_to_check:
            user.is_email_verified = True
            user.save()
            return redirect(reverse('users:login'))
        else:
            raise ValidationError(f'You have used the wrong code!')
    else:
        context = {'page_title': 'Email verification'}
        return render(request, 'users/verify_email.html', context)