# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 12:37:26 2021

@author: TARUN SAMANTA
"""

#Importing necessary libraries
import threading
from threading import*
import time

#I have taken an empty dictionary to store key value pair
store={}

#function for create operation
#for storing data use function call snytax: create(key,value,timout_value), Here timout is optional as per the given constraint you can also call it by passing only first two arguments

def create(key,value,timeout=0):
    #same key cannot be stores more than once
    
    if key in store:
        return ('Error: given key already exists') #error message 1
        
     #if it is a new key
    else:
        if(key.isalpha()): #given constraint that key consists of alphabets only.
            
            if(len(store)<(1024*1024*1024) and value<=(16*1024*1024)): #given constraints for file size less than 1GB and Jsonobject value must be less than 16KB
                
                if timeout==0:
                    
                    data=[value,timeout]
                else:
                    data=[value,time.time()+timeout] # current time+time_out
                    
                if len(key)<=32: #constraints for input key_name capped at 32chars
                     store[key]=data;
                     return "Data Inserted successfully"
                        
            else:
                return "error: Memory limit exceeded!!" #error message 2
                
        else:
            return "error: Invalid key_name!! key_name must consists of only alphabets and no special characters or numbers" #error message 3
                

            
# function for read operation
#To read data(key:value) from database use function call snytax: read(key)

def read(key):
    
    if(key not in store):
         return "error: given key does not exist in database. Please enter a valid key" #error message 4
    else:
        a=store[key]
        
        if(a[1]!=0):
            if time.time()<a[1]: #comparing the present time with expiry time
                s=str(key)+":"+str(a[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return s
            else:
                return "error: time-to-live of ",key," has expired" #error message5
                
        else:
            s=str(key)+":"+str(a[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
            return s
          
# function for delete operation
#To delete data from database use function call snytax: delete(key)   

def delete(key):
    if key not in store:
         return "error: given key does not exist in database. Please enter a valid key" #error message 6
    else:
        a=store[key]
        
        if(a[1]!=0):
            if time.time()<a[1]: #comparing the current time with expiry time
                del store[key]
                return "key deleted successfully"
            
            else:
                return "error: time-to-live of ",key," has expired" #error message 7
                
        else:
            
            del store[key]
            return "key deleted successfully"
        
        
