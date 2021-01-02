from django.contrib.auth.models import User
from django.test import TestCase, Client
from estate_app.models import Ad, SaleOrRent, NumberRooms, TypePremise, District, DistrictCity, DistrictCityArea, \
    Construction, Furniture, Elevator


class TestViewsEstateApp(TestCase):
    def test_about_us_page_loads_successfully(self):
        client = Client()
        response = client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_general_rules_page_loads_successfully(self):
        client = Client()
        response = client.get('/general_rules/')
        self.assertEqual(response.status_code, 200)

    def test_create_ad_page_opens_when_user_logged_in(self):
        User.objects.create_user(username="Pesho567", password='BrumDrun@123')
        client = Client()
        client.login(username="Pesho567", password='BrumDrun@123')
        response = client.get('/create_ad/')
        self.assertEqual(response.status_code, 200)

    def test_create_ad_page_NOT_open_when_user_NOT_logged_in(self):
        client = Client()

        response = client.get('/create_ad/')
        self.assertEqual(response.status_code, 302)

        url = response['location']
        self.assertIn('auth/login/', url)


class TestAdViews(TestCase):

    def test_displayAdHomePage_after_ad_is_created(self):
        test_user = User.objects.create_user(username="Pesho567", password='BrumDrun@123')
        sale = SaleOrRent.objects.create(name="Продажба")
        numberRooms = NumberRooms.objects.create(name="3-стаен")
        type_premise = TypePremise.objects.create(name="Апартамент")
        disctrict = District.objects.create(name="Sofia")
        city = DistrictCity.objects.create(name="Sofia", district=disctrict)
        area = DistrictCityArea.objects.create(name="Center", city=city)
        construction = Construction.objects.create(name='Тухла')
        furniture = Furniture.objects.create(name='Обзаведен')
        elevator = Elevator.objects.create(name='Да')
        my_ad = Ad.objects.create(
            id=45,
            approved=True,
            rejected=False,
            comments_reject="",
            phone_number="0123456789",
            date_modified="2020-12-30",
            price=500,
            square_meters=87,
            floor=4,
            total_floors=8,
            built_date="",
            description="Отдавам прекрасен апартамен в квартал Редута . Идеален за семейства. Само за дългосрочни наематели.",
            created_by=test_user,
            sale_or_rent=sale,
            district=disctrict,
            city=city,
            area=area,
            type_premise=type_premise,
            construction=construction,
            number_rooms=numberRooms,
            furniture=furniture,
            elevator=elevator
        )
        client = Client()
        client.login(username="Pesho567", password='BrumDrun@123')
        my_ad.save()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, my_ad.description)

    def test_ad_NOT_created_when_Not_LoggedIn(self):
        test_user = User.objects.create_user(username="Pesho567", password='BrumDrun@123')
        client = Client()
        response = client.get('/create_ad/')
        current_user = response.wsgi_request.user
        sale = SaleOrRent.objects.create(name="Продажба")
        numberRooms = NumberRooms.objects.create(name="3-стаен")
        type_premise = TypePremise.objects.create(name="Апартамент")
        disctrict = District.objects.create(name="Sofia")
        city = DistrictCity.objects.create(name="Sofia", district=disctrict)
        area = DistrictCityArea.objects.create(name="Center", city=city)
        construction = Construction.objects.create(name='Тухла')
        furniture = Furniture.objects.create(name='Обзаведен')
        elevator = Elevator.objects.create(name='Да')
        with self.assertRaises(ValueError) as ex:
            my_ad = Ad.objects.create(
                id=45,
                approved=True,
                rejected=False,
                comments_reject='',
                phone_number="0123456789",
                date_modified="2020-12-30",
                price=500,
                square_meters=87,
                floor=4,
                total_floors=8,
                built_date="",
                description="Отдавам прекрасен апартамен в квартал Редута . Идеален за семейства. Само за дългосрочни наематели.",
                created_by=current_user,
                sale_or_rent=sale,
                district=disctrict,
                city=city,
                area=area,
                type_premise=type_premise,
                construction=construction,
                number_rooms=numberRooms,
                furniture=furniture,
                elevator=elevator
            )
        self.assertIsNotNone(ex)

    def test_ad_details_page_loaded(self):
        test_user = User.objects.create_user(username="Pesho567", password='BrumDrun@123')
        sale = SaleOrRent.objects.create(name="Продажба")
        numberRooms = NumberRooms.objects.create(name="3-стаен")
        type_premise = TypePremise.objects.create(name="Апартамент")
        disctrict = District.objects.create(name="Sofia")
        city = DistrictCity.objects.create(name="Sofia", district=disctrict)
        area = DistrictCityArea.objects.create(name="Center", city=city)
        construction = Construction.objects.create(name='Тухла')
        furniture = Furniture.objects.create(name='Обзаведен')
        elevator = Elevator.objects.create(name='Да')
        my_ad = Ad.objects.create(
            id=45,
            approved=True,
            rejected=False,
            comments_reject="",
            phone_number="0123456789",
            date_modified="2020-12-30",
            price=500,
            square_meters=87,
            floor=4,
            total_floors=8,
            built_date="",
            description="Отдавам прекрасен апартамен в квартал Редута . Идеален за семейства. Само за дългосрочни наематели.",
            created_by=test_user,
            sale_or_rent=sale,
            district=disctrict,
            city=city,
            area=area,
            type_premise=type_premise,
            construction=construction,
            number_rooms=numberRooms,
            furniture=furniture,
            elevator=elevator
        )
        client = Client()
        my_ad.save()
        response = client.get('/details/'+f'{my_ad.id}/')
        self.assertEqual(response.status_code, 200)
        url = response.wsgi_request.path
        self.assertEqual('/details/'+f'{my_ad.id}/', url)
        self.assertContains(response, my_ad.description)





