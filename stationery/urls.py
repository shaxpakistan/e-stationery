from django.urls import path
from .views import *
from .addToCart import addTocartView
from pagecounter import mzigo

urlpatterns = [

    #site base urls
    path('', HomeView.as_view(), name="homepage"),    
    path('about/', AboutView.as_view(), name="aboutus"),
    path('contact/', ContactView.as_view(), name="contactus"),
    path('products/', ProductsViews.as_view(), name="products_list"),
    path('records/', MyrecordsView.as_view(), name="myrecords"),
    path('records/order-<int:pk>/', OrderDetailView.as_view(), name="orderdetails"),

    #stationery base urls
    path('register-stationery/', StationeryRegister.as_view(), name="new_stationery"),
    path('stationery/<str:pk>/', DetailsView.as_view(), name="stationery_details"),
    path('<str:pk>/products/', ProductView.as_view(), name="products"),
    path('item/<int:pk>/', OneProduct.as_view(), name="item"),
    path('addproduct/<str:pk>/', AddProduct.as_view(), name="post-product"),
    path('mystationery/<str:pk>/', Mystationery.as_view(), name="mystationery"),
    path('stock/<str:pk>/', StockView.as_view(), name="stock"),
    path('stockdetails/<str:pk>/', StockDetailsView.as_view(), name="stock-details"),
    path('orderdetails/<str:stat>/<str:pk>/', StationeryOrderDetailsView.as_view(), name="order-details"),
    path('updatestock/<int:pk>/', StockUpdateView.as_view(), name="update-stock"),
    path('deletestock/<int:pk>/', StockDeleteView.as_view(), name="delete-stock"),

    #stationer urls 
    path('dashboard/', StationeryDashboard.as_view(), name="dashboard"),    
    path('category/<str:pk>/', CategoryView.as_view(), name = "filtercategory"),

    #carts urls
    path('<int:pk>/', addTocartView, name="addtocart"),
    path('my-cart/', MyCartView.as_view(), name="mycart"),
    path('manage-cart/<int:cp_id>/', ManageCartView.as_view(), name='managecart'),
    path('emptycart/', EmptyCartView.as_view(), name='emptycart'),
    path('checkout/', CheckOutView.as_view(), name='checkout'),


    #booking stationery
    path('pagecounter/', mzigo, name = "doc"),
    path('booking/<str:pk>/', BookingView.as_view(), name = "booking"),
    path('booking-records/', BookingRec.as_view(), name = "bookingrec"),

]
