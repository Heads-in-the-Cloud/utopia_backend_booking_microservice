package com.smoothstack.microservice_bookings.service;

import com.smoothstack.microservice_bookings.dao.BookingPaymentDAO;
import com.smoothstack.microservice_bookings.model.BookingPayment;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BookingPaymentService {

    @Autowired
    private BookingPaymentDAO bookingPaymentDao;

    public BookingPayment getById(int booking_id) {
        try {
            return bookingPaymentDao.findById(booking_id).get();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return new BookingPayment();
    }

    public List<BookingPayment> getAllBookingPayments() {
        return bookingPaymentDao.findAll();
    }

    public boolean insertBookingPayment(BookingPayment booking_payment) {
        try {
            bookingPaymentDao.save(booking_payment);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean deleteBookingPayment(BookingPayment booking_payment) {
        try {
            bookingPaymentDao.delete(booking_payment);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean deleteBookingPayment(int booking_id) {
        try {
            bookingPaymentDao.deleteById(booking_id);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }
}
