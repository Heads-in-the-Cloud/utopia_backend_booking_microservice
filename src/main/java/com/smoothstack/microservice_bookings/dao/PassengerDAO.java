package com.smoothstack.microservice_bookings.dao;

import com.smoothstack.microservice_bookings.model.Passenger;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface PassengerDAO extends JpaRepository<Passenger, Integer> {

}