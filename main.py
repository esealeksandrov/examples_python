from datetime import datetime
from time import sleep

now, timestamp = datetime.now, datetime.timestamp

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            cls.instance.__init__(*args, **kwargs)
        return cls.instance

    def __init__(self, tlm=1):
        self.tlm = tlm
        if not hasattr(self, 'index'):
            self.index = 1
            self.update_time = int(datetime.timestamp(datetime.now()))
        else:
            now = int(datetime.timestamp(datetime.now()))
            if (now - self.update_time) > self.tlm:
                self.index += 1

    def update(self):
        self.index += 1

    def init(self):
        self.index = 1


    def check_tlm(self):
        return (int(timestamp(now())) - self.update_time >= self.tlm)

    def need_update(self):
        if self.check_tlm():
            self.update()



    def get_index(self):
        return self.index


i1 = Singleton()
i2 = Singleton()
print(i1.index, i2.index)

sleep(6)
i3 = Singleton()

print(i1, i2, i3)
print(i1.index, i2.index, i3.index)