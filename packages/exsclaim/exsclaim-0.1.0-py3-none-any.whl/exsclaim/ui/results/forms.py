from django import forms

class ResultsForm(forms.Form):
    keywords = forms.CharField(max_length=100)
    keyword_locations = [
        ("sc", "Subfigure Caption"),
        ("fc", "Full Caption"),
        ("t", "Article Title")
    ]
    keyword_location = forms.MultipleChoiceField(
        choices=keyword_locations,
        widget=forms.CheckboxSelectMultiple
    )