package com.kk.business;

public class TicketSeller {
    private int inventory;

    public void setInventory(int inventory) {
        this.inventory = inventory;
    }

    public int getInventory() {
        return inventory;
    }

    public void sell(int count){
        if (inventory <= count) return;
        inventory -= count;
    }

    public void refund(int count){
        inventory+=count;
    }
}
