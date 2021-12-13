package com.smoothstack.microservice_bookings.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "booking_user")
public class BookingUser {

    @Id
    @Column(name = "booking_id")
    private Integer booking_id;

    @Column(name = "user_id")
    private Integer user_id;




    public BookingUser() {};

    public BookingUser(Integer booking_id, Integer user_id) {
        this.booking_id = booking_id;
        this.user_id = user_id;
    }

    public String toString() {
        return String.format("Booking ID: %d  User ID: %d", this.booking_id, this.user_id);
    }

    public Integer getBooking_id() {
        return booking_id;
    }

    public void setBooking_id(Integer booking_id) {
        this.booking_id = booking_id;
    }

    public Integer getUser_id() {
        return user_id;
    }

    public void setUser_id(Integer user_id) {
        this.user_id = user_id;
    }
}
