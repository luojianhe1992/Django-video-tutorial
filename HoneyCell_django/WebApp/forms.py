from django import forms
from WebApp.models import *

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article

        fields = ['user', 'title', 'body']

    def clean(self):
        cleaned_data = super(ArticleForm, self).clean()

        user = cleaned_data.get('user')
        title = cleaned_data.get('title')
        body = cleaned_data.get('body')

        if not (user and title and body):
            raise forms.ValidationError("There are some fields which are None.")

        return cleaned_data

    def clean_title(self):

        user = self.cleaned_data.get('user')
        title = self.cleaned_data.get('title')

        if len(Article.objects.filter(user=user, title=title)):
            raise forms.ValidationError("The title for this user already exsit.")

        return title

    def clean_body(self):

        user = self.cleaned_data.get('user')
        body = self.cleaned_data.get('body')

        if len(Article.objects.filter(user=user, body=body)):
            raise forms.ValidationError("The body for this user already exsit.")

        return body




# Create three Form


class ContactForm1(forms.Form):
    subject = forms.CharField(max_length=1000)

class ContactForm2(forms.Form):
    sender = forms.EmailField()

class ContactForm3(forms.Form):
    message = forms.CharField(widget=forms.Textarea)











