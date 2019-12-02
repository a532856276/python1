#!/usr/bin/env python
#coding:utf-8

import numpy as np

class InputData(object):
    def __init__(self,fileName):
        self.file = fileName
        self.Content = np.loadtxt(fname=fileName, delimiter= ",", skiprows=1)
        self.amount = np.loadtxt(fname=fileName, dtype= float, delimiter= ",", skiprows=1,usecols = (0))
        self.High = np.loadtxt(fname=fileName, dtype= float, delimiter= ",", skiprows=1,usecols = (1))
        self.Low = np.loadtxt(fname=fileName, dtype= float, delimiter= ",", skiprows=1,usecols = (2))
        self.Open = np.loadtxt(fname=fileName, dtype= float, delimiter= ",", skiprows=1,usecols = (3))
        self.Close = np.loadtxt(fname=fileName, dtype= float, delimiter= ",", skiprows=1,usecols = (4))
        self.Count = np.loadtxt(fname=fileName, dtype= float, delimiter= ",", skiprows=1,usecols = (5))
        self.Vol = np.loadtxt(fname=fileName, dtype= float, delimiter= ",", skiprows=1,usecols = (6))
        self.Id = np.loadtxt(fname=fileName, dtype=int, delimiter= ",", skiprows=1,usecols = (7))
    def getContent(self, rows = 0, cols = 0):
        return self.Content[rows][cols]

    def getOpen(self):
        return self.Content.index

    def getFileName(self):
        return self.file

    def getClose(self, rows = None, clos = None):
        if rows is not None and clos is not None:
            return self.Close[rows][clos]
        return self.Close