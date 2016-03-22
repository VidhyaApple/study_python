class AthleteList(list):
	def __init__(self,name,dob=None,times=[]):
		self.name=name
		self.dob=dob
		self.extend(times)
	def top3(self):
		return(sorted(set([sanitize_own(t) for t in self ]))[0:3])


	
def sanitize_own(time):
	if "-" in time:
		(mins,secs)=time.split("-")
		return(mins+"."+secs)
	elif ":" in time:
		(mins,secs)=time.split(":")
		return(mins+"."+secs)
	else: return(time)
