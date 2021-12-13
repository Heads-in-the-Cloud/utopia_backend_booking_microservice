package com.smoothstack.microservice_bookings.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "booking_guest")
public class BookingGuest {

    @Id
    @Column(name = "booking_id")
    private Integer booking_id;

    @Column(name = "contact_email")
    private String contact_email;

    @Column(name = "contact_phone")
    private String contact_phone;




    public BookingGuest() {};

    public BookingGuest(Integer booking_id, String contact_email, String contact_phone) {
        this.booking_id = booking_id;
        this.contact_email = contact_email;
        this.contact_phone = contact_phone;
    }

    public String toString() {
        return String.format("Booking ID: %d  Email: %s  Phone: %s",
                this.booking_id, this.contact_email, this.contact_phone);
    }

    public Integer getBooking_id() {
        return booking_id;
    }

    public void setBooking_id(Integer booking_id) {
        this.booking_id = booking_id;
    }

    public String getContact_email() {
        return contact_email;
    }

    public void setContact_email(String contact_email) {
        this.contact_email = contact_email;
    }

    public String getContact_phone() {
        return contact_phone;
    }

    public void setContact_phone(String contact_phone) {
        this.contact_phone = contact_phone;
    }
}
