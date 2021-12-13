package com.smoothstack.microservice_bookings.controller;

import com.smoothstack.microservice_bookings.model.BookingGuest;
import com.smoothstack.microservice_bookings.service.BookingGuestService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(path = "/utopia/booking_guest")
public class BookingGuestController {

    @Autowired
    private BookingGuestService bookingGuestService;

    @GetMapping(path = "/{booking_id}")
    public BookingGuest getById(@PathVariable int booking_id) {
        return bookingGuestService.getById(booking_id);
    }

    @GetMapping(path = "/all")
    public List<BookingGuest> getAllTypes() {
        return bookingGuestService.getAllBookingGuests();
    }

    @PostMapping(path = "/upload")
    public boolean insertType(@RequestBody BookingGuest booking_guest) {
        return bookingGuestService.insertBookingGuest(booking_guest);
    }

    @PostMapping(path = "/delete")
    public boolean delete(@RequestBody BookingGuest booking_guest) {
        return bookingGuestService.deleteBookingGuest(booking_guest);
    }

    @PostMapping(path = "/delete/{booking_id}")
    public boolean delete(@PathVariable int booking_id) {
        return bookingGuestService.deleteBookingGuest(booking_id);
    }
}
