package com.smoothstack.microservice_bookings.dao;

import com.smoothstack.microservice_bookings.model.BookingUser;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface BookingUserDAO extends JpaRepository<BookingUser, Integer> {

}