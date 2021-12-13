package com.smoothstack.microservice_bookings.controller;


import com.smoothstack.microservice_bookings.model.FlightBooking;
import com.smoothstack.microservice_bookings.service.FlightBookingService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(path = "/utopia/flight_booking")
public class FlightBookingController {

    @Autowired
    private FlightBookingService flightBookingService;

    @GetMapping(path = "/{booking_id}")
    public FlightBooking getById(@PathVariable int booking_id) {
        return flightBookingService.getById(booking_id);
    }

    @GetMapping(path = "/all")
    public List<FlightBooking> getAllTypes() {
        return flightBookingService.getAllFlightBookings();
    }

    @PostMapping(path = "/upload")
    public boolean insertType(@RequestBody FlightBooking flight_booking) {
        return flightBookingService.insertFlightBooking(flight_booking);
    }

    @PostMapping(path = "/delete")
    public boolean delete(@RequestBody FlightBooking flight_booking) {
        return flightBookingService.deleteFlightBooking(flight_booking);
    }

    @PostMapping(path = "/delete/{booking_id}")
    public boolean delete(@PathVariable int booking_id) {
        return flightBookingService.deleteFlightBooking(booking_id);
    }
}
