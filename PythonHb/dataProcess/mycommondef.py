#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading

g_OrderBuyOpenEvent = threading.Event()  # 触发买入开仓 -- 开多线程
g_OrderSellOpenEvent = threading.Event()  # 触发卖出开仓 -- 开空线程
g_OrderBuyCloseEvent = threading.Event()  # 触发买入平仓 -- 平空线程
g_OrderSellCloseEvent = threading.Event()  # 触发卖出平仓 -- 平多线程
g_GetContraInfoEvent = threading.Event()  # 触发查询线程
g_OrderProcessByOptEvent = threading.Event()  # 触发交易线程处理

orderPriceThreadLock = threading.Lock()  # 创建订单价格线程锁
orderOptThreadLock = threading.Lock()  # 创建订单操作线程锁
orderVolnumeThreadLock = threading.Lock()  # 创建订单操作线程锁

g_OrderBuyOpenPrice = 0


def setOrderBuyOpenPrice(value):
    global g_OrderBuyOpenPrice
    g_OrderBuyOpenPrice = value


def getOrderBuyOpenPrice():
    global g_OrderBuyOpenPrice
    return g_OrderBuyOpenPrice


g_OrderSellOpenPrice = 0


def setOrderSellOpenPrice(value):
    global g_OrderSellOpenPrice
    g_OrderSellOpenPrice = value


def getOrderSellOpenPrice():
    global g_OrderSellOpenPrice
    return g_OrderSellOpenPrice


g_OrderBuyOpenFlag = False


def setOrderBuyOpenFlag(value):
    global g_OrderBuyOpenFlag
    g_OrderBuyOpenFlag = value


def getOrderBuyOpenFlag():
    global g_OrderBuyOpenFlag
    return g_OrderBuyOpenFlag


g_OrderSellOpenFlag = False


def setOrderSellOpenFlag(value):
    global g_OrderSellOpenFlag
    g_OrderSellOpenFlag = value


def getOrderSellOpenFlag():
    global g_OrderSellOpenFlag
    return g_OrderSellOpenFlag


g_BuyMaxProfit = 0.0  # 多单最大利润


def setBuyMaxProfit(value):
    global g_BuyMaxProfit
    g_BuyMaxProfit = value


def getBuyMaxProfit():
    global g_BuyMaxProfit
    return g_BuyMaxProfit


g_SellMaxProfit = 0.0  # 空单最大利润，当买入时需要配置为0，第一次查询后更新该值


def setSellMaxProfit(value):
    global g_SellMaxProfit
    g_SellMaxProfit = value


def getSellMaxProfit():
    global g_SellMaxProfit
    return g_SellMaxProfit

# g_halfOfLastKline = 0.0 #上一k线的中点

# 加入日志
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log20190928135728.txt")
handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s %(name)s:[%(levelname)s]%(message)s')
formatter = logging.Formatter('%(asctime)s [%(levelname)s]%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

g_halfOfLastKline = 0.0

def Writeinfo(content):
    global logger
    logger.info(content)

def getHalf():
    global g_halfOfLastKline
    return g_halfOfLastKline


def setHalf(value):
    global g_halfOfLastKline
    g_halfOfLastKline = value
