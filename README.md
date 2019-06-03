# Data Feed Scripts

## Overview
### BASH
1. Traverse Directories in /local/datafeeds
2. Get the files: name.csv, name_old.csv - If name_old.csv doesn’t exist, then skip to the script
3. Diff the files and create name_remove.csv (products to delete?)
4. Run name.csv and name_remove.csv through python script
5. Delete name_old.csv and name_delete.csv
6. Rename name.csv to name_old.csv
7. If failure, alert me somehow?
8. Repeat this daily

### PYTHON
1. Get the data feed from the directory
2. Process it by affiliate script 
3. Get cleaned file for addition
4. Connect to DB by PYDBC
5. Run and commit changes (insert, update, or delete)
6. Close connection

## Processing Affiliates
* Pandas Dataframe with the columns matching our product schema. 
    * [title,price,description,url,image,brand,gender,colors,categories,mid,affiliate]
* Return 1 on success, 0 on failure
