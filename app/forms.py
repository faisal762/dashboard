from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label='email',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'email',
            'name': 'username',
            'placeholder': 'Enter your username',
            'autofocus': 'autofocus'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'password',
            'name': 'password',
            'placeholder': 'enter password',
            'aria-describedby': 'password'
        }),
        label='Password'
    )
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput, label='Remember Me')


    
class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=150, 
        label='Username',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'email',
            'name': 'username',
            'placeholder': 'Enter your username',
            'autofocus': 'autofocus'
        }) )
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'email',
            'name': 'username',
            'placeholder': 'Enter your email',
            'autofocus': 'autofocus'
        })
                             )
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'password',
            'name': 'password',
            'placeholder': 'enter password',
            'aria-describedby': 'password'
        }), label='Password')
    terms = forms.BooleanField(required=True, label='I agree to privacy policy & terms')

class VerifyMnemonicForm(forms.Form):
    mnemonic = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Enter your 12-word recovery phrase',
            'required': True,
        }),
        label='Enter your 12-word recovery phrase'
    )