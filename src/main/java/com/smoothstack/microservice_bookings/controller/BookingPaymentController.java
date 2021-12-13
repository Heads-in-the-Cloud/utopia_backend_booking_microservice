package com.smoothstack.microservice_bookings.controller;

import com.smoothstack.microservice_bookings.model.BookingPayment;
import com.smoothstack.microservice_bookings.service.BookingPaymentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(path = "/utopia/booking_payment")
public class BookingPaymentController {

    @Autowired
    private BookingPaymentService bookingPaymentService;

    @GetMapping(path = "/{booking_id}")
    public BookingPayment getById(@PathVariable int booking_id) {
        return bookingPaymentService.getById(booking_id);
    }

    @GetMapping(path = "/all")
    public List<BookingPayment> getAllTypes() {
        return bookingPaymentService.getAllBookingPayments();
    }

    @PostMapping(path = "/upload")
    public boolean insertType(@RequestBody BookingPayment booking_payment) {
        return bookingPaymentService.insertBookingPayment(booking_payment);
    }

    @PostMapping(path = "/delete")
    public boolean delete(@RequestBody BookingPayment booking_payment) {
        return bookingPaymentService.deleteBookingPayment(booking_payment);
    }

    @PostMapping(path = "/delete/{booking_id}")
    public boolean delete(@PathVariable int booking_id) {
        return bookingPaymentService.deleteBookingPayment(booking_id);
    }
}
