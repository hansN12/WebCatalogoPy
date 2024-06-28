from django import forms
from .models import Artists
from .models import Albums

class ArtistsForm(forms.ModelForm):
    class Meta:
        model = Artists
        fields = '__all__'

class AlbumsForm(forms.ModelForm):
    class Meta:
        model = Albums
        fields = '__all__'
        widgets = {
            'artist': forms.Select(attrs={'class': 'form-select'}),}
