from django import template
from store.models import Category
from cart.utils import get_cart_data

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def check_field_class(field):
    # if field.name == 'address_1' or field.name == 'address_2':
    #     return True
    if field.name in ['address_1', 'address_2']:
        return True


@register.simple_tag()
def get_cart_total_qty(request):
    cart_data = get_cart_data(request)
    return cart_data['cart_total_quantity']