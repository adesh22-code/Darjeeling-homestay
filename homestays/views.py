from .models import Homestay
from django.shortcuts import render, get_object_or_404
from .forms import BookingForm


def home(request):
    homestays = Homestay.objects.all()

    return render(
        request,
        "homestays/home.html",
        {
            "homestays": homestays
        }
    )





def homestay_detail(request, id):
    homestay = get_object_or_404(Homestay, id=id)

    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():

            booking = form.save(commit=False)

            booking.homestay = homestay

            # Link booking to logged-in user
            if request.user.is_authenticated:
                booking.user = request.user

            # Validate maximum guests
            if booking.guests > homestay.max_guests:
                form.add_error(
                    "guests",
                    f"This homestay allows a maximum of {homestay.max_guests} guests."
                )

            else:
                booking.save()

                return render(
                    request,
                    "homestays/booking_success.html",
                    {
                        "booking": booking
                    }
                )

    else:
        form = BookingForm()

    return render(
        request,
        "homestays/detail.html",
        {
            "homestay": homestay,
            "form": form,
        }
    )
