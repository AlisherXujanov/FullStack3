from .usecases import *

# def users(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST, request.FILES)
#         if form.is_valid():
#             username = form.cleaned_data['first_name']
#             messages.success(
#                 request,
#                 f'{username} hass been created successfully!'
#             )
#             form.save(commit=True)

#     context = get_users_context()

#     return render(request, 'index.html', context)


# def user_details(request, user_id):
#     user = User.objects.get(id=user_id)
#     context = {'user': user}
#     return render(request, 'user_details.html', context)


# def delete_user(request, del_id):
#     user = User.objects.get(id=del_id)
#     print(user.first_name)
#     user.delete()
#     print(user.first_name)

#     return redirect('users_view')
