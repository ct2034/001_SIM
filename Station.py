import numpy as np
from time import sleep


class Station(object):

    def __init__(self, name="Lager", pos=[0,0]):
        self.name = name;
        self.pos = pos;
        self.__is_blocked = False;

        print("Station "+name+" wurde erstellt.");

    def process_Product(self, wait_time=1):
        self.__is_blocked = True; # blocked till process is done
        if (wait_time > 360):
            print("WARNING: Wait time is higher than 360 seconds. wait_time: ",wait_time)
        if (wait_time > 0):
            sleep(wait_time);
        self.__is_blocked = False; # next Package is allowed

    def is_free(self):
        return self.__is_blocked;

    def get_pos(self):
        return self.pos;

    def get_name(self):
        return self.name;






