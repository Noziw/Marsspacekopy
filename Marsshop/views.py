from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *
import random
# Create your views here.
class ProductView(APIView):
    def get(self, request):
        Products = Product.objects.all()
        if Products:
            serializer = ProductSRL(Products, many = True)
            return Response(serializer.data)
        else:
            return Response ('Bizda hozircha mahsulotlar yoq')
        
    def post(self, request):
        serializer = ProductSRL(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class EditProductView(APIView):


    def get (self, request, id):
        Product = Product.objects.filter(id=id).first()
        if Product:
            serializer = ProductSRL(Product)
            return Response(serializer.data)
        else:
            return Response("Bunday mahsulot topilmadi")
        

    def patch (self, request, id):
        Product = Product.objects.filter(id=id).first()
        if Product:
            serializer = ProductSRL(instance=Product, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save() 
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("Bunday mahsulot topilmadi")


    def delete(self, request, id):
        Product = Product.objetcs.filter(id=id).first()
        if Product:
           Product.delete()
           return Response("O'chirildi")
        else:
            return Response("Bunday Mahsulot topilmadi")
        


class PostOrderView(APIView):
    def post(self, request):
        product = request.data.get('product')
        products = product.object.all()
        quantiy_order = request.data.get('quantiy')
        if product in products:
            if product in products:
                for product in products:
                    if product == product and quantiy_order == product.quantiy:
                        serializer = OrderSRL(data = request.data)
                        if serializer.is_valid():
                            serializer.save() 
                            return Response(serializer.data)
                        else:
                            return Response(serializer.error)
                    else:
                        continue
                    
            else:
                return Response('bizda unday maxsulot mavjud emas')
            
def cd():
    return random.randint(1000,9999)



class PostOrderView(APIView):
    def post(self, request, id ):
        product = Product.object.filter(id = id).first()
        if product:
            quantity = request.data.get('quantity')
            if product.quantity <= quantity:
                a = cd()
                return Response(f'haridingiz uchun raxmat, sizning kodingiz {a}')
            else:
                return Response('xatolik yuz berdi')
            

class GetOrderView(APIView):
    def get(self, request, id):
        user = User.object.filter(id= id).first()
        if user:
            order = Order.object.filter(user = user)
            serializers = OrderSerializer(order, many= True)
            return Response(serializers.data)
        else:
            return Response('bunday user mavjud emas')


