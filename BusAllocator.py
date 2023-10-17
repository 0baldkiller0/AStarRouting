from GridParameters import GridParameters



class BusAllocator:
    def __init__(self, clearance, trackwidth, grid_parameter: GridParameters):
        self.NetList = grid_parameter.netList
        self.FootprintList = grid_parameter.footprint_list
        self.clearance = clearance
        self.trackwidth = trackwidth
        self.BusList = []
    def is_near(self,pad1, pad2, MaxDistance):
        dx = pad1.position.X - pad2.position.X
        dy = pad1.position.Y - pad2.position.Y
        distance = (dx**2+dy**2)**0.5
        return distance <= MaxDistance
    def GenerateMultipadFPList(self):
        MultipadFPList = []
        for i in range(len(self.FootprintList)):
            if len(self.FootprintList[i].pads) > 2:
                MultipadFPList.append(self.FootprintList[i])
        return MultipadFPList


    def FindInNet(self, pad):
        for i in range(len(self.Netlist)):
            if 
    
    def NetsInFP(self, footprint):
        PadAndNet = []
        for pad in footprint.pads:
            PadAndNet.append((pad, pad.net.number))
        return PadAndNet




    def allocate(self):
        """
        1. add Footprint with over 2 pads to MFPList
        2. search each Footprint pair to find the same net number
        3. if there are over 2 nets between Footprint pair ,record pads and set Bus parameters
        """

        MFPList=self.GenerateMultipadFPList()
#        StartBusPins = []
#        EndBusPins = []
#        BusWidth = 0
        BusID = 0

        for i in range(len(MFPList)-1):
            PadNet1 = self.NetsInFP(MFPList[i])
            for j in range(len(MFPList)-1-i):
                StartBusPins_temp = []
                EndBusPins_temp = []
                BusWidth_temp = 0
                count = 0

                PadNet2 = self.NetsInFP(MFPList[j])
#                for pad in MFPList[i].pads:
#                    if pad.net in

                for m in range(len(PadNet1) - 1):
                    net1 = PadNet1[m][1]
                    for n in  range(len(PadNet2) - 1):
                        net2 = PadNet2[n][1]
                        if net1 == net2 :
                            StartBusPins_temp.append(PadNet1[m][0])
                            EndBusPins_temp.append(PadNet2[n][0])
                            BusWidth_temp += self.clearance + self.trackwidth
                            count +=1
            if count >= 2:
                start_x = 
                start_y =
                end_x = 
                end_y = 
                Bus_start = 
                Bus_end =
                BusWidth = 
                BusID = 
                self.BusList.append((BusID, Bus_start, Bus_end, BusWidth))

                    
                



