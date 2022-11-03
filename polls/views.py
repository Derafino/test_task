from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from polls.forms import UploadFileForm
from polls.logic import data_preparation
from polls.models import User, UserAvatar


@staff_member_required()
def index(request):
    display_users = list()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            xml_file = request.FILES['xml_file']
            data = data_preparation(csv_file, xml_file)
            data = [u for u in data.to_dict('records')]
            new_users = list()
            for i in data:
                if not User.objects.filter(username=i['username']):
                    new_user = User.objects.create_user(username=i['username'],
                                                        password=i['password'],
                                                        date_joined=i['date_joined'],
                                                        first_name=i['first_name'],
                                                        last_name=i['last_name'],
                                                        )
                    new_user.save()
                    if i['avatar']:
                        user_avatar = UserAvatar.objects.create(user=new_user, avatar=i['avatar'])
                        user_avatar.save()
                    new_users.append(new_user)
            display_users = list()
            for user in new_users:
                user_db = User.objects.get(username=user.username)
                try:
                    avatar = UserAvatar.objects.get(user=user)
                    img = avatar.avatar
                except UserAvatar.DoesNotExist:
                    img = None
                display_users.append({
                    'username': user_db.username,
                    'date_joined': user_db.date_joined,
                    'first_name': user_db.first_name,
                    'last_name': user_db.last_name,
                    'avatar': img}

                )
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form, 'users': display_users})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('index')
            else:
                return redirect('home')
        return redirect('login')
    return render(request, 'login.html')


@login_required
def home(request):
    user = request.user
    try:
        avatar = UserAvatar.objects.get(user=user)
        img = avatar.avatar
    except UserAvatar.DoesNotExist:
        img = None
    return render(request, 'home.html', {'user': user, 'img': img})


def logout_view(request):
    logout(request)
    return redirect('login')



