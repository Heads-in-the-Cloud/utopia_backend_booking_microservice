# ######################################################################################################################
# ########################################                               ###############################################
# ########################################       SQLAlchemy Models       ###############################################
# ########################################                               ###############################################
# ######################################################################################################################
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base


# ------------------------------------------------
#                   Models Tables
# ------------------------------------------------

# ------------------------------------------------
#                     Bookings
# ------------------------------------------------

class Booking(Base):
    __tablename__ = "booking"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    is_active = Column(Boolean, nullable=False)
    confirmation_code = Column(String, nullable=False)


# ------------------------------------------------
#                 Booking Guest
# ------------------------------------------------


class BookingGuest(Base):
    __tablename__ = "booking_guest"

    booking_id = Column(Integer, ForeignKey("booking.id"), primary_key=True, index=True)
    contact_email = Column(String, nullable=False)
    contact_phone = Column(String)


# ------------------------------------------------
#               Booking Payments
# ------------------------------------------------



class BookingPayment(Base):
    __tablename__ = "booking_payment"

    booking_id = Column(Integer, ForeignKey("booking.id"), primary_key=True)
    stripe_id = Column(String, nullable=False)
    refunded = Column(Boolean, nullable=False, default=False)


# ------------------------------------------------
#                  Passenger
# ------------------------------------------------


class Passenger(Base):
    __tablename__ = "passenger"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    booking_id = Column(Integer, ForeignKey("booking.id"), nullable=False)
    given_name = Column(String, nullable=False)
    family_name = Column(String, nullable=False, index=True)
    dob = Column(Date, nullable=False)
    gender = Column(String, nullable=False)
    address = Column(String, nullable=False)


# # ------------------------------------------------
# #                   Association Tables
# # ------------------------------------------------
#
#
# booking_agent = Table(
#     "booking_agent",
#     metadata,
#     Column("booking_id", Integer, ForeignKey("booking.id"), primary_key=True),
#     Column("agent_id", Integer, ForeignKey("user.id"), primary_key=True)
# )
#
#
# booking_user = Table(
#     "booking_user",
#     metadata,
#     Column("booking_id", Integer, ForeignKey("booking.id"), primary_key=True),
#     Column("user_id", Integer, ForeignKey("user.id"), primary_key=True)
# )
#
#
# flight_booking = Table(
#     "flight_booking",
#     metadata,
#     Column("flight_id", Integer, ForeignKey("flight.id"), primary_key=True),
#     Column("booking_id", Integer, ForeignKey("booking.id"), primary_key=True)
# )
