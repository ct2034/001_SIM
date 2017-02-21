from time import clock
import _thread

from Station import Station
from numpy import linalg as LA
from time import sleep

class Product(object):

    def __init__(self, stations=[Station()], flow=[], n_id=0):
        self.n_id = n_id
        self.stations = stations
        self.ind_flow = 0
        self.flow = flow
        self.is_finished = False
        self.t_birth = clock()
        print("Product was created")

    def start_lifecycle(self):
        #runs lifecycle as Thread
        _thread.start_new_thread(self.__start_lifecycle(), ());

    def __start_lifecycle(self):
        # als Eigenen Thread starten
        self.t_life = clock();
        # do flow here
        for i in range(0,self.flow.__len__()):
                if (i >= self.flow.__len__()-1):
                    #Produkt fährt zum Ausgang
                    self.transport_to_next_station();
                    self.is_finished = True;
                    print("Product Nr. ", self.n_id, "is finished")
                else:
                    self.transport_to_next_station()
                    self.process_Product();


        self.t_end = clock();
        print("Product Nr. ",self.n_id,"is finished")

    def process_Product(self):
        is_processed = False;
        process_time = self.flow[self.get_flow_index()][1];  # Zeit des Prozesschrittes aus Liste

        while(is_processed == False):
            source_Station = self.stations[self.flow[self.get_flow_index()]];
            if (source_Station.is_free()):
                source_Station.process_Product(process_time);
                is_processed=True;
                print("Produkt on Station",source_Station.get_name(),"was processed in ",process_time,"secs.")
            sleep(1);

    def transport_to_next_station(self):
        #Transportiere von Source nach Destination
        #flow = [stat, time]
        #Ermittle Station aus Flow List
        source_Station = self.stations[self.flow[self.get_flow_index()]];
        dest_Station = self.stations[self.flow[self.get_next_flow_index()]];
        #Ermittle Position der Station aus Stationsliste
        pos_source = source_Station.get_pos();
        pos_dest = dest_Station.get_pos();
        #Berechne Abstand zwischen Stationen = Fahrtzeit
        pos_delta =  ([pos_source[0]-pos_dest[0]],[pos_source[1]-pos_dest[1]])
        sek_sleep = LA.norm(pos_delta)

        print("Product drives",sek_sleep,"s, from "+source_Station.get_name()+" to "+dest_Station.get_name())
        sleep(sek_sleep)
        #Fzg ist am Ziel, Flusspunkt erreicht
        self.increment_flow_index();


    def is_finished(self):
        return self.is_finished;

    def get_flow_index(self):
        return self.flow_index;

    def get_next_flow_index(self):
        if (self.flow.__len__-1 >= self.ind_flow):
            return self.ind_flow;
        else:
            return  self.ind_flow+1;

    def increment_flow_index(self):
        if (self.flow.__len__-1 < self.ind_flow):
            self.ind_flow+=1;