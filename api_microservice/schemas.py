# ######################################################################################################################
# ########################################                               ###############################################
# ########################################        Pydantic Schemas       ###############################################
# ########################################                               ###############################################
# ######################################################################################################################
import datetime
from typing import Optional

from pydantic import BaseModel


# ------------------------------------------------
#                     Bookings
# ------------------------------------------------


class Booking(BaseModel):
    is_active: bool
    confirmation_code: str


class BookingUpdate(BaseModel):
    is_active: Optional[bool] = None
    confirmation_code: Optional[str] = None


class BookingFull(Booking):
    id: int

    class Config:
        orm_mode = True


# ------------------------------------------------
#                 Booking Guest
# ------------------------------------------------


class BookingGuest(BaseModel):
    booking_id: int
    contact_email: str
    contact_phone: str

    class Config:
        orm_mode = True


class BookingGuestUpdate(BaseModel):
    booking_id: Optional[int] = None
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None


# ------------------------------------------------
#               Booking Payments
# ------------------------------------------------


class BookingPayment(BaseModel):
    booking_id: int
    stripe_id: str
    refunded: bool

    class Config:
        orm_mode = True


class BookingPaymentUpdate(BaseModel):
    booking_id: Optional[int] = None
    stripe_id: Optional[str] = None
    refunded: Optional[bool] = None


# ------------------------------------------------
#                  Passenger
# ------------------------------------------------


class Passenger(BaseModel):
    booking_id: int
    given_name: str
    family_name: str
    dob: datetime.date
    gender: str
    address: str


class PassengerUpdate(BaseModel):
    booking_id: Optional[int] = None
    given_name: Optional[str] = None
    family_name: Optional[str] = None
    dob: Optional[datetime.date] = None
    gender: Optional[str] = None
    address: Optional[str] = None


class PassengerFull(Passenger):
    id: int

    class Config:
        orm_mode = True