# ######################################################################################################################
# ########################################                               ###############################################
# ########################################        Restful Resources      ###############################################
# ########################################                               ###############################################
# ######################################################################################################################
from flask import request
from flask_restful import Resource, Api

from schemas import *

# ------------------------------------------------
#                   Booking
# ------------------------------------------------

class BookingResource(Resource):
    def get(self, booking_id):
        booking = Booking.query.get_or_404(booking_id)
        return booking_schema.dump(booking)


class BookingListResource(Resource):
    def get(self):
        bookings = Booking.query.all()
        return bookings_schema.dump(bookings)


class BookingCreationResource(Resource):
    def post(self):
        new_booking = Booking(
            id=request.json['booking_id'],
            is_active=request.json['is_active'],
            confirmation_code=request.json['confirmation_code']
        )
        db.session.add(new_booking)
        db.session.commit()
        return booking_schema.dump(new_booking)


class BookingPatchResource(Resource):
    def patch(self, booking_id):
        booking = Booking.query.get_or_404(booking_id)

        if 'booking_id' in request.json:
            booking.id = request.json['booking_id']
        if 'is_active' in request.json:
            booking.is_active = request.json['is_active']
        if 'confirmation_code' in request.json:
            booking.confirmation_code = request.json['confirmation_code']

        db.session.commit()
        return booking_schema.dump(booking)


class BookingDeleteResource(Resource):
    def delete(self, booking_id):
        booking = Booking.query.get_or_404(booking_id)

        db.session.delete(booking)
        db.session.commit()
        return '', 204


# ------------------------------------------------
#                   BookingGuest
# ------------------------------------------------

class BookingGuestResource(Resource):
    def get(self, booking_id):
        booking_guest = BookingGuest.query.get_or_404(booking_id)
        return booking_guest_schema.dump(booking_guest)


class BookingGuestListResource(Resource):
    def get(self):
        booking_guests = BookingGuest.query.all()
        return booking_guests_schema.dump(booking_guests)


class BookingGuestCreationResource(Resource):
    def post(self):
        new_booking_guest = BookingGuest(
            booking_id=request.json['booking_id'],
            contact_email=request.json['email'],
            contact_phone=request.json['phone']
        )
        db.session.add(new_booking_guest)
        db.session.commit()
        return booking_guest_schema.dump(new_booking_guest)


class BookingGuestPatchResource(Resource):
    def patch(self, booking_id):
        booking_guest = BookingGuest.query.get_or_404(booking_id)

        if 'booking_id' in request.json:
            booking_guest.booking_id = request.json['booking_id']
        if 'contact_email' in request.json:
            booking_guest.contact_email = request.json['contact_email']
        if 'contact_phone' in request.json:
            booking_guest.contact_phone = request.json['contact_phone']

        db.session.commit()
        return booking_guest_schema.dump(booking_guest)


class BookingGuestDeleteResource(Resource):
    def delete(self, booking_id):
        booking_guest = BookingGuest.query.get_or_404(booking_id)

        db.session.delete(booking_guest)
        db.session.commit()
        return '', 204


# ------------------------------------------------
#                   BookingPayment
# ------------------------------------------------

class BookingPaymentResource(Resource):
    def get(self, booking_id):
        booking_payment = BookingPayment.query.get_or_404(booking_id)
        return booking_guest_schema.dump(booking_payment)


class BookingPaymentListResource(Resource):
    def get(self):
        booking_payments = BookingPayment.query.all()
        return booking_payments_schema.dump(booking_payments)


class BookingPaymentCreationResource(Resource):
    def post(self):
        new_booking_payment = BookingPayment(
            booking_id=request.json['booking_id'],
            stripe_id=request.json['stripe_id'],
            refunded=request.json['refunded']
        )
        db.session.add(new_booking_payment)
        db.session.commit()
        return booking_payment_schema.dump(new_booking_payment)


class BookingPaymentPatchResource(Resource):
    def patch(self, booking_id):
        booking_payment = BookingPayment.query.get_or_404(booking_id)

        if 'booking_id' in request.json:
            booking_payment.iata_id = request.json['booking_id']
        if 'stripe_id' in request.json:
            booking_payment.contact_email = request.json['stripe_id']
        if 'refunded' in request.json:
            booking_payment.contact_phone = request.json['refunded']

        db.session.commit()
        return booking_guest_schema.dump(booking_payment)


