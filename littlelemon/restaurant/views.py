from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Booking, MenuItem
from .serializers import BookingSerializer, MenuItemSerializer

@csrf_exempt
def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Проверка на дублирование брони
            reservation_date = form.cleaned_data['reservation_date']
            reservation_slot = form.cleaned_data['reservation_slot']
            if Booking.objects.filter(reservation_date=reservation_date, reservation_slot=reservation_slot).exists():
                return JsonResponse({'error': 'This time slot is already booked.'})
            form.save()
            return JsonResponse({'success': 'Booking created successfully!'})
    else:
        form = BookingForm()

    return render(request, 'restaurant/booking.html', {'form': form})

def bookings_api(request):
    date = request.GET.get('date')
    if date:
        bookings = Booking.objects.filter(reservation_date=date)
    else:
        bookings = Booking.objects.all()

    if not bookings:
        return JsonResponse({"message": "No Booking"}, safe=False)

    data = [{"first_name": b.first_name, "reservation_date": b.reservation_date, "reservation_slot": b.reservation_slot} for b in bookings]
    return JsonResponse(data, safe=False)



class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]


