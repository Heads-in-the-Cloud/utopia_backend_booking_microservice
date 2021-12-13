package com.smoothstack.microservice_bookings.service;

import com.smoothstack.microservice_bookings.dao.BookingGuestDAO;
import com.smoothstack.microservice_bookings.model.BookingGuest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BookingGuestService {

    @Autowired
    private BookingGuestDAO bookingGuestDao;

    public BookingGuest getById(int booking_id) {
        try {
            return bookingGuestDao.findById(booking_id).get();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return new BookingGuest();
    }

    public List<BookingGuest> getAllBookingGuests() {
        return bookingGuestDao.findAll();
    }

    public boolean insertBookingGuest(BookingGuest booking_guest) {
        try {
            bookingGuestDao.save(booking_guest);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean deleteBookingGuest(BookingGuest booking_guest) {
        try {
            bookingGuestDao.delete(booking_guest);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean deleteBookingGuest(int booking_id) {
        try {
            bookingGuestDao.deleteById(booking_id);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }
}
