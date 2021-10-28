from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Category, Product


# def products_list(request):
#     category = None
#     paginated_by = 6
    
#     queryset = Product.available.all()

#     data = {
#         products: 'queryset'
#     }

#     return render(request, '', data)


# def product_detail(request, product_slug):
#     pass

class ProductDetailView(DetailView):
    queryset = Product.available.all()


class ProductListView(ListView):
    category = None
    paginate_by = 6

    def get_queryset(self):
        queryset = Product.available.all()

        category_slug = self.kwargs.get("slug")
        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=self.category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        context["categories"] = Category.objects.all()
        return context
