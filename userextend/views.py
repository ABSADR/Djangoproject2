from datetime import datetime
import random

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from userextend.forms import UserForm, UserProfileForm
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


@login_required
def edit_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            # Save user-related fields
            user = user_form.save(commit=False)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()

            return redirect('login')


    else:
        user_form = UserForm(instance=request.user)

        print('here now')

    return render(request, 'userextend/edit_user.html', {'user_form': user_form})




def edit_profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.age = request.POST['age']
            profile.gender = request.POST['gender']
            profile.country = request.POST['country']
            profile.zodiac = request.POST['zodiac']
            profile.save()

            # Redirect to a success page or any other desired page
            return redirect('user_profile')

    else:
        profile_form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'userextend/edit_profile.html', {'profile_form': profile_form})



class UserListView(ListView):
    template_name = 'userextend/list_of_users.html'
    model = User
    context_object_name = 'all_users'


    def get_queryset(self):
        return User.objects.filter(is_active=True)

