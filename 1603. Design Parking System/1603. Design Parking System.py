class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slot_status=[0]*4
        self.slot_status[1]=big
        self.slot_status[2]=medium
        self.slot_status[3]=small

        

    def addCar(self, carType: int) -> bool:
        if(self.slot_status[carType]>0):
            self.slot_status[carType]-=1
            return True
        else:
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
