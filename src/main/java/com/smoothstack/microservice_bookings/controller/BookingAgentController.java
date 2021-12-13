package com.smoothstack.microservice_bookings.controller;

import com.smoothstack.microservice_bookings.model.BookingAgent;
import com.smoothstack.microservice_bookings.service.BookingAgentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(path = "/utopia/booking_agent")
public class BookingAgentController {

    @Autowired
    private BookingAgentService bookingAgentService;

    @GetMapping(path = "/{agent_id}")
    public BookingAgent getByIataId(@PathVariable int agent_id) {
        return bookingAgentService.getById(agent_id);
    }

    @GetMapping(path = "/all")
    public List<BookingAgent> getAllTypes() {
        return bookingAgentService.getAllTypes();
    }

    @PostMapping(path = "/upload")
    public boolean insertType(@RequestBody BookingAgent bookingAgent) {
        return bookingAgentService.insertBookingAgent(bookingAgent);
    }

    @PostMapping(path = "/delete")
    public boolean delete(@RequestBody BookingAgent bookingAgent) {
        return bookingAgentService.deleteBookingAgent(bookingAgent);
    }

    @PostMapping(path = "/delete/{agent_id}")
    public boolean delete(@PathVariable int agent_id) {
        return bookingAgentService.deleteBookingAgent(agent_id);
    }
}
