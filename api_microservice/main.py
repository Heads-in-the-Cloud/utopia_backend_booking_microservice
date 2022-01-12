# ######################################################################################################################
# ########################################                               ###############################################
# ########################################              Main             ###############################################
# ########################################                               ###############################################
# ######################################################################################################################
import datetime
from typing import List

from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session

from .database import engine
from . import (
    models as m,
    schemas as s
)

m.Base.metadata.create_all(bind=engine)

app = FastAPI()


# ######################################################################################################################
# ########################################                               ###############################################
# ########################################          API Routes           ###############################################
# ########################################                               ###############################################
# ######################################################################################################################


@app.get("/health")
def health_check():
    return "Healthy"


# ------------------------------------------------
#                     Bookings
# ------------------------------------------------

# --------------------  Create  ------------------


@app.post("/api/v2/bookings/", response_model=s.BookingFull)
def create_booking(confirm_code: str):
    with Session(engine) as db:
        db_booking = get_booking_by_conf(confirm_code)

        if db_booking:
            raise HTTPException(
                status_code=400,
                detail="A booking with that confirmation code already exists"
            )

        booking = m.Booking(
            confirmation_code=confirm_code,
            is_active=True
        )

        db.add(booking)
        db.commit()
        db.refresh(booking)

        return booking


# --------------------   Read   ------------------


@app.get("/api/v2/bookings/{booking_id}", response_model=s.BookingFull)
def get_booking(booking_id: int):
    with Session(engine) as db:
        db_booking = db                             \
            .query(m.Booking)                       \
            .filter(m.Booking.id == booking_id)    \
            .first()

        if not db_booking:
            raise HTTPException(
                status_code=404,
                detail="Booking not found"
            )

        return db_booking


@app.get("/api/v2/bookings/conf_code={conf_code}", response_model=s.BookingFull)
def get_booking_by_conf(conf_code):
    with Session(engine) as db:
        db_booking = db                                         \
            .query(m.Booking)                                   \
            .filter(m.Booking.confirmation_code == conf_code)   \
            .first()

        if not db_booking:
            raise HTTPException(
                status_code=404,
                detail="Booking not found"
            )

        return db_booking


@app.get("/api/v2/bookings/", response_model=List[s.BookingFull])
def get_bookings():
    with Session(engine) as db:
        db_bookings = db            \
            .query(m.Booking)       \
            .all()

        if not db_bookings:
            raise HTTPException(
                status_code=404,
                detail="No bookings found"
            )

        return db_bookings


@app.get("/api/v2/bookings/active/", response_model=List[s.BookingFull])
def get_active_bookings():
    with Session(engine) as db:
        active_bookings = db                \
            .query(m.Booking)               \
            .filter(m.Booking.is_active)    \
            .all()

        if not active_bookings:
            raise HTTPException(
                status_code=404,
                detail="No active bookings found"
            )

        return active_bookings


# --------------------  Update  ------------------


@app.patch("/api/v2/bookings/{booking_id}", response_model=s.BookingFull)
def update_booking(booking_id: int, booking: s.BookingUpdate):
    with Session(engine) as db:
        db_booking = db                             \
            .query(m.Booking)                       \
            .filter(m.Booking.id == booking_id)    \
            .first()

        if not db_booking:
            raise HTTPException(
                status_code=404,
                detail="Booking not found"
            )

        booking_data = booking.dict(exclude_unset=True)
        for key, value in booking_data.items():
            setattr(db_booking, key, value)

        db.add(db_booking)
        db.commit()
        db.refresh(db_booking)

        return db_booking


# --------------------  Delete  ------------------


@app.delete("/api/v2/bookings/{booking_id}")
def delete_booking(booking_id: int):
    with Session(engine) as db:
        db_booking = db                             \
            .query(m.Booking)                       \
            .filter(m.Booking.id == booking_id)    \
            .first()

        if not db_booking:
            raise HTTPException(
                status_code=404,
                detail="Booking not found"
            )

        db.delete(db_booking)
        db.commit()

        return {"ok": True}


# ------------------------------------------------
#                 Booking Guest
# ------------------------------------------------

# --------------------  Create  ------------------


@app.post("/api/v2/booking_guests/", response_model=s.BookingGuest)
def create_booking_guest(guest: s.BookingGuest):
    with Session(engine) as db:
        db_guest = db                                           \
            .query(m.BookingGuest)                              \
            .filter(m.BookingGuest.booking_id == guest.booking_id)    \
            .first()

        if not db_guest:
            raise HTTPException(
                status_code=404,
                detail="Booking guest not found"
            )

        if db_guest:
            raise HTTPException(
                status_code=400,
                detail="Booking guest already exists with that booking id"
            )

        guest = m.BookingGuest(
            booking_id=guest.booking_id,
            contact_email=guest.contact_email,
            contact_phone=guest.contact_phone
        )

        db.add(guest)
        db.commit()
        db.refresh(guest)

        return guest


# --------------------   Read   ------------------


