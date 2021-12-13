package com.smoothstack.microservice_bookings.controller;

import com.smoothstack.microservice_bookings.model.Booking;
import com.smoothstack.microservice_bookings.service.BookingService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(path = "/utopia/booking")
public class BookingController {

    @Autowired
    private BookingService bookingService;

    @GetMapping(path = "/{booking_id}")
    public Booking getById(@PathVariable int booking_id) {
        return bookingService.getById(booking_id);
    }

    @GetMapping(path = "/all")
    public List<Booking> getAllTypes() {
        return bookingService.getAllBookings();
    }

    @PostMapping(path = "/upload")
    public boolean insertType(@RequestBody Booking booking) {
        return bookingService.insertBooking(booking);
    }

    @PostMapping(path = "/delete")
    public boolean delete(@RequestBody Booking booking) {
        return bookingService.deleteBooking(booking);
    }

    @PostMapping(path = "/delete/{booking_id}")
    public boolean delete(@PathVariable int booking_id) {
        return bookingService.deleteBooking(booking_id);
    }
}
