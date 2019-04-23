from django import forms
from .models import Genre, Movie, Score

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields = '__all__'
        
class ScoreForm(forms.ModelForm):
    class Meta:
        model=Score
        fields=['content','value',]