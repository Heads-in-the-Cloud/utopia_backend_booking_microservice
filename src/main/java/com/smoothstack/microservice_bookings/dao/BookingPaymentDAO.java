package com.smoothstack.microservice_bookings.dao;

import com.smoothstack.microservice_bookings.model.BookingPayment;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface BookingPaymentDAO extends JpaRepository<BookingPayment, Integer> {

}
