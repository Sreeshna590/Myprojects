from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Menu, MenuItem
from .forms import MenuItemForm,MenuUpdateForm

# List all menus with their items
class MenuListView(ListView):
    model = Menu
    template_name = 'menu_list.html'
    context_object_name = 'menus'

# Display all items in a specific menu
class MenuDetailView(DetailView):
    model = Menu
    template_name = 'menu_items.html'
    context_object_name = 'menu'

# Add a new MenuItem
class MenuItemCreateView(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'add_menu_items.html'
    success_url = reverse_lazy('menu_list')

# Update the price of a MenuItem
class MenuItemUpdateView(UpdateView):
    model = MenuItem
    form_class = MenuUpdateForm
    template_name = 'update.html'
    success_url = reverse_lazy('menu_list')

class DeleteView(DeleteView):
    model = MenuItem
    template_name = 'delete.html'  # Specify a confirmation template
    success_url = reverse_lazy('menu_list')

