from GridParameters import GridParameters



class BusAllocator:
    def __init__(self, grid_parameter: GridParameters):
        self.NetList = grid_parameter.netList
        self.FootprintList = grid_parameter.footprint_list
    def is_near(self,pad1, pad2, MaxDistance):
        dx = pad1.position.X - pad2.position.X
        dy = pad1.position.Y - pad2.position.Y
        distance = (dx**2+dy**2)**0.5
        return distance <= MaxDistance
    def FindInNet(self, pad):
        for i in range(len(self.Netlist)):
            if 



    def allocate(self):
        for i in range(len(self.FootprintList)):
            for j in range(len(self.FootprintList) - i):

