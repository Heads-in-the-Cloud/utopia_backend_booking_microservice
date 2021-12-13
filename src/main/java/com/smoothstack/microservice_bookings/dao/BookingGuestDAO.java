package com.smoothstack.microservice_bookings.dao;

import com.smoothstack.microservice_bookings.model.BookingGuest;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface BookingGuestDAO extends JpaRepository<BookingGuest, Integer> {

}
