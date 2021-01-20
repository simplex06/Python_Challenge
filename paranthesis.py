#daily-python-challenge
#QUESTION:
#This is an interview question asked by Google.
#Given a string of parentheses, write a function to compute 
#the minimum number of parentheses to be removed to make 
#the string valid (i.e. each open parenthesis is eventually closed).
#For example, given the string "()())()", you should return 1. 
#Given the string ")(", you should return 2, since we must remove all of them. 

def num_parentheses(data):
    if data != data.replace('()', ''):
        data=data.replace('()', '')
        
    elif data != data.replace('{}', ''):    
        data=data.replace('{}', '')
        
    elif data != data.replace('[]', ''):    
        data=data.replace('[]', '')
    
    return len(data)
    

print(num_parentheses("{()())(]"))