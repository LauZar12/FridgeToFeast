from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Ingredient
from .forms import RecipeForm, IngredientForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView

# Estrategia base para validaciones
class ValidationStrategy:
    def validate(self, form):
        raise NotImplementedError

# Estrategia para validaciones específicas de cocina Africana
class AfricanCuisineValidationStrategy(ValidationStrategy):
    def validate(self, form):
        if form.cleaned_data.get('portions') == "":
            form.add_error('portions', "Please specify the portion size for African cuisine.")
        if form.cleaned_data.get('details') == "":
            form.add_error('details', "Details are required for African cuisine.")

# Estrategia de validación por defecto
class DefaultValidationStrategy(ValidationStrategy):
    def validate(self, form):
        # Validación por defecto, sin reglas adicionales
        pass

# Aplicación del patrón Strategy en la vista
@login_required
@require_GET
def index(request):
    form = RecipeForm()
    strategy = DefaultValidationStrategy()

    if request.GET.get("preference") == "African":
        strategy = AfricanCuisineValidationStrategy()

    # Aplicar la estrategia de validación
    strategy.validate(form)

    show_modal = request.session.pop('show_modal', False)
    return render(request, "home.html", {"form": form, "show_modal": show_modal})


@login_required
def create_ingredient(request):
    if request.method == "POST":
        new_name = request.POST.get("name")
        quantity = request.POST.get("quantity")
        unit = request.POST.get("unit")

        if new_name == "":
            ingredients = Ingredient.objects.all()
            return render(
                request, "list_ingredients.html", {"ingredients": ingredients, "error": "Title and description are required"}
            )

        ingredient = Ingredient(name=new_name, user=request.user, quantity=quantity, unit=unit)
        ingredient.save()
        return redirect("/kitchen/")
    else:
        return redirect("/kitchen/")
