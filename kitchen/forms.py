from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Ingredient


# Decorador para agregar validaciones adicionales al formulario
class FormValidationDecorator:
    def __init__(self, form):
        self.form = form

    def add_validation(self, field, error_message):
        if not self.form.cleaned_data.get(field):
            self.form.add_error(field, error_message)

    def is_valid(self):
        return self.form.is_valid()


class RecipeForm(forms.Form):
    details = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'E.g. "20 minutes to prepare", "for a celebration", etc.'}),
        max_length=100,
        required=False,
        label="Any specific requests? (preparation time, length, complexity, etc.)",
    )

    def __create_tuples(lst):
        return [(elem, elem) for elem in lst]

    preference = forms.ChoiceField(
        required=False,
        choices=__create_tuples([
            _("Any kind of cuisine"),
            _("African"),
            _("Caribbean"),
            _("Central American"),
            _("Central European"),
            _("Chinese"),
            _("East Asian"),
            _("Eastern European"),
            _("German"),
            _("Indian"),
            _("North American"),
            _("Northern European"),
            _("Oceanic"),
            _("South American"),
            _("South Asian"),
            _("South Eastern European"),
            _("Southern European"),
            _("Western European"),
        ]),
        label="What kind of cuisine are you looking for?",
    )

    portions = forms.ChoiceField(
        required=False,
        choices=__create_tuples([
            _("1 person"),
            _("2 people"),
            _("3 people"),
            _("4 people"),
            _("5 people"),
            _("6 people"),
            _("7 people"),
            _("8 people"),
            _("9 people"),
            _("+10 people"),
        ]),
        label="How many people is the recipe for?",
    )


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']


