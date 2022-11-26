package com.kk.thread;

import java.util.concurrent.*;

public class Main {

    public static void main(String[] args) {

//        thread();
        executor();
        threadPool();
        callable();
    }

    /**
     * 使用 Thread 类来定义工作
     */
    static void thread(){
        Thread thread = new Thread() {
            @Override
            public void run() {
                System.out.println("Thread started!");
            }
        };

        thread.start();
    }

    /**
     * 使用 Runnable 类来定义工作
     */
    static void runnable(){
        Runnable runnable = new Runnable() {
            @Override
            public void run() {
                System.out.println("Runnable started!");
            }
        };
        Thread thread = new Thread(runnable);
        thread.start();
    }

    static void executor(){
        Runnable runnable = new Runnable() {
            @Override
            public void run() {
                System.out.println("executor Runnable started!");
            }
        };
        Executor executor = Executors.newCachedThreadPool();
        executor.execute(runnable);
        executor.execute(runnable);
        executor.execute(runnable);
    }

    static void threadPool(){
        ThreadPoolExecutor threadPoolExecutor = new ThreadPoolExecutor(5, 10, 60L,
                TimeUnit.SECONDS, new SynchronousQueue<>());
        threadPoolExecutor.execute(new Runnable() {
            @Override
            public void run() {
                System.out.println("threadPool Runnable started!");
            }
        });
    }

    static void callable(){
        Callable<String> callable = new Callable<String>() {
            @Override
            public String call() throws Exception {
                try {
                    Thread.sleep(3000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }

                return "return demo!";
            }
        };
        try {
            Future<String> res = Executors.newSingleThreadExecutor().submit(callable);
            System.out.println(res.get()); // 这个方法阻塞，因此可以等着拿到数据
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (ExecutionException e) {
            e.printStackTrace();
        }
    }
}
