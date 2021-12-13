package com.smoothstack.microservice_bookings.dao;

import com.smoothstack.microservice_bookings.model.Booking;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface BookingDAO extends JpaRepository<Booking, Integer> {

}