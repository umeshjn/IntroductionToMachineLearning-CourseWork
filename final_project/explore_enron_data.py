#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("final_project_dataset.pkl", "r"))

def count_poi():
    count = 0
    for a in enron_data:
        if(enron_data[a]['poi']==True):
            count +=1
    return count
    
   
def count_salary():
    count = 0
    for a in enron_data:
        if(enron_data[a]['salary']!='NaN'):
            count +=1
    return count
    
    
def total_salary():
    total = 0
    for a in enron_data:
        if(enron_data[a]['salary']!='NaN'):
            total +=  enron_data[a]['salary']          
    return total
    
def total_salary4poi():
    total = 0
    for a in enron_data:
        if(enron_data[a]['poi']==True and enron_data[a]['salary']!='NaN'):
            total +=  enron_data[a]['salary']          
    return total
    
    
def count_bonus():
    count = 0
    for a in enron_data:
        if(enron_data[a]['bonus']!='NaN'):
            count +=1
    return count
    
def total_bonus():
    total = 0
    for a in enron_data:
        if(enron_data[a]['bonus']!='NaN'):
            total +=  enron_data[a]['bonus']          
    return total
    
def total_bonus4poi():
    total = 0
    for a in enron_data:
        if(enron_data[a]['poi']==True and enron_data[a]['bonus']!='NaN'):
            total +=  enron_data[a]['bonus']          
    return total
    
    
def count_email():
    count = 0
    for a in enron_data:
        if(enron_data[a]['email_address']!='NaN'):
            count +=1
    return count
    
    
def count_totalpayments():
    count = 0
    for a in enron_data:
        if(enron_data[a]['total_payments']=='NaN'):
            count +=1
    return count
    
def check_totalpayments4poi():
    count = 0
    for a in enron_data:
        if(enron_data[a]['poi']==True and enron_data[a]['total_payments']=='NaN'):
            count +=1
    return count
    
    
def check_stocks4poi():
    count = 0
    for a in enron_data:
        if(enron_data[a]['poi']==True and enron_data[a]['total_stock_value']=='NaN'):
            count +=1
    return count
    
def total_stocks():
    total = 0
    for a in enron_data:
        if(enron_data[a]['total_stock_value']!='NaN'):
            total +=  enron_data[a]['total_stock_value']
    return total
    
def total_stocks4poi():
    total = 0
    for a in enron_data:
        if(enron_data[a]['poi']==True and enron_data[a]['total_stock_value']!='NaN'):
            total +=  enron_data[a]['total_stock_value']
    return total
    
def check_stocks():
    count = 0
    for a in enron_data:
        if(enron_data[a]['total_stock_value']=='NaN'):
            count +=1
    return count
    
   
print len(enron_data)
print "Count POI::",count_poi()
print "Count Salary::",count_salary()
print "Total Salary::",total_salary()
print "Total Salary 4 POI::",total_salary4poi()
print "Count Bonus::",count_bonus()
print "Total Bonus::",total_bonus()
print "Total Bonus 4 POI::",total_bonus4poi()
print "Count email::",count_email()
print "Count total payments::",count_totalpayments()
print "Check total payments for poi::",check_totalpayments4poi()
print "Check total stocks value for poi::",check_stocks4poi()
print "Check stocks::",check_stocks()
print "Total stocks::",total_stocks()
print "Total stocks 4 POI::",total_stocks4poi()
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']



