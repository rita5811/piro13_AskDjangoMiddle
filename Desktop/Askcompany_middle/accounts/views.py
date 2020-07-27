from django.shortcuts import redirect, render, resolve_url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .form import SignupForm
from django.contrib.auth import login as auth_login
# Create your views here.

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

''' #함수 기반 뷰
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save() #이 순간이 user가 생성되는 것
            auth_login(request, user)
            return redirect('profile')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html',{
        'form': form,
    })
'''

class SignupView(CreateView): #클래스 기반 뷰
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        return resolve_url('profile')

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())

signup = SignupView.as_view()

'''
signup = CreateView.as_view(model=User,
                            form_class=SignupForm,
                            success_url=settings.LOGIN_URL,
                            template_name="accounts/signup.html")
'''