package com.kk.thread.sync;

public class SingleMan {

    private static volatile SingleMan instance;

    public SingleMan() {
    }

    public static SingleMan getInstance(){
        if (instance == null) {
            synchronized (SingleMan.class) {
                if (instance == null) {
                    instance = new SingleMan();
                }
            }
        }

        return instance;
    }
}
