package com.smoothstack.microservice_bookings.dao;

import com.smoothstack.microservice_bookings.model.BookingAgent;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface BookingAgentDAO extends JpaRepository<BookingAgent, Integer> {

}
