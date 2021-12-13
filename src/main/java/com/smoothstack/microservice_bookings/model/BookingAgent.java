package com.smoothstack.microservice_bookings.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "booking_agent")
public class BookingAgent {

    @Id
    @Column(name = "booking_id")
    private Integer booking_id;

    @Column(name = "agent_id")
    private Integer agent_id;




    public BookingAgent() {};

    public BookingAgent(Integer booking_id, Integer agent_id) {
        this.booking_id = booking_id;
        this.agent_id = agent_id;
    }

    public String toString() {
        return String.format("Booking ID: %d   Agent ID: %d", this.booking_id, this.agent_id);
    }

    public Integer getBooking_id() {
        return booking_id;
    }

    public void setBooking_id(Integer booking_id) {
        this.booking_id = booking_id;
    }

    public Integer getAgent_id() {
        return agent_id;
    }

    public void setAgent_id(Integer agent_id) {
        this.agent_id = agent_id;
    }
}