@app.get("/api/v2/booking_guests/{booking_id}", response_model=s.BookingGuest)
def get_booking_guest(booking_id: int):
    with Session(engine) as db:
        db_guest = db                                           \
            .query(m.BookingGuest)                              \
            .filter(m.BookingGuest.booking_id == booking_id)    \
            .first()

        if not db_guest:
            raise HTTPException(
                status_code=404,
                detail="Booking guest not found"
            )

        return db_guest


# --------------------  Update  ------------------


@app.patch("/api/v2/booking_guests/{booking_id}", response_model=s.BookingGuest)
def update_booking_guest(booking_id: int, guest: s.BookingGuestUpdate):
    with Session(engine) as db:
        db_guest = db                                           \
            .query(m.BookingGuest)                              \
            .filter(m.BookingGuest.booking_id == booking_id)    \
            .first()

        if not db_guest:
            raise HTTPException(
                status_code=404,
                detail="Booking guest not found"
            )

        guest_data = guest.dict(exclude_unset=True)
        for key, value in guest_data:
            setattr(db_guest, key, value)

        db.add(db_guest)
        db.commit()
        db.refresh(db_guest)

        return db_guest


# --------------------  Delete  ------------------


@app.delete("/api/v2/booking_guests/{booking_id}", response_model=s.BookingGuest)
def delete_booking_guest(booking_id: int):
    with Session(engine) as db:
        db_guest = db                                           \
            .query(m.BookingGuest)                              \
            .filter(m.BookingGuest.booking_id == booking_id)    \
            .first()

        if not db_guest:
            raise HTTPException(
                status_code=404,
                detail="Booking guest not found"
            )

        db.delete(db_guest)
        db.commit()

        return {"ok": True}


# ------------------------------------------------
#                 Booking Payment
# ------------------------------------------------

# --------------------  Create  ------------------


@app.post("/api/v2/booking_payments/", response_model=s.BookingPayment)
def create_booking_payment(payment: s.BookingPayment):
    with Session(engine) as db:
        db_payment = db                                                     \
            .query(m.BookingPayment)                                        \
            .filter(m.BookingPayment.booking_id == payment.booking_id)      \
            .first()

        if db_payment:
            raise HTTPException(
                status_code=400,
                detail="Payment with that booking id already"
            )

        new_payment = m.BookingPayment(
            booking_id=payment.booking_id,
            stripe_id=payment.stripe_id,
            refunded=payment.refunded
        )

        db.add(new_payment)
        db.commit()
        db.refresh(new_payment)

        return new_payment


# --------------------   Read   ------------------


@app.get("/api/v2/booking_payments/{booking_id}", response_model=s.BookingPayment)
def get_booking_payment(booking_id: int):
    with Session(engine) as db:
        db_payment = db                                                 \
                .query(m.BookingPayment)                                \
                .filter(m.BookingPayment.booking_id == booking_id)      \
                .first()

        if not db_payment:
            raise HTTPException(
                status_code=404,
                detail="Booking payment not found"
            )


@app.get("/api/v2/booking_payments/stripe_id={stripe_id}", response_model=s.BookingPayment)
def get_booking_payment(stripe_id: str):
    with Session(engine) as db:
        db_payment = db                                                 \
                .query(m.BookingPayment)                                \
                .filter(m.BookingPayment.stripe_id == stripe_id)      \
                .first()

        if not db_payment:
            raise HTTPException(
                status_code=404,
                detail="Booking payment not found"
            )


@app.get("/api/v2/booking_payments/", response_model=List[s.BookingPayment])
def get_booking_payments():
    with Session(engine) as db:
        payments = db                   \
            .query(m.BookingPayment)    \
            .all()

        if not payments:
            raise HTTPException(
                status_code=404,
                detail="No booking payments found"
            )

        return payments


@app.get("/api/v2/booking_payments/refunded", response_model=List[s.BookingPayment])
def get_refunded_booking_payments():
    with Session(engine) as db:
        refunded_payments = db                      \
            .query(m.BookingPayment)                \
            .filter(m.BookingPayment.refunded)      \
            .all()

        if not refunded_payments:
            raise HTTPException(
                status_code=404,
                detail="No refunded booking payments found"
            )

        return refunded_payments


@app.get("/api/v2/booking_payments/active", response_model=List[s.BookingPayment])
def get_refunded_booking_payments():
    with Session(engine) as db:
        active_payments = db                        \
            .query(m.BookingPayment)                \
            .filter(not m.BookingPayment.refunded)  \
            .all()

        if not active_payments:
            raise HTTPException(
                status_code=404,
                detail="No active booking payments found"
            )

        return active_payments


# --------------------  Update  ------------------


