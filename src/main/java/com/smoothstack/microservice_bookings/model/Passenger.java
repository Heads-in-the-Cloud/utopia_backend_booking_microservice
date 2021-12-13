package com.smoothstack.microservice_bookings.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import java.sql.Date;

@Entity
@Table(name = "passenger")
public class Passenger {

    @Id
    @Column(name = "id")
    private Integer id;

    @Column(name = "booking_id")
    private Integer booking_id;

    @Column(name = "given_name")
    private String given_name;

    @Column(name = "family_name")
    private String family_name;

    @Column(name = "dob")
    private Date dob;

    @Column(name = "gender")
    private String gender;

    @Column(name = "address")
    private String address;




    public Passenger() {};

    public Passenger(Integer booking_id, String given_name, String family_name,
                     Date dob, String gender, String address) {
        this.booking_id = booking_id;
        this.given_name = given_name;
        this.family_name = family_name;
        this.dob = dob;
        this.gender = gender;
        this.address = address;
    }

    public Passenger(Integer id, Integer booking_id, String given_name,
                     String family_name, Date dob, String gender, String address) {
        this.id = id;
        this.booking_id = booking_id;
        this.given_name = given_name;
        this.family_name = family_name;
        this.dob = dob;
        this.gender = gender;
        this.address = address;
    }

    public String toString() {
        return "Passenger ID: " + this.id + "    Booking ID: " + this.booking_id + "\n" +
                "Name: " + this.given_name + " " + this.family_name + "\n" +
                "DOB: " + this.dob.toString() + "    Gender: " + this.gender + "\n" +
                "Address: " + this.address;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Integer getBooking_id() {
        return booking_id;
    }

    public void setBooking_id(Integer booking_id) {
        this.booking_id = booking_id;
    }

    public String getGiven_name() {
        return given_name;
    }

    public void setGiven_name(String given_name) {
        this.given_name = given_name;
    }

    public String getFamily_name() {
        return family_name;
    }

    public void setFamily_name(String family_name) {
        this.family_name = family_name;
    }

    public Date getDob() {
        return dob;
    }

    public void setDob(Date dob) {
        this.dob = dob;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
}
