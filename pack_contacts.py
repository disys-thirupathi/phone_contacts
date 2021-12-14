import phonecontacts
class verification(phonecontacts.contacts):
    def __init__(self):
        self.__search = input("\nEnter number/name to search ")

    def search_val(self):
        if isinstance (self.__search,str or int):
            if type(self.__search) is str:
                if len(self.__search) >=20:
                    raise ValueError("Invalid search name")
            elif type(self.__search) is int:
                if len(str(self.__search)) != 10:
                    if self.__phone[0] != (6 or 7 or 8 or 9):
                        raise ValueError("Invalid phone number")
            
    def search(self):
        for i,j in phonecontacts.data.items():
            if self.__search == i:
            
                print("Name: \t",i,"\t")
                if type(j) is dict:
                    print("Found")
                    for x,y in j.items():
                        print(x,"\t---",y)
                        
            elif self.__search != i:
                
                if type(j) is dict:
                    for k,l in j.items():
                        if self.__search == k:
                            print (j.keys,"\n",k,"\t",l)
                            print("Found")
                        elif self.__search == l:
                            print (i)
                            print("Found")
                            for n,m in j.items():
                                print (n,"\t---",m)
            else:
                print("Not Found")

ob1 = verification()
ob1.search_val()
ob1.search()
