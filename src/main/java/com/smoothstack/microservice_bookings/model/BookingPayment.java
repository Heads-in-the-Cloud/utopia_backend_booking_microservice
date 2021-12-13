package com.smoothstack.microservice_bookings.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "booking_payment")
public class BookingPayment {

    @Id
    @Column(name = "booking_id")
    private Integer booking_id;

    @Column(name = "stripe_id")
    private String stripe_id;

    @Column(name = "refunded")
    private boolean refunded;




    public BookingPayment() {};

    public BookingPayment(String stripe_id, boolean refunded) {
        this.stripe_id = stripe_id;
        this.refunded = refunded;
    }

    public BookingPayment(Integer booking_id, String stripe_id, boolean refunded) {
        this.booking_id = booking_id;
        this.stripe_id = stripe_id;
        this.refunded = refunded;
    }

    public Integer getBooking_id() {
        return booking_id;
    }

    public void setBooking_id(Integer booking_id) {
        this.booking_id = booking_id;
    }

    public String getStripe_id() {
        return stripe_id;
    }

    public void setStripe_id(String stripe_id) {
        this.stripe_id = stripe_id;
    }

    public boolean isRefunded() {
        return refunded;
    }

    public void setRefunded(boolean refunded) {
        this.refunded = refunded;
    }
}