class BookingPaymentDeleteResource(Resource):
    def delete(self, booking_id):
        booking_payment = BookingPayment.query.get_or_404(booking_id)

        db.session.delete(booking_payment)
        db.session.commit()
        return '', 204


# ------------------------------------------------
#                    Passenger
# ------------------------------------------------

class PassengerResource(Resource):
    def get(self, passenger_id):
        passenger = Passenger.query.get_or_404(passenger_id)
        return passenger_schema.dump(passenger)


class PassengerListResource(Resource):
    def get(self):
        passengers = Passenger.query.all()
        return passengers_schema.dump(passengers)


class PassengerCreationResource(Resource):
    def post(self):
        new_passenger = Passenger(
            id=request.json['passenger_id'],
            booking_id=request.json['booking_id'],
            given_name=request.json['given_name'],
            family_name=request.json['family_name'],
            dob=request.json['dob'],
            gender=request.json['gender'],
            address=request.json['address']
        )
        db.session.add(new_passenger)
        db.session.commit()
        return passenger_schema.dump(new_passenger)


class PassengerPatchResource(Resource):
    def patch(self, passenger_id):
        passenger = Passenger.query.get_or_404(passenger_id)

        if 'passenger_id' in request.json:
            passenger.id = request.json['passenger_id']
        if 'booking_id' in request.json:
            passenger.booking_id = request.json['booking_id']
        if 'given_name' in request.json:
            passenger.given_name = request.json['given_name']
        if 'family_name' in request.json:
            passenger.family_name = request.json['family_name']
        if 'dob' in request.json:
            passenger.dob = request.json['dob']
        if 'gender' in request.json:
            passenger.gender = request.json['gender']
        if 'address' in request.json:
            passenger.gender = request.json['address']

        db.session.commit()
        return passenger_schema.dump(passenger)


class PassengerDeleteResource(Resource):
    def delete(self, passenger_id):
        passenger = Passenger.query.get_or_404(passenger_id)

        db.session.delete(passenger)
        db.session.commit()
        return '', 204


# ######################################################################################################################
# ########################################                               ###############################################
# ########################################         Restful Routes        ###############################################
# ########################################                               ###############################################
# ######################################################################################################################

api = Api()

# ------------------------------------------------
#                   Booking
# ------------------------------------------------

api.add_resource(BookingResource, '/api/booking/<booking_id>')
api.add_resource(BookingListResource, '/api/booking/all')
api.add_resource(BookingCreationResource, '/api/booking/create')
api.add_resource(BookingPatchResource, '/api/booking/update/<booking_id>')
api.add_resource(BookingDeleteResource, '/api/booking/delete/<booking_id>')

# ------------------------------------------------
#                   BookingGuest
# ------------------------------------------------

api.add_resource(BookingGuestResource, '/api/booking_guest/<booking_id>')
api.add_resource(BookingGuestListResource, '/api/booking_guest/all')
api.add_resource(BookingGuestCreationResource, '/api/booking_guest/create')
api.add_resource(BookingGuestPatchResource, '/api/booking_guest/update/<booking_id>')
api.add_resource(BookingGuestDeleteResource, '/api/booking_guest/delete/<booking_id>')

# ------------------------------------------------
#                   BookingPayment
# ------------------------------------------------

api.add_resource(BookingPaymentResource, '/api/booking_payment/<booking_id>')
api.add_resource(BookingPaymentListResource, '/api/booking_payment/all')
api.add_resource(BookingPaymentCreationResource, '/api/booking_payment/create')
api.add_resource(BookingPaymentPatchResource, '/api/booking_payment/update/<booking_id>')
api.add_resource(BookingPaymentDeleteResource, '/api/booking_payment/delete/<booking_id>')

# ------------------------------------------------
#                    Passenger
# ------------------------------------------------

api.add_resource(PassengerResource, '/api/passenger/<passenger_id>')
api.add_resource(PassengerListResource, '/api/passenger/all')
api.add_resource(PassengerCreationResource, '/api/passenger/create')
api.add_resource(PassengerPatchResource, '/api/passenger/update/<passenger_id>')
api.add_resource(PassengerDeleteResource, '/api/passenger/delete/<passenger_id>')
