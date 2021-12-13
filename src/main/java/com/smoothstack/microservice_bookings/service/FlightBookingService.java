package com.smoothstack.microservice_bookings.service;

import com.smoothstack.microservice_bookings.dao.FlightBookingDAO;
import com.smoothstack.microservice_bookings.model.FlightBooking;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class FlightBookingService {

    @Autowired
    FlightBookingDAO flightBookingDao;

    public FlightBooking getById(int booking_id) {
        try {
            return flightBookingDao.findById(booking_id).get();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return new FlightBooking();
    }

    public List<FlightBooking> getAllFlightBookings() {
        return flightBookingDao.findAll();
    }

    public boolean insertFlightBooking(FlightBooking flight_booking) {
        try {
            flightBookingDao.save(flight_booking);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean deleteFlightBooking(FlightBooking flight_booking) {
        try {
            flightBookingDao.delete(flight_booking);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean deleteFlightBooking(int booking_id) {
        try {
            flightBookingDao.deleteById(booking_id);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }
}
