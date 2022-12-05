from .models import Category


def extras(request):
    categories = Category.objects.order_by('name')
    return {'categories': categories}
