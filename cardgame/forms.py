from django import forms


class NewGameForm(forms.Form):
    players_num = forms.IntegerField(min_value=1, max_value=4, label='Number of players (1-4)')
    players_num.widget.attrs['class'] = 'form-control'
    squares_num = forms.IntegerField(min_value=1, max_value=79, label='Number of squares on the board (1-79)')
    squares_num.widget.attrs['class'] = 'form-control'
    deck_num = forms.IntegerField(min_value=1, max_value=200, label='Number of cards in the deck (1-200)')
    deck_num.widget.attrs['class'] = 'form-control'

