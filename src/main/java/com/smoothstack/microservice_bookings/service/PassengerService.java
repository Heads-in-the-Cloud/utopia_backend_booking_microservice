package com.smoothstack.microservice_bookings.service;

import com.smoothstack.microservice_bookings.dao.PassengerDAO;
import com.smoothstack.microservice_bookings.model.Passenger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PassengerService {

    @Autowired
    PassengerDAO passengerDao;

    public Passenger getById(int passenger_id) {
        try {
            return passengerDao.findById(passenger_id).get();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return new Passenger();
    }

    public List<Passenger> getAllPassengers() {
        return passengerDao.findAll();
    }

    public boolean insertPassenger(Passenger passenger) {
        try {
            passengerDao.save(passenger);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean deletePassenger(Passenger passenger) {
        try {
            passengerDao.delete(passenger);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean deletePassenger(int passenger_id) {
        try {
            passengerDao.deleteById(passenger_id);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }
}
