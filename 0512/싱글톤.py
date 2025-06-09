class Singleton:
    __instance = None

    @classmethod
    def getInstance(cls):
        if cls.__instance == None: cls.__instance = cls.__new__(cls)
        return cls.__instance
    
    def display(self):
        print('*************')

c1 = Singleton.getInstance()
c1.display()