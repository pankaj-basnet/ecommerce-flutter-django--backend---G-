from django.shortcuts import render #isn= commented

from rest_framework import generics, status       # isn=
from rest_framework.response import Response       # isn=
from rest_framework.views import APIView       # isn=
from . import models, serializers       # isn=
from django.db.models import Count       # isn=
import random       # isn=

class CategoryList(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer

    queryset = models.Category.objects.all()

class HomeCategoryList(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):

        queryset = models.Category.objects.all()
        # print(queryset.count())           # sn=

        queryset = queryset.annotate(random_order = Count('id'))
        # print(queryset[0].random_order)           # sn=
        # print(queryset[1].random_order)           # sn=

        queryset = list(queryset)
        random.shuffle(queryset)

        return queryset[:5]
    
class BrandList(generics.ListAPIView):
    serializer_class = serializers.BrandSerializer

    queryset = models.Brand.objects.all()

class ProductList(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):

        queryset = models.Product.objects.all()
        queryset = queryset.annotate(random_order = Count('id'))

        queryset = list(queryset)
        random.shuffle(queryset)

        return queryset[:20]

class PopularProductsList(generics.ListAPIView):

    serializer_class = serializers.ProductSerializer

    def get_queryset(self):

        queryset = models.Product.objects.filter(ratings__gte=4.0, ratings__lte = 5.0)
        queryset = queryset.annotate(random_order = Count('id'))

        queryset = list(queryset)
        random.shuffle(queryset)

        return queryset[:20]



# class ProductListByClothesType(generics.ListAPIView): #isn= #TypeError: ProductListByClothesType.get_queryset() missing 1 required positional argument: 'request'
# # class ProductListByClothesType(APIView): #isn=
#     serializer_class = serializers.ProductSerializer

#     # def get_queryset(self, request): # isn=
#     def get_queryset(self): #sn=
#         query = self.request.query_params.get('clothesType', None)
#         queryset = models.Product.objects.filter(clothesType = query)


#         if query:
#             # queryset = models.Product.objects.filter(clothesType = query)
#             queryset = queryset.annotate(random_order = Count('id'))

#             products_list = list(queryset)
#             random.shuffle(products_list)

#             limited_products =  products_list[:20]

#             serializer = serializers.ProductSerializer(limited_products, many= True)

#             return Response(serializer.data)
        
#         else:
#             return Response({'message': 'No query provided'}, status=status.HTTP_400_BAD_REQUEST)
    


# sn= -------------------------------------------------------------------
class ProductListByClothesType(APIView): #isn= #TypeError: ProductListByClothesType.get_queryset() missing 1 required positional argument: 'request'
# class ProductListByClothesType(APIView): #isn=
    serializer_class = serializers.ProductSerializer

    # ## def get_queryset(self, request): # isn=
    # def get(self):                   #sn=  # TypeError: ProductListByClothesType.get() takes 1 positional argument but 2 were given
    #     query = self.request.query_params.get('clothesType', None) # doesnot work --- error

    # def get_queryset(self, request): # isn=
    def get(self, request): #isn=
        query = request.query_params.get('clothesType', None)



        queryset = models.Product.objects.filter(clothesType = query)
        print('--------------------------')


        if query:
            # queryset = models.Product.objects.filter(clothesType = query)
            queryset = queryset.annotate(random_order = Count('id'))

            products_list = list(queryset)
            random.shuffle(products_list)

            limited_products =  products_list[:20]

            serializer = serializers.ProductSerializer(limited_products, many= True)

            return Response(serializer.data)
        
        else:
            return Response({'message': 'No query provided'}, status=status.HTTP_400_BAD_REQUEST)
    



class SimilarProducts(APIView):

    def get(self, request):
        query = request.query_params.get('category', None)

        if query:
            products = models.Product.objects.filter(category = query)

            product_list = list(products)
            random.shuffle(product_list)

            limited_products = product_list[:6]

            serializer = serializers.ProductSerializer(limited_products, many = True)

            return Response(serializer.data)
        else:
            return Response({'message': 'No query provided'}, status= status.HTTP_400_BAD_REQUEST)
        

class SearchProductByTitle(APIView):
    def get(self, request):
        query = request.query_params.get('q', None)

        if query:
            products = models.Product.objects.filter(title_icontains = query)

            serializer = serializers.ProductSerializer(products, many= True)
            return Response(serializer.data)
        else:
            return Response({'message': 'No query provided'}, status= status.HTTP_400_BAD_REQUEST)


class FilterProductByCategory(APIView):
    def get(self, request):
        query = request.query_params.get('category', None)

        if query:
            products = models.Product.objects.filter(category = query)

            serializer = serializers.ProductSerializer(products, many = True)

            return Response(serializer.data)
        else:
            return Response({'message': 'No query provided'}, status= status.HTTP_400_BAD_REQUEST)