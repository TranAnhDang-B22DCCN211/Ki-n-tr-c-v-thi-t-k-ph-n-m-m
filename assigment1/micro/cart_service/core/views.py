import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import CartSerializer

BOOK_SERVICE_URL = "http://127.0.0.1:8002/api/books/"

class CartView(APIView):
    # 1. Xem giỏ hàng của User
    def get(self, request, user_id):
        cart, _ = Cart.objects.get_or_create(user_id=user_id)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    # 2. Thêm vào giỏ hàng
    def post(self, request, user_id):
        book_id = request.data.get('book_id')
        quantity = int(request.data.get('quantity', 1))

        # --- GỌI SANG BOOK SERVICE ĐỂ LẤY GIÁ ---
        try:
            response = requests.get(f"{BOOK_SERVICE_URL}{book_id}/")
            if response.status_code != 200:
                return Response({"error": "Sách không tồn tại bên Book Service"}, status=404)
            book_data = response.json()
            price = book_data['price'] # Lấy giá từ service kia
        except:
             return Response({"error": "Không kết nối được Book Service"}, status=503)
        # ----------------------------------------

        cart, _ = Cart.objects.get_or_create(user_id=user_id)
        
        # Thêm hoặc cập nhật số lượng
        item, created = CartItem.objects.get_or_create(cart=cart, book_id=book_id, defaults={'price': price})
        if not created:
            item.quantity += quantity
        else:
            item.quantity = quantity # set số lượng ban đầu
            item.price = price       # set giá
            
        item.save()
        return Response({"message": "Đã thêm vào giỏ", "cart_id": cart.id})