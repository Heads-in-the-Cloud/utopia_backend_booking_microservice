package com.smoothstack.microservice_bookings.controller;

import com.smoothstack.microservice_bookings.model.BookingUser;
import com.smoothstack.microservice_bookings.service.BookingUserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(path = "/utopia/booking_user")
public class BookingUserController {

    @Autowired
    private BookingUserService bookingUserService;

    @GetMapping(path = "/{booking_id}")
    public BookingUser getById(@PathVariable int booking_id) {
        return bookingUserService.getById(booking_id);
    }

    @GetMapping(path = "/all")
    public List<BookingUser> getAllTypes() {
        return bookingUserService.getAllBookingUsers();
    }

    @PostMapping(path = "/upload")
    public boolean insertType(@RequestBody BookingUser booking_user) {
        return bookingUserService.insertBookingUser(booking_user);
    }

    @PostMapping(path = "/delete")
    public boolean delete(@RequestBody BookingUser booking_user) {
        return bookingUserService.deleteBookingUser(booking_user);
    }

    @PostMapping(path = "/delete/{booking_id}")
    public boolean delete(@PathVariable int booking_id) {
        return bookingUserService.deleteBookingUser(booking_id);
    }
}
