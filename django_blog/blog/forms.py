# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post,Tag
from .models import Comment


class PostForm(forms.ModelForm):
    # Virtual field for comma-separated tags
    tags_csv = forms.CharField(
        required=False,
        help_text="Comma-separated tags, e.g. django, web, tips",
        label="Tags"
    )

    class Meta:
        model = Post
        fields = ["title", "content", "tags_csv"] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pre-fill tags_csv when editing
        if self.instance and self.instance.pk:
            existing = self.instance.tags.values_list("name", flat=True)
            self.fields["tags_csv"].initial = ", ".join(existing)

    def clean_tags_csv(self):
        raw = self.cleaned_data.get("tags_csv", "")
        # Normalize: split, strip empties, de-duplicate (case-insensitive)
        pieces = [p.strip() for p in raw.split(",") if p.strip()]
        seen = set()
        result = []
        for p in pieces:
            key = p.lower()
            if key not in seen:
                seen.add(key)
                result.append(p)
        return result

    def save(self, commit=True):
        tags_list = self.cleaned_data.get("tags_csv", [])
        post = super().save(commit=commit)
        # Create/find tags, attach to post
        tag_objs = []
        for name in tags_list:
            tag, _ = Tag.objects.get_or_create(name=name)
            tag_objs.append(tag)
        # if commit=False above, ensure post has a pk before setting M2M
        if post.pk:
            post.tags.set(tag_objs)
        return post
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