from django import forms
# from django.forms import extras
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime
from learn.models import Document, Profile, Comments
from string import Template
from django.utils.safestring import mark_safe
from django.forms import ImageField

"""
UserCreationForm contain password1 and password2(conf.password)
it also check both password must be same
"""
class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None):
        html =  Template("""<img src="$link"/>""")
        return mark_safe(html.substitute(link=value))

class SignUpPage(UserCreationForm):                 # renders a signup form to user with the help of template
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class SearchUser(forms.Form):                 # renders a signup form to user with the help of template
    username = forms.CharField(max_length=500, widget=forms.TextInput(
        attrs={'placeholder': 'Enter name of user you need to search',}))

    class Meta:
        fields = ('username',)

class Info(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('First_Name', 'Last_Name', 'City', 'DOB', 'bio', 'profile_pic', )


# class DocumentForm(forms.ModelForm):                   # to render to user a form where he can upload pictures

class DocumentForm(forms.ModelForm):                                                       # it is connected to Document table in database
    # photo = forms.ImageField()
    
    class Meta:
        model = Document
        # status = forms.ModelChoiceField(queryset=Document.objects.filter(uploaded_at=datetime.now()), empty_label=None)
        # width = forms.IntegerField()
        # height = forms.IntegerField()
        # flip = forms.ModelChoiceField(queryset=Document.objects.filter(uploaded_at=datetime.now()), empty_label=None, widget =forms.Select(attrs={
        #     "onChange": 'loadPic()'}))

        # rotate = forms.ModelChoiceField(queryset=Document.objects.filter(uploaded_at=datetime.now()), empty_label=None)
        # blur = forms.ModelChoiceField(queryset=Document.objects.filter(uploaded_at=datetime.now()), empty_label=None)
        # effect = forms.ModelChoiceField(queryset=Document.objects.filter(uploaded_at=datetime.now()), empty_label=None)
        fields = ('document', 'status',)


class UpdateForm(forms.ModelForm):                     # renders a form update pictures uploaded
                                                       # it is connected to Document table in database
    class Meta:
        model = Document
        status = forms.ModelChoiceField(queryset=Document.objects.filter(uploaded_at=datetime.now()),
                                        empty_label=None)
        width = forms.IntegerField()
        height = forms.IntegerField()
        flip = forms.ModelChoiceField(queryset=Document.objects.filter(uploaded_at=datetime.now()),
                                      empty_label=None)
        rotate = forms.ModelChoiceField(queryset=Document.objects.filter(uploaded_at=datetime.now()),
                                         empty_label=None)
        blur = forms.ModelChoiceField(queryset=Document.objects.filter(uploaded_at=datetime.now()),
                                      empty_label=None)
        effect = forms.ModelChoiceField(queryset=Document.objects.filter(uploaded_at=datetime.now()),
                                        empty_label=None)
        fields = ('status', 'width','height', 'flip', 'rotate', 'blur', 'effect')

# class CommentForm(forms.ModelForm):
#
#     class meta:
#         model = Comments
#         fields = ('comment', )

class MessageForm(forms.Form):                 # renders a signup form to user with the help of template
    talk = forms.CharField(max_length=500, widget=forms.TextInput(
        attrs={'placeholder': 'Enter messgage',}))

    class Meta:
        fields = ('talk',)


