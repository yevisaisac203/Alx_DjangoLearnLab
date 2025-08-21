# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post
from .models import Comment

class RegisterForm(UserCreationForm):
    """
    Extends Django's signup form to also collect email.
    - UserCreationForm already gives you password1 + password2 (with validation).
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        # The fields you want in the form, in order:
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        """
        Optional: basic 'unique email' check.
        Django's default User doesn't enforce unique emails, so we add this.
        """
        email = self.cleaned_data.get("email")
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email


class ProfileForm(forms.ModelForm):
    """
    Simple 'edit profile' form that edits the built-in User fields.
    """
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 8}),
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment...'}),
        }
        labels = {'content': ''}       