from django.test import TestCase
from rest_framework.test import APIClient
from .models import Booking, MenuItem

class BookingAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.booking = Booking.objects.create(first_name="John", reservation_date="2024-10-20", reservation_slot="18:00")

    def test_get_bookings(self):
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, 200)

    def test_create_booking(self):
        data = {'first_name': 'Jane', 'reservation_date': '2024-10-21', 'reservation_slot': '19:00'}
        response = self.client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, 201)
