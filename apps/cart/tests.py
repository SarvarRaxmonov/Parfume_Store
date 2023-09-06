from rest_framework.test import APITestCase

from apps.cart.models.cart import District, Cart, Accreditation
from apps.cart.models.cart import Region
from apps.user.models import User


class CartAPITestCase(APITestCase):
    def setUp(self):
        self.region = Region.objects.create(name='Toshkent Viloyati')
        self.district = District.objects.create(region=self.region, name='Toshkent Viloyati')
        self.user = User.objects.create(
            phone_number='+998974436638',
            password='qwert#'
        )
        self.accreditation = Accreditation.objects.create(
            user=self.user,
            region=self.region,
            district=self.district,

        )
        self.cart = Cart.objects.create(
            user=self.user,
            product=1,
            count=123
        )

    def test_user_created(self):
        self.assertEqual(self.user.phone_number, '+998974436638')
