package com.smoothstack.microservice_bookings.dao;

import com.smoothstack.microservice_bookings.model.FlightBooking;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface FlightBookingDAO extends JpaRepository<FlightBooking, Integer> {

}
