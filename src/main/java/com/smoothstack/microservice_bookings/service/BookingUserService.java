package com.smoothstack.microservice_bookings.service;

import com.smoothstack.microservice_bookings.dao.BookingUserDAO;
import com.smoothstack.microservice_bookings.model.BookingUser;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BookingUserService {

    @Autowired
    BookingUserDAO bookingUserDao;

    public BookingUser getById(int booking_id) {
        try {
            return bookingUserDao.findById(booking_id).get();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return new BookingUser();
    }

    public List<BookingUser> getAllBookingUsers() {
        return bookingUserDao.findAll();
    }

    public boolean insertBookingUser(BookingUser booking_user) {
        try {
            bookingUserDao.save(booking_user);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean deleteBookingUser(BookingUser booking_user) {
        try {
            bookingUserDao.delete(booking_user);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean deleteBookingUser(int booking_id) {
        try {
            bookingUserDao.deleteById(booking_id);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }
}
