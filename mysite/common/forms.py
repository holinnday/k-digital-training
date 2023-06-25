from django import forms
from django.contrib.auth.forms import UserCreationForm
from common.models import User, Profile

class UserForm(UserCreationForm):

    email = forms.EmailField(label='이메일')
    tel = forms.CharField(label='연락처')
    first_name = forms.CharField(label='성')
    last_name = forms.CharField(label='이름')
    gender = forms.CharField(label='성별')
    nickname = forms.CharField(label='닉네임')


    class Meta:
        model = User
        fields = ("username","first_name","last_name","email","tel","gender","nickname")

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['profile_img','profile_img_date']
#         labels = {
#             'profile_img' :'프로필이미지',
#             'profile_img_date' : '프로필이미지저장날자',
#         }