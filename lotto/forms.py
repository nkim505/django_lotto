from django import forms
from .models import GuessNumbers

class PostForm(forms.ModelForm):

    class Meta:
        model = GuessNumbers  #게스넘버스
        fields = ('name', 'text', ) # 유저에게 네임과 텍스트만 받음
