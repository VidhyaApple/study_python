import pickle #to store data in pickled format

from athletelist import AthleteList  #importing AthleteList class to sort and give top3 times


#put list of data files
def put_to_store(file_list): #here file_list argument is the list type
        all_athletes={}   #dictionary to store data
        
        for each_file in file_list:
                athlete_obj=get_coach_data(each_file)  #get_coach_data returns object instance of AtheleteList class
                all_athletes[athlete_obj.name]=athlete_obj

        #pickle the data
        try:
                with open("atheletes.pickle","wb") as athpic:
                        pickle.dump(all_athletes,athpic)

        except IOError as ioerr: print("File error in put to store data: "+str(ioerr))
        
        return(all_athletes)

#get list of data files
def get_from_store():
        all_athletes={}
        #get back pickle data
        try:
                with open("atheletes.pickle","rb") as athpic:
                        all_athletes=pickle.load(athpic)

        except IOError as ioerr: print("File error in get from data: "+str(ioerr))
        
        return(all_athletes)
        


#get data it uses AtheleteList class
def get_coach_data(filename):
        try:
                with open(filename)as f :
                        data=f.readline()
                temp=data.strip().split(",")
                return(AthleteList(temp.pop(0),temp.pop(0),temp))
        
        except IOError as ioerr:
                print(str(ioerr))
                return(None)

