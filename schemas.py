# ######################################################################################################################
# ########################################                               ###############################################
# ########################################      Marshmallow Schemas      ###############################################
# ########################################                               ###############################################
# ######################################################################################################################
from flask_marshmallow import Marshmallow
from models import *

# Initializing Marshmallow Serialization Handler
ma = Marshmallow()


class BookingSchema(ma.Schema):
    class Meta:
        fields = ("id", "is_active", "confirmation_code")
        model = Booking


booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)


class BookingGuestSchema(ma.Schema):
    class Meta:
        fields = ("booking_id", "contact_email", "contact_phone")
        model = BookingGuest


booking_guest_schema = BookingGuestSchema()
booking_guests_schema = BookingGuestSchema(many=True)


class BookingPaymentSchema(ma.Schema):
    class Meta:
        fields = ("booking_id", "stripe_id", "refunded")
        model = BookingPayment


booking_payment_schema = BookingPaymentSchema()
booking_payments_schema = BookingPaymentSchema(many=True)


class PassengerSchema(ma.Schema):
    class Meta:
        fields = ("id", "booking_id", "given_name", "family_name", "dob", "gender", "address")
        model = Passenger


passenger_schema = PassengerSchema()
passengers_schema = PassengerSchema(many=True)
