from django.urls import path,include
from .views import *
from .strategy import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products',ProductViewSet,basename='products')
router.register(r'lowcal',LowCalViewSet,basename='lowcal')
router.register(r'diabetic',DiabeticViewSet,basename='diabetic')
router.register(r'protein',ProteinViewSet,basename='protein')
router.register(r'supplement',SupplementViewSet,basename='supplement')

urlpatterns = [
    path('',latest_homepage,name='latest_homepage'),
    path('adminpanel/',adminpanel,name='adminpanel'),
    path('create/',addproduct,name='create'),
    path('delete/<str:pk>/',deleteproduct,name='delete'),
    path('update/<str:pk>/',editproduct,name='update'),
    path('product/<str:pk>/',editproduct,name='product'),
    path('signup/',registration,name ='registration'),
    path('login/',loginpage,name ='login'),
    path('logout/',logoutuser,name = 'logoutpage'),
    path('password_change/',PasswordsChangeView.as_view(template_name='store/change_password.html'),name='password_change'),
    path('products/',filter, name="products"),
    path('singleproduct/<str:pk>/',singleproduct, name="singleproduct"),
    path('latest/',latest, name="latest"),
    path('contact/',contact,name='contact'),

    path('products/',ShowAllProducts().showProducts,name='products'),
    path('lowcal/',ShowLowCal().showProducts,name='lowcal'),
    path('diabetic/',ShowDiab().showProducts,name='diabetic'),
    path('protein/',ShowProt().showProducts,name='protein'),
    path('supplements/',ShowSupplements().showProducts,name = 'supplements'),
    path('nutri/',ShowNutri().showProducts,name = 'nutri'),
    path('bev/',ShowBev().showProducts,name = 'bev'),

    path('api/',include(router.urls))
]
