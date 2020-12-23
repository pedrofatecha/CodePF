import pandas as pd

data=pd.read_excel('C:\\Users\\NP692MC\\Downloads\\mock data set.xlsx', sheet_name='Sheet1', encoding='UTF-8')

jsondata=[]

jsonfile= open('mock data set.json','w')
jsonfile2= open('mock data set2.json','w')

jsondata= data.to_json(orient='records')
jsondata2= data.to_json(orient='index')

jsonfile.write(jsondata)
jsonfile2.write(jsondata2)

jsondata=[]
columns= data.columns


'''
for line in data.iterrows():
    print(line[1][0])
    break

 
for line in data.iterrows():
    elements=["'%s':'%s'" % (columns[i],line[1][i]) for i in range(0,len(columns)-1)]
    print(elements)     
    row= { }
    row.append(ele for ele in elements)

'''

'''
def tabletojson(dat):
    jsondata=[]
    try:
        columns= dat.columns
    Exception ValueError:
        print("the data is not a Data Frame, make sure you are passing a data Frame 'dat'")
    for line in dat:
        elements=[columns[i]: for i in range(1,len(columns)-1) ]
         
        row= {columns[len(columns)-1] }



'''