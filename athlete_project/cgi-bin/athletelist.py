
class AthleteList(list):

    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    @staticmethod
    def sanitize_own(time):
        if "-" in time:
            (mins,secs)=time.split("-")
            return(mins+"."+secs)
        elif ":" in time:
            (mins,secs)=time.split(":")
            return(mins+"."+secs)
        else: return(time)
        
        
    
    def top3(self):
        return(sorted(set([self.sanitize_own(t) for t in self]))[0:3])

    
    def clean_data(self):
        return(sorted(set([self.sanitize_own(t) for t in self])))
