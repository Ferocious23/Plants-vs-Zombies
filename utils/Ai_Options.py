class Options():
    def __init__(self):
        self.grid_coordinates = {
            "grid1": (71, 132),
            "grid2": (154, 132),
            "grid3": (236,130),
            "grid4": (320,128),
            "grid5": (394,127),
            "grid6": (470,126),
            "grid7": (569,126),
            "grid8": (632,127),
            "grid9": (722,131),
            "grid10": (72,222),
            "grid11": (153,222),
            "grid12": (222,222),
            "grid13": (312,221),
            "grid14": (404,218),
            "grid15": (480,214),
            "grid16": (549,224),
            "grid17": (639,224),
            "grid18": (717,224),
            "grid19": (81,318),
            "grid20": (147,315),
            "grid21": (217,313),
            "grid22": (331,317),
            "grid23": (398,318),
            "grid24": (477,319),
            "grid25": (566,324),
            "grid26": (629,323),
            "grid27": (729,321),
            "grid28": (74,416),
            "grid29": (137,413),
            "grid30": (241,413),
            "grid31": (334,418),
            "grid32": (395,418),
            "grid33": (489,415),
            "grid34": (567,416),
            "grid35": (640,418),
            "grid36": (725,418),
            "grid37": (77,525),
            "grid38": (158,515),
            "grid39": (240,513),
            "grid40": (312,513),
            "grid41": (412,513),
            "grid42": (475,512),
            "grid43": (555,512),
            "grid44": (644,512),
            "grid45": (712, 514)
        }
        
        self.plant_coordinates = {
            "Sunflower": (111, 42),
            "Scary_Shooter": (167, 43),
            "Sasquatch": (223, 38),
            "Cold_Shooter": (271, 44),
            "Triplet_Shooter": (333, 43),
            "Blocker": (385, 38),
            "Chille": (439, 39),
            "Cherry": (503, 41)
        }
        
    def select_grid(self, grid_choice):
        if grid_choice in self.grid_coordinates:
            return self.grid_coordinates[grid_choice]
        else:
            raise ValueError("Invalid grid choice.")
        
    def select_plant(self, plant_choice):
        if plant_choice in self.plant_coordinates:
            return self.plant_coordinates[plant_choice]
        else:
            raise ValueError("Invalid plant choice.")
