package com.kk.thread.sync;

import java.util.concurrent.atomic.AtomicReference;

public class Sync2Demo implements TaskDemo {
    private int num;
    @Override
    public void runTest() {

        new Thread(){
            @Override
            public void run() {
                for (int i = 0; i < 1_000_000; i++) {
                    count();
                }
                System.out.println("final num from 1: " + num);
            }
        }.start();

        new Thread(){
            @Override
            public void run() {
                for (int i = 0; i < 1_000_000; i++) {
                    count();
                }
                System.out.println("final num from 2: " + num);
            }
        }.start();
    }

    private synchronized void count(){
        num++;
    }
}
