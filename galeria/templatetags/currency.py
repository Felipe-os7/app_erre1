from django import template
from decimal import Decimal

register = template.Library()


@register.filter(is_safe=True)
def clp(value):
    """Formatea un número a peso chileno: agrega `$` y separadores de miles con `.`.
    No muestra decimales. Si el valor es falso o vacío, devuelve cadena vacía.
    Ej: 1234567.89 -> "$1.234.568" (redondeado)
    """
    if value in (None, '', False):
        return ''
    try:
        # Aceptar Decimal, float, int, str
        amount = Decimal(value)
    except Exception:
        return value
    # redondear al entero más cercano
    amount_int = int(round(amount))
    # formato con separador de miles y reemplazo de ',' por '.'
    formatted = f"{amount_int:,}".replace(',', '.')
    return f"${formatted}"
