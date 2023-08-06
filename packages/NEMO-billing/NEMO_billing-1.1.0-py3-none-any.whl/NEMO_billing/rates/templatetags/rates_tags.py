from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

from NEMO_billing.rates.models import Rate

register = template.Library()


@register.simple_tag
def search_rates():
    type_filter = set()
    result = "["
    for item in Rate.objects.all():
        identifier = (
            item.get_item().id if item.type.item_specific else item.id if not item.type.category_specific else ""
        )
        type_name = f"{item.type.get_rate_group_type()}_{identifier}"
        if type_name not in type_filter:
            type_filter.add(type_name)
            item_name = str(item.get_item() or str(item.type))
            result += '{{"name":"{0}", "id":{1}, "type": "{2}", "type_value": "{3}"}},'.format(
                escape(item_name), item.id, item.type.get_rate_group_type().upper(), item.type.get_rate_group_type()
            )
    result = result.rstrip(",") + "]"
    return mark_safe(result)
