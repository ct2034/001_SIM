#!/usr/bin/python

#Klassischer Aufbau: Imports, Definitionen, Ausführung
from time import clock
from time import sleep
from numpy import linalg as LA

import numpy as np

#stations = ["name", [x,y]];
stations = [["Lager",    np.array([0,0])],
            ["Station1", np.array([0,2])],
            ["Station2", np.array([3,0])],
            ["Station3", np.array([6,0])],
            ["Station4", np.array([4,5])],
            ["Ausgang",  np.array([6,6])]
            ];
#flow = [station, dauer [s]], [...], .. ;
flow = [[0,2],
        [4,3],
        [3,1],
        [2,4],
        [1,5]
        ];
#change

def run(n=1, stations=stations,flow=flow):
    print("Simulation startet:")
    t_start = clock()
    for x in range(0,n):
        for i in range(0,flow.__len__()):
            if (i >= flow.__len__()-1):
                transport_Product(stations[flow[i-1][0]], stations[flow[i][0]])
            else:
                transport_Product(stations[flow[i][0]], stations[flow[i+1][0]])
                work_Product(flow[i][0],flow[i][1])

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

run();



