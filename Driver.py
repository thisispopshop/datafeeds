'''
    Main Driver for Processing Data Feeds
    Created By Makena Kong June 2019
'''

import sys
import pandas as pd 
import pyodbc 

import * from Helpers
import * from Affiliates

def main():

    # get input file(s) - name.csv and name_removecsv
    # get affiliate name(directory)
    # get advertiser name (filename)

    # if neither found -> error
    # if one input file and affiliate doesn't exist in Affiliates.py-> error
    # alert me to add new affiliate script?
    
    # run correct processing function -> get output dataframe(s)
    # if given remove file
    
    # connect to db  
    # for each row in non_remove file
        # search by mid & affiliate
        # update or insert depending on existence
    # for each row in remove file 
        # search by mid & afffiliate
        # delete product 
    # close connection
    # return success or failure

    return 

if __name__ == "__main__":
    main()