from django import forms
from .models import VideoGame


class GameForm(forms.ModelForm):
    class Meta:
        model = VideoGame
        fields = {'name', 'genre', }
