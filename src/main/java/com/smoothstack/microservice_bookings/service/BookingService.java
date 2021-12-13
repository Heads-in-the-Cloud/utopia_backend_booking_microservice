package com.smoothstack.microservice_bookings.service;

import com.smoothstack.microservice_bookings.dao.BookingDAO;
import com.smoothstack.microservice_bookings.model.Booking;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BookingService {

    @Autowired
    private BookingDAO bookingDao;

    public Booking getById(int booking_id) {
        try {
            return bookingDao.findById(booking_id).get();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return new Booking();
    }

    public List<Booking> getAllBookings() {
        return bookingDao.findAll();
    }

    public boolean insertBooking(Booking booking) {
        try {
            bookingDao.save(booking);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean deleteBooking(Booking booking) {
        try {
            bookingDao.delete(booking);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean deleteBooking(int booking_id) {
        try {
            bookingDao.deleteById(booking_id);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }
}
