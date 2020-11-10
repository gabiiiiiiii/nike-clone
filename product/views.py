from django.http  import JsonResponse
from django.views import View
from .models      import Product, SubImageUrl

class ProductlistView(View):
    def get(self, request):
        try:
            product_list = [{
                    "id"    : product.id,
                    "img"   : product.main_image_url,
                    "title" : product.name,
                    "price" : int(product.price),
                    "color" : product.color.first().name
                    } for product in Product.objects.filter(type__name="조던").distinct()]
            
            return JsonResponse({"shoes": product_list}, status = 200)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)

class DetailView(View):
    def get(self, request, product_id):
        selected_product = Product.objects.get(pk=product_id)

        data = {
            "id"          : selected_product.id,
            "price"       : int(selected_product.price),
            "name"        : selected_product.name,
            "detailImage" : [image.url for image in SubImageUrl.objects.filter(product_id=selected_product)],
            "title"       : selected_product.description_title,
            "content"     : selected_product.description_content,
            "color"       : selected_product.description_color,
            "style"       : selected_product.style
        }

        return JsonResponse({"data": data}, status = 200)