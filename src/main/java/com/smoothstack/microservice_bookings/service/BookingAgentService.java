package com.smoothstack.microservice_bookings.service;

import com.smoothstack.microservice_bookings.dao.BookingAgentDAO;
import com.smoothstack.microservice_bookings.model.BookingAgent;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BookingAgentService {

    @Autowired
    private BookingAgentDAO bookingAgentDao;


    public BookingAgent getById(int agent_id) {
        try {
            return bookingAgentDao.findById(agent_id).get();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return new BookingAgent();
    }

    public List<BookingAgent> getAllTypes() {
        return bookingAgentDao.findAll();
    }

    public boolean insertBookingAgent(BookingAgent bookingAgent) {
        try {
            bookingAgentDao.save(bookingAgent);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean deleteBookingAgent(BookingAgent bookingAgent) {
        try {
            bookingAgentDao.delete(bookingAgent);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean deleteBookingAgent(int agent_id) {
        try {
            bookingAgentDao.deleteById(agent_id);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }
}
