class individual:
    def __init__(self,cr1,cr2,cr3,sex):
        self.cr1 = cr1
        self.cr2 = cr2
        self.cr3 = cr3
        self.sex = sex
        
        if sex == ["X","Y"]:
            sex_name = "male"
        elif sex == ["X","X"]:
            sex_name = "female"
        
        self.sex_name = sex_name
        
    def get_sex(self):
        print(self.sex)
   
chromossome = ["ACT","CAT","GGC","GCG","ATC"]

ademir = individual(["ACT","CAT","GGC","GCG","ATC"], 
                    ["ACT","CAT","GGC","GCG","ATC"], 
                    ["ACT","CAT","GGC","GCG","ATC"], 
                    ["X","Y"])