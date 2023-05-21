from deneme import chard,clover, dataset,datasetAn,replace,display,null,delete


class Program:
    def __init__(self,ad):
        self.ad=ad
        self.app=True
        self.crop_name = None
        self.crop_data = None
    def hadi(self):
        self.men()
    def men(self):
       liste ={1:("Chard",chard),2:("Clover",clover)}
       while True:

        print("Please choose the crop that you want to evaluate")
        for k,v in liste.items():
            print(f"{k} -  {v[0]}") 
        print("3 -  See the last updated graph of root data")  
        print("4 -  Exit")  

        try:
         userinput=int(input("""  Please enter what you would like to do \n  """))
        except ValueError:
          print("Please enter adam gibi")
          continue
        if(userinput==3):
           display()
           break
        if(userinput==4):
           exit()

        self.crop_name, self.crop_data = liste[userinput] 
      
        while True:  
            print(f"\nWhat would you like to do on database of {self.crop_name}?")
            print("1 - See all values")
            print("2 - Analyze data")
            print("3 - Add a value to database")
            print("4 - Delete a value from database")
            print("5 - Edit data")
            print("6 - See the null data and fix it")
            print(f"7 - See the different treatments of {self.crop_name}")
            print("8 - Go to main menu")
            print("9 - Exit")
    
            try:
                user=int(input("Enter"))
                if user not in range (1,10):
                    print("Invalid input. Please enter a number between 1 and 9.")  # If user input is not valid, ask again and continue loop
                    continue
            except ValueError:
                print("Invalid input. Please enter an integer.")  # If user input is not valid, ask again and continue loop
                continue

            if(user==1):
                self.selectedData()
            if(user==2):
                self.selectedDataAnaly()    
            if(user==3): ## Add a data to dataset    
              pass 
            if(user==4): ## Delete a data to dataset    
              self.deleteData()
            if(user==5): ## Update a data to dataset    
              self.replaceData()
            if(user==6):
               self.nulldata()  
            if(user==8):
               break  
            if(user==9):
                self.exit()
    def selectedData(self):
        print(dataset(self.crop_name))
    def selectedDataAnaly(self):
        print(f"Information of data for {self.crop_name} \n")
        print(datasetAn(self.crop_name))
    def replaceData(self):
        while True:
          try:  
            potnot=int(input("Pot no"))
          except ValueError:
            print("Please Enter a intger No")  
            continue 
        
          date = input("Date: ")
          if date not in ("08Sep2022", "18Sep2022", "28Sep2022", "08Oct2022"):
                 print("Please enter a valid date")
                 continue
          try:  
            value=float(input("Deger"))
          except ValueError:
            print("Please Enter a float no")  
            continue    
          print(replace(potnot,date,value))
          break
    def nulldata(self):
       print(null(self.crop_name),f" \n Data set {self.crop_data}")   
    def deleteData(self):
          while True:
           try:  
            potnot=int(input("Pot no"))
           except ValueError:
            print("Please Enter a intger No")  
            continue 
        
           date = input("Date: ")
           if date not in ("08Sep2022", "18Sep2022", "28Sep2022", "08Oct2022"):
                 print("Please enter a valid date")
                 continue
           delete(potnot,date)
           break
    def exit(self):
        exit()    
                







deneme = Program("sen")

while deneme.app:
 deneme.hadi()   





