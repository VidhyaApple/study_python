#! /usr/local/bin/python3

import cgitb
cgitb.enable()

import athletelist_model  #to get data from model py
import yate  #to html texts
import cgi

athletes = athletelist_model.get_from_store()   #get data from pickled format

#get form data
form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value

#print html page
print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))
print(yate.header("Athlete: " + athlete_name + ", DOB: " +athletes[athlete_name].dob + "."))
	
print(yate.para("The top times for this athlete are:"))

print(yate.u_list(athletes[athlete_name].top3()))

print(yate.include_footer({"Home": "/index.html","Select another athlete": "athletelist_generate_list.py"}))
