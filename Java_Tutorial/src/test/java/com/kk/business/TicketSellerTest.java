package com.kk.business;

import org.junit.jupiter.api.*;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("售票器类型测试")
class TicketSellerTest {

    private TicketSeller ticketSeller;

    /**
     * 定义在整个测试类开始前执行的操作
     * 通常包括全局和外部资源（包括测试桩）的创建和初始化
     */
    @BeforeAll
    public static void init(){
        // ...
    }

    /**
     * 定义整个测试类完成后执行的操作
     * 通常包括全局和外部资源的释放和销毁
     */
    @AfterAll
    public static void cleanup(){
        // ...
    }

    /**
     * 定义在每个测试用例开始前执行的操作
     * 通常包括基础数据和运行环境的准备
     */
    @BeforeEach
    public void create(){
        this.ticketSeller = new TicketSeller();
        // ...
    }

    /**
     * 定义在每个测试用例完成后执行的操作
     * 通常包括运行环境的清理
     */
    @AfterEach
    public void destroy(){
        //...
    }

    /**
     * 测试用例，当车票售出后余票应该减少
     */
    @Test
    @DisplayName("售票后余票应减少")
    public void shouldReduceInventoryWhenTicketSoldOut(){
        ticketSeller.setInventory(10);
        ticketSeller.sell(1);
        assertEquals(9, ticketSeller.getInventory());
    }
}