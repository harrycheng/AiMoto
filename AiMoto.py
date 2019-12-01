import time
from threading import Thread
import random


class AiMoto():
    def start(self):
        print("my ai moto")
        moto_data = MotoData()
        check_senor_thread = CheckSenorThread(moto_data)
        check_senor_thread.start()

        process_thread = ProcessThread(moto_data)
        process_thread.start()


class CheckSenorThread(Thread):
    def __init__(self, moto_data):
        super().__init__()
        self.moto_data = moto_data

    def run(self):
        while True:
            self.moto_data.isEmergency = True if random.random() < 0.5 else False
            self.moto_data.leftTurnSignal = True if random.random() < 0.5 else False
            self.moto_data.rightTurnSignal = True if random.random() < 0.5 else False
            self.moto_data.rearEnd = True if random.random() < 0.5 else False
            # print("CheckSenorThread", time.time(), " data ", self.moto_data.getStrStaus(), end=" ")
            time.sleep(0.01);


class ProcessThread(Thread):
    def __init__(self, moto_data):
        super().__init__()
        self.moto_data = moto_data

    def run(self):
        while True:
            print("**********ProcessThread********** ", time.time(), " data ", self.moto_data.getStrStaus())
            time.sleep(1);


class MotoData():
    def __init__(self):
        self.isEmergency = False
        self.leftTurnSignal = False
        self.rightTurnSignal = False
        self.rearEnd = False

    def getStrStaus(self):
        return "{} {} {} {}".format(self.isEmergency, self.leftTurnSignal, self.rightTurnSignal, self.rearEnd)


aiMoto = AiMoto()
aiMoto.start()
