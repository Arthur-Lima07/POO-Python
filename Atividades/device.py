class NetworkDevice:
    #Construtor parametrizado
    def __init__(self, name='device', adress='192.168.0.1'):
        self.name = name
        self.adress = adress
        self.__endDevices = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_):
        if isinstance(name_, str) and len(name_) > 0:
            self.__name = name_
        else:
            raise RuntimeError('Device name must be a non-empty string')

    @property
    def adress(self):
        return self.__adress
    
    @adress.setter
    def adress(self, adress_):
        if isinstance(self.adress, str) and len(self.adress) > 0:
            self.__adress = adress_
        else:
            raise RuntimeError('Device adress must be a non-empty string')

    def add(self, endDevice):
        if isinstance(endDevice, EndDevice):
            if endDevice not in self.__endDevices:
                self.__endDevices.append(endDevice)
            else:
                raise RuntimeError('Can only add an endDevice once')
        else:
            raise RuntimeError ('Can only add EndDevices.')
    
    def add(self, endDevice):
        if isinstance(endDevice, EndDevice):
            if endDevice in self.__endDevices:
                self.__endDevices.remove(endDevice)
            else:
                raise RuntimeError('EndDevice does not belong to NetworkDevice')
        else:
            raise RuntimeError ('Can only remove EndDevices.')
    def __str__(self):
        res = f'{self.__class__.__name__} -> [name: {self.name}], [adress: {self.adress}]'
        for ed in self.__endDevices:
            res += str(ed) + '\n'
        return res

    
class EndDevice:
    #Construtor parametrizado
    def __init__(self, name='localhost', adress='127.0.0.1'):
        self.name = name
        self.adress = adress
        
    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, name_):
        if isinstance(name_, str) and len(name_) > 0:
            self.__name = name_
        else:
            raise RuntimeError('Device name must be a non-empty string')
        
    @property
    def adress(self):
        return self.__adress
            
    @adress.setter
    def adress(self, adress_):
        if isinstance(self.adress, str) and len(self.adress) > 0:
            self.__adress = adress_
        else:
            raise RuntimeError('Device adress must be a non-empty string')

    def __eq__(self, other):
        if isinstance(other, EndDevice):
            return RuntimeError ('End Device can only be compared to other EndDevice')
        else:
            return self.adress == other.adress
            
    def __str__(self):
        return f'NetworkDevice -> [name: {self.__name}], [adress: {self.__adress}]'
        

if __name__ == '__main__':
    nd1 = NetworkDevice(adress='192.168.0.2')
    print(nd1)

    nd2 = NetworkDevice(name='Switch 1')
    print(nd2)
    ed = EndDevice()
    print(ed)

    try:
        nd3 = NetworkDevice(name='')
    except RuntimeError as e:
        print(e)
    try:
        nd3 = NetworkDevice(name=1)
    except RuntimeError as e:
        print(e)

    try:
        nd3 = NetworkDevice(adress='')
    except RuntimeError as e:
        print(e)
    try:
        nd3 = NetworkDevice(adress=1)
    except RuntimeError as e:
        print(e)

    ed1 = EndDevice(adress='192.168.0.2')
    print(ed1)
    
    ed2 = EndDevice(name='Switch 1')
    print(ed2)
    ed = EndDevice()
    print(ed)
    
    try:
        ed3 = EndDevice(name='')
    except RuntimeError as e:
        print(e)
    try:
        ed3 = EndDevice(name=1)
    except RuntimeError as e:
        print(e)
    
    try:
        ed3 = EndDevice(adress='')
    except RuntimeError as e:
        print(e)
    try:
        ed3 = EndDevice(adress=1)
    except RuntimeError as e:
        print(e)

    nd1.add(ed1)
    nd1.add(ed2)
    print(nd1)
    nd1.remove(ed1)
    print(nd1)