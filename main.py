#!/usr/bin/python

#Klassischer Aufbau: Imports, Definitionen, Ausführung
from time import clock
from time import sleep
from numpy import linalg as LA
#Eigene importe
from Station import Station
from Product import Product

import numpy as np


class Transport_Handler(object):
    stations = [["Lager", np.array([0, 0])],
                ["Station1", np.array([0, 2])],
                ["Station2", np.array([3, 0])],
                ["Station3", np.array([6, 0])],
                ["Station4", np.array([4, 5])],
                ["Ausgang", np.array([6, 6])]];
    flow = [[0, 2],
            [4, 3],
            [3, 1],
            [2, 4],
            [1, 5]];


    def __init__(self, n_products=10):
        self.n_products = n_products;
        self.lade_Listen();

    def lade_Listen(self):
        # Import Stations, flow and Products from XML
        # If File exists
        if (True):
            pass
        else:
            stations = [[Station("Lager",[0,0])],
                        [Station("Trennen",[0,2])],
                        [Station("Bohren",[2,0])],
                        [Station("Fuegen",[5,2])],
                        [Station("Schweißen",[7,3])],
                        [Station("Polieren",[5,4])],
                        [Station("Ausgang",[6,6])],
                        ];

    def transport_product(self):
        pass


    def start(n=1):
        print("Simulation startet:")
        t_start = clock()



        t_end = clock()
        t_dt = t_end - t_start
        print("Der Vorgang mit",n,"Produkten dauerte",t_dt,"sekunden.")

    def transport_Product(source=["Station1", np.array([1,0])],destination=["Station2", np.array([0,4])]):
        #Transportiere von Source nach Destination
        pos_source = source[1]
        pos_dest = destination[1]
        pos_delta =  ([pos_source[0]-pos_dest[0]],[pos_source[1]-pos_dest[1]])
        sek_sleep = LA.norm(pos_delta)
        print("Product drives",sek_sleep,"s, from "+source[0]+" to "+destination[0])
        sleep(sek_sleep)

    def work_Product(id_station=0, work_time=0):
        #id_station = 0 - n
        print("Product now working on Station",id_station+1," and takes ",work_time,"seks.");
        sleep(work_time);


## Main
def run():
    start_object = Transport_Handler();
    start_object.start(10);



run();



