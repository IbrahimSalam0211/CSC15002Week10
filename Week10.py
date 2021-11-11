
import csv
import json

# open a csv file
csv_file = open('SalesJan2009.csv')
# create a list of dictioneries
sales_data = []
# read the csv file in rows 
csvreader = csv.reader(csv_file)
for row in csvreader:
    # creating dictionery
    dict = {'Transacion_date':row[0],
    'Product':row[1],
    'Price':row[2],
    'Payment_Type':row[3],
    'Name':row[4],
    'City':row[5],
    'State':row[6],
    'Country':row[7]
    }
    
    sales_data.append(dict)


# writing the dictionery to the json file


with open('./transaction_data.json', 'w') as fout:
    json.dump(sales_data , fout)
