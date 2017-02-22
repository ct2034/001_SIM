#!/usr/bin/python

#Klassischer Aufbau: Imports, Definitionen, Ausführung
from time import clock
from time import sleep
from numpy import linalg as LA
#Eigene importe
from Station import Station
from Product import Product
import threading

import numpy as np


class Transport_Handler(object):
    stations = [];
    flow = [];
    product_list = [];

    def __init__(self, n_products=10):
        self.n_products = n_products;
        self.lade_Listen();

    def start(self,n=10):
        print("Simulation startet:")
        t_start = clock()

        for i in range(0,n):
            t = threading.Thread(target=Product, args=(self,self.stations,self.flow,i)).start();
            #self.product_list.append(t);
        sleep(0.1*n);

        #print("Product :",self.product_list)
        are_products_finished = False;
        while (are_products_finished == False):
            is_done=True;
            for prod in self.product_list:
                if (not prod.is_finished()):
                    is_done = False;
            if (is_done):
                are_products_finished = True;
                print("it's done, magic")
            sleep(0.1);

        t_end = clock()
        t_dt = t_end - t_start
        print("Der Vorgang mit",n,"Produkten dauerte",t_dt,"sekunden.")

    def register_products(self,prod=Product):
        self.product_list.append(prod);
        #print("Product was added, size:",self.product_list.__len__());

    def lade_Listen(self):
        # Import Stations, flow and Products from XML
        # If File exists
        if (False):
            pass
        else:
            self.stations = [Station("Lager",[0,0]),
                            Station("Trennen",[0,1]),
                            Station("Bohren",[1,0]),
                            Station("Fuegen",[3,2]),
                            Station("Schweißen",[6,3]),
                            Station("Polieren",[5,4]),
                            Station("Ausgang",[6,6]),
                            ];
            self.flow = [[0, 2],
                        [1, 3],
                        [2, 1],
                        [4, 4],
                        [3, 3],
                        [5, 3],
                        [6, 2]
                         ];
            print("Keine XML gefunden, lade Ersatzwerte",self.flow)

## Main
def run():
    start_object = Transport_Handler();
    start_object.start(100); # Anzahl der zu fertigenden Produkte


run();



