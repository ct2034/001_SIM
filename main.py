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
    stations = [Station];
    flow = [0,0];
    product_list = [Product];

    def __init__(self, n_products=10):
        self.n_products = n_products;
        self.lade_Listen();

    def start(self,n=10):
        print("Simulation startet:")
        t_start = clock()

        for i in range(0,n):
            threading.Thread(self.create_Product(self.stations,self.flow,i)).start();
            #t1.start();
            #t1.join();

            #prod = Product(self.stations,self.flow,i);
            #self.product_list.append(prod);
            #prod.start_lifecycle();

        t_end = clock()
        t_dt = t_end - t_start
        print("Der Vorgang mit",n,"Produkten dauerte",t_dt,"sekunden.")

    def create_Product(self,stations, flow, i):
        prod = Product(self.stations, self.flow, i);
        self.product_list.append(prod);

    def lade_Listen(self):
        # Import Stations, flow and Products from XML
        # If File exists
        if (False):
            pass
        else:
            self.stations = [Station("Lager",[0,0]),
                            Station("Trennen",[0,2]),
                            Station("Bohren",[2,0]),
                            Station("Fuegen",[5,2]),
                            Station("Schweißen",[7,3]),
                            Station("Polieren",[5,4]),
                            Station("Ausgang",[6,6]),
                            ];
            self.flow = [[0, 2],
                    [4, 3],
                    [3, 1],
                    [2, 4],
                    [1, 5]];
            print("Keine XML gefunden, lade Ersatzwerte",self.flow)

## Main
def run():
    start_object = Transport_Handler();
    start_object.start(10);


run();



