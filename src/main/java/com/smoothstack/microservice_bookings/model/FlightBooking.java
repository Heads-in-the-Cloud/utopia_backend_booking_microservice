package com.smoothstack.microservice_bookings.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "flight_bookings")
public class FlightBooking {

    @Id
    @Column(name = "flight_id")
    private Integer flight_id;

    @Column(name = "booking_id")
    private Integer booking_id;




    public FlightBooking() {};

    public FlightBooking(Integer flight_id, Integer booking_id) {
        this.flight_id = flight_id;
        this.booking_id = booking_id;
    }

    public Integer getFlight_id() {
        return flight_id;
    }

    public void setFlight_id(Integer flight_id) {
        this.flight_id = flight_id;
    }

    public Integer getBooking_id() {
        return booking_id;
    }

    public void setBooking_id(Integer booking_id) {
        this.booking_id = booking_id;
    }
}