@app.patch("/api/v2/booking_payments/{booking_id}", response_model=s.BookingPayment)
def update_booking_payment(payment: s.BookingPaymentUpdate):
    with Session(engine) as db:
        db_payment = db                                                         \
                .query(m.BookingPayment)                                        \
                .filter(m.BookingPayment.booking_id == payment.booking_id)      \
                .first()

        if not db_payment:
            raise HTTPException(
                status_code=400,
                detail="Booking payment not found"
            )

        payment_data = payment.dict(exclude_unset=True)
        for key, value in payment_data.items():
            setattr(db_payment, key, value)

        db.add(db_payment)
        db.commit()
        db.refresh(db_payment)

        return db_payment


# --------------------  Delete  ------------------


@app.delete("/api/v2/booking_payments/{booking_id}")
def delete_booking_payment(booking_id: int):
    with Session(engine) as db:
        db_payment = db                                                 \
                .query(m.BookingPayment)                                \
                .filter(m.BookingPayment.booking_id == booking_id)      \
                .first()

        if not db_payment:
            raise HTTPException(
                status_code=400,
                detail="Booking payment not found"
            )

        db.delete(db_payment)
        db.commit()

        return {"ok": True}


# ------------------------------------------------
#                  Passenger
# ------------------------------------------------

# --------------------  Create  ------------------


@app.post("/api/v2/passengers/", response_model=s.PassengerFull)
def create_passenger(passenger: s.Passenger):
    with Session(engine) as db:
        db_passenger = db \
            .query(m.Passenger) \
            .filter(m.Passenger.booking_id == passenger.booking_id) \
            .first()

        if db_passenger:
            raise HTTPException(
                status_code=400,
                detail="Passenger with that booking id already exists"
            )

        new_passenger = m.Passenger(
            passenger.booking_id,
            passenger.given_name,
            passenger.family_name,
            passenger.dob,
            passenger.gender,
            passenger.address
        )

        db.add(new_passenger)
        db.commit()
        db.refresh(new_passenger)

        return new_passenger


# --------------------   Read   ------------------


@app.get("/api/v2/passengers/{passenger_id}", response_model=s.PassengerFull)
def get_passenger(passenger_id: int):
    with Session(engine) as db:
        db_passenger = db \
            .query(m.Passenger) \
            .filter(m.Passenger.id == passenger_id) \
            .first()

        if not db_passenger:
            raise HTTPException(
                status_code=404,
                detail="Passenger not found"
            )

        return db_passenger


@app.get("/api/v2/passengers/", response_model=List[s.PassengerFull])
def get_passengers():
    with Session(engine) as db:
        passengers = db             \
            .query(m.Passenger)     \
            .all()

        if not passengers:
            raise HTTPException(
                status_code=404,
                detail="No passengers found"
            )

        return passengers


@app.get("/api/v2/passengers/booking_id={booking_id}", response_model=List[s.PassengerFull])
def get_passengers_by_family(booking_id: int):
    with Session(engine) as db:
        passengers = db                                         \
            .query(m.Passenger)                                 \
            .filter(m.Passenger.booking_id == booking_id)       \
            .all()

        if not passengers:
            raise HTTPException(
                status_code=404,
                detail="No passengers found"
            )

        return passengers


@app.get("/api/v2/passengers/family={family_name}", response_model=List[s.PassengerFull])
def get_passengers_by_family(family_name: str):
    with Session(engine) as db:
        family = db                                             \
            .query(m.Passenger)                                 \
            .filter(m.Passenger.family_name == family_name)     \
            .all()

        if not family:
            raise HTTPException(
                status_code=404,
                detail="No passengers found"
            )

        return family


@app.get("/api/v2/passengers/family={family_name}", response_model=List[s.PassengerFull])
def get_passengers_by_dob(dob: datetime.date):
    with Session(engine) as db:
        passengers = db                                     \
            .query(m.Passenger)                             \
            .filter(m.Passenger.dob == dob)                 \
            .all()

        if not passengers:
            raise HTTPException(
                status_code=404,
                detail="No passengers found"
            )

        return passengers


# --------------------  Update  ------------------


@app.get("/api/v2/passengers/{passenger_id}", response_model=s.PassengerFull)
def update_passenger(passenger_id: int, passenger: s.PassengerUpdate):
    with Session(engine) as db:
        db_passenger = db \
            .query(m.Passenger) \
            .filter(m.Passenger.id == passenger_id) \
            .first()

        if not db_passenger:
            raise HTTPException(
                status_code=404,
                detail="Passenger not found"
            )

        passenger_data = passenger.dict(exclude_unset=True)
        for key, value in passenger_data:
            setattr(db_passenger,  key, value)

        db.add(db_passenger)
        db.commit()
        db.refresh(db_passenger)

        return db_passenger


# --------------------  Delete  ------------------


@app.delete("/api/v2/passengers/{passenger_id}")
def delete_passenger(passenger_id: int):
    with Session(engine) as db:
        db_passenger = db \
            .query(m.Passenger) \
            .filter(m.Passenger.id == passenger_id) \
            .first()

        if not db_passenger:
            raise HTTPException(
                status_code=404,
                detail="Passenger not found"
            )

        db.delete(db_passenger)
        db.commit()

        return {"ok": True}
