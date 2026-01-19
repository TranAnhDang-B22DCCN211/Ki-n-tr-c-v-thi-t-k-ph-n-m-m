# cart/views.py


from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status, views, permissions
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import CartSerializer
from books.models import Book

class CartView(views.APIView):
    # Chỉ cho phép người đã đăng nhập mới được xem giỏ
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Lấy giỏ hàng của user đang đăng nhập
        cart, created = Cart.objects.get_or_create(customer=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

class AddToCartView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # Lấy dữ liệu gửi lên: book_id và quantity
        book_id = request.data.get('book_id')
        quantity = int(request.data.get('quantity', 1))

        # 1. Tìm hoặc tạo giỏ hàng cho user
        cart, created = Cart.objects.get_or_create(customer=request.user)

        # 2. Kiểm tra sách có tồn tại không
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({"error": "Sách không tồn tại"}, status=status.HTTP_404_NOT_FOUND)

        # 3. Thêm vào giỏ (Nếu có rồi thì cộng dồn, chưa có thì tạo mới)
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, book=book)
        
        if not item_created:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart_item.quantity = quantity
            cart_item.save()

        return Response({"message": "Đã thêm vào giỏ thành công!"}, status=status.HTTP_200_OK)