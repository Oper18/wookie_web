from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from .models import ChatUser
from django import forms

class ChatUserLoginForm(AuthenticationForm):
    class Meta:
        model = ChatUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(ChatUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ChatUserRegisterForm(UserCreationForm):
    class Meta:
        model = ChatUser
        fields = ('username', 'password1', 'password2', 'email', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    # def clean_age(self):
    #     data = self.cleaned_data['age']
    #
    #     return data

class ChatUserEditForm(UserChangeForm):
    class Meta:
        model = ChatUser
        fields = ('username', 'email', 'password', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()