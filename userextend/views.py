from datetime import datetime
import random

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from userextend.forms import UserForm
from userextend.models import History, UserProfile


# Create your views here.


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('user_profile')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()
            new_user.last_name = new_user.last_name.title()
            # new_user.username = f'{new_user.first_name[0].lower()}{new_user.last_name.lower().replace(" ", "")}_{random.randint(100000, 999999)}'
            new_user.save()


        # Creating UserProfile

            user_profile = UserProfile.objects.create(user=new_user)
            user_profile.custom_username = self.request.POST['username']
            user_profile.save()

            login(self.request, new_user)

            # get_message = (f' {new_user.username} was successfully added.'
            #                f'first_name:{new_user.first_name},'
            #                f'last_name:{new_user.last_name},'
            #                f'email:{new_user.email}')
            #
            # History.objects.create(message=get_message, created_at=datetime.now(), active=True)

            return redirect('user_profile')
        return super().form_valid(form)


def user_profile_redirect(request):
    user = request.user
    return render(request, 'userextend/useradded.html', {'user':user})

#     def get_success_url(self):
#
#         return reverse_lazy('user_profile', kwargs={'username': self.object.username})
#
#
# def user_profile(request, username):
#     user = User.objects.get(username=username)
#
#     return render(request, 'userextend/useradded.html', {'user': user})
