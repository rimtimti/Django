from django import forms
from game_app.models import Author

GAMES = [
    ("c", "coin"),
    ("d", "cube"),
    ("r", "ramdom"),
]


class GamesForm(forms.Form):
    game = forms.ChoiceField(choices=GAMES)
    count = forms.IntegerField(min_value=1, max_value=64)


class AddAuthorForm(forms.ModelForm):
    birthdate = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date", "placeholder": "dd.mm.yyyy"})
    )

    class Meta:
        model = Author
        fields = ["firstname", "lastname", "email", "biography", "birthdate"]
