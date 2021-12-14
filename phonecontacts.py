data={}

class contacts:

    def __init__ (self):
        self.__a = int(input("number of contacts "))
        
    def noc_val(self):
        if isinstance(self.__a,int) == False:
            raise ValueError ("\nInvalid data\n")
        
    def data_base(self):
        for i in range(self.__a):
            print("Contact #",i+1,"\n")
            self.__first_name=input("First_name ")
            self.__last_name= input("Last_name ")
            self.__name=self.__first_name+self.__last_name
            data[self.__name]={}
            self.__phone = input("Phone_number ")
            self.__group = input("Group (Friends/family) ")
            data[self.__name]["phone"] = self.__phone
            data[self.__name]["group"] = self.__group

    def database_val(self):
        if isinstance(self.__first_name,str):
            if len(self.__first_name) >= 10:
                raise ValueError ("Firstname in string and 10 characters")
            
        if isinstance(self.__last_name,str):
            if len(self.__last_name) >= 10:
                raise ValueError ("lastname in string and 10 characters")
            

        if isinstance (self.__phone,int):
            if len(str(self.__phone)) != 10:
                if self.__phone[0] != (6 or 7 or 8 or 9):
                    raise ValueError ("Invalid phone number.")
                
        if isinstance (self.__group,str):
            if self.__group == None:
                raise ValueError ("Invalid group")
            
            
    def display(self):
        for i,k in data.items():
            print("\n",i)
            print("------------------------\n")
            if type(k) is dict:
                for j,l in k.items():
                    print(j,"\t---\t",l)

ob = contacts()
ob.noc_val()
ob.data_base()
ob.database_val()
ob.display()
