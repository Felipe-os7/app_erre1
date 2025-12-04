"""
Utilidades para el manejo del carrito de compras
"""
from decimal import Decimal


def get_cart(request):
    """Obtiene el carrito de la sesión"""
    return request.session.get('cart', [])


def add_to_cart(request, item_type, item_id, title, price=None):
    """Agrega un item al carrito"""
    cart = get_cart(request)
    
    # Verificar si el item ya existe
    for item in cart:
        if item['type'] == item_type and item['id'] == item_id:
            return False  # Ya existe
    
    # Agregar nuevo item
    cart.append({
        'type': item_type,  # 'painting' o 'mural'
        'id': item_id,
        'title': title,
        'price': float(price) if price else None,
    })
    
    request.session['cart'] = cart
    request.session.modified = True
    return True


def remove_from_cart(request, item_type, item_id):
    """Elimina un item del carrito"""
    cart = get_cart(request)
    cart = [item for item in cart if not (item['type'] == item_type and item['id'] == item_id)]
    request.session['cart'] = cart
    request.session.modified = True
    return cart


def clear_cart(request):
    """Limpia el carrito"""
    if 'cart' in request.session:
        del request.session['cart']
    request.session.modified = True


def get_cart_total(cart):
    """Calcula el total del carrito"""
    total = Decimal('0.00')
    for item in cart:
        if item.get('price'):
            total += Decimal(str(item['price']))
    return total


def get_cart_summary(cart):
    """Obtiene un resumen del carrito para incluir en el mensaje"""
    if not cart:
        return ""
    
    summary = "\n\n--- COTIZACIÓN SOLICITADA ---\n\n"
    paintings = [item for item in cart if item['type'] == 'painting']
    murals = [item for item in cart if item['type'] == 'mural']
    
    if paintings:
        summary += "PINTURAS:\n"
        for item in paintings:
            summary += f"- {item['title']}"
            if item.get('price'):
                summary += f" - ${item['price']:,.0f} CLP"
            summary += "\n"
        summary += "\n"
    
    if murals:
        summary += "MURALES:\n"
        for item in murals:
            summary += f"- {item['title']}"
            if item.get('price'):
                summary += f" - ${item['price']:,.0f} CLP"
            summary += "\n"
        summary += "\n"
    
    total = get_cart_total(cart)
    if total > 0:
        summary += f"TOTAL: ${total:,.0f} CLP\n"
    
    return summary

