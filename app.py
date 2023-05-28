from functions import chard,clover, dataset,datasetAn,replace,display,null,delete,add,Mono,Pre,Same, potNoCheck


class Program:
    def __init__(self):
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
              self.adddata()
            if(user==4): ## Delete a data to dataset    
              self.deleteData()
            if(user==5): ## Update a data to dataset    
              self.replaceData()
            if(user==6):
               self.nulldata()  
            if(user==7):
               self.treatments()   
            if(user==8):
               break  
            if(user==9):
                self.exit()
    def selectedData(self): ## To show the database of selected crop
        print(dataset(self.crop_name))
    def selectedDataAnaly(self): ## To Show the data analays of selected crop
        print(f"Information of data for {self.crop_name} \n")
        print(datasetAn(self.crop_name))
    def adddata(self): ## To Add a data to selected dataset of crop
       pass
        # put=int(input("Pot"))   
        # treat=input("Treatment")
        # crop=input(self.crop_name)
        # date=input("date")
        # value= float(input("Value"))
       # print(add(26, 'Pre', 'Chard','08Sep2022', 16.5))
      
    def replaceData(self): ## To update or replace the data from selected crop dataset
        while True:
          try:  
            print(dataset(self.crop_name))
            potnot=int(input("Pot no")) 
            result = potNoCheck(self.crop_name, potnot)
            if potnot not in result:
             print(f"Please try again this pot not exist in the data set of {self.crop_name}")
             break
          except ValueError:
            print("Please Enter a intger No")  
            continue 
        
          date = input("Date: ")
          if date not in ("08Sep2022", "18Sep2022", "28Sep2022", "08Oct2022"):
                 print("Please enter a valid date \n Valid options are : 08Sep2022", "18Sep2022", "28Sep2022", "08Oct2022")
                 break
          try:  
            value=float(input("Deger"))
          except ValueError:
            print("Please Enter a float no")  
            continue    
          print(replace(potnot,date,value))
          break
    def nulldata(self): ## See the null data of selected crop
       print(null(self.crop_name),f" \n Data set {self.crop_data}")   
    def treatments(self):  ## To see the other treatment of selected crop
         while True:
          print(f"\nWhich treatment of {self.crop_name} would you like to see?")
          print("1 - Mono")
          print("2 - Same")
          print("3 - Pre")
          print("4 - Exit")
          print("5 - Upper Menü")

          try:
            user_input = int(input("User input : ")) ## user input 
          except:
             print("Try again")
             continue
          if(user_input==1):
             print(Mono(self.crop_name))
          if(user_input==2):
             print(Same(self.crop_name))
          if(user_input==3):
             print(Pre(self.crop_name))
          if(user_input==4):
             exit()
          if(user_input==5):
             break
             
    def deleteData(self):  #Delete a data from selected crop dataset
          print(dataset(self.crop_name))
          while True:
           try:  
            potnot=int(input("Pot no"))
            result = potNoCheck(self.crop_name, potnot)
            if potnot not in result:
             print(f"Please try again this pot no not exsist on the dataset of {self.crop_name} ")
             break
           except ValueError:
            print("Please Enter a intger No : ")  
            continue 
           date = input("Date: ")
           if date not in ("08Sep2022", "18Sep2022", "28Sep2022", "08Oct2022"):
              print("Please enter a valid date \n input must be one of this :\n 08Sep2022 ,  18Sep2022, 28Sep2022, 08Oct2022")
              break
                 
           delete(potnot,date)
           break
    def exit(self):
        exit()    

                
deneme = Program()

while deneme.app:
 deneme.hadi()   





