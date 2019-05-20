import json

from flask import Flask, render_template, request, redirect, Response, jsonify
import pandas as pd
from collections import defaultdict
import numpy as np
#First of all you have to import it from the flask module:
app = Flask(__name__)
#By default, a route only answers to GET requests. You can use the methods argument of the route() decorator to handle different HTTP methods.
@app.route("/", methods = ['POST', 'GET'])
def index():
    #df = pd.read_csv('data.csv').drop('Open', axis=1)
    global df
    global p1
    if request.method == 'POST':
        if request.form['data'] == 'loadcomp1':
            print("Reached X")
            print(request.form['name'])
            companyData = p1[p1['company'] == request.form['name']]
            print(companyData)
            finalDF = companyData.to_dict(orient='records')
            finalDF = json.dumps(finalDF, indent=2)
            data = {'plot_data': finalDF}
            return jsonify(data)
        elif request.form['data'] == 'getlevelsal':
            print("Reached level sal")
            print(request.form['name'])
            print(type(request.form['level']))
            companyData = p1[p1['company'] == request.form['name']]
            levelData = companyData[companyData['levelTagNormalized'] == np.int64(request.form['level'])]
            print(levelData)
            grp = levelData.groupby('state')
            finalList = []
            for name, group in grp:
                print(name)
                print(group['salary'])
                print(group['salary'].sum())
                print(group['salary'].count())
                sal = group['salary'].sum()/group['salary'].count()
                bonus = group['bonus'].sum()/group['bonus'].count()
                stock = group['stock'].sum()/group['stock'].count()
                temp = {"state":name,"salary":sal,"bonus":bonus,"stock":stock}
                finalList.append(temp)
            print(finalList)
            finalDF = pd.DataFrame.from_dict(finalList).to_dict(orient='records')
            finalDF = json.dumps(finalDF, indent=2)
            data = {'plot_data': finalDF}
            return jsonify(data)

    #The current request method is available by using the method attribute
    #data = df[['company','compensation']]
    print(p1['company'].unique())
    print(type(p1['company'].unique()))
    p2 = pd.DataFrame(p1['company'].unique())
    print(p2)
    chart_data = p2.to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    data = {'chart_data': chart_data}
    return render_template("index.html", data=data)

@app.route("/index.html", methods = ['POST', 'GET'])
def indexTwo():
    #df = pd.read_csv('data.csv').drop('Open', axis=1)
    global df
    #The current request method is available by using the method attribute
    data = df[['company','compensation']]
    print(type(data))
    maxSalary = defaultdict(int)
    for index, row in data.iterrows():
        if(int(maxSalary[row["company"]])<=int(row["compensation"])):
            maxSalary[row["company"]] = row["compensation"]
        #mydi[row["company"]] = row["compensation"]
    finalTable = defaultdict(int)
    cmpl = []
    compl = []
    for cmp, comp in maxSalary.items():
        cmpl.append(cmp)
        compl.append(comp)
    finalTable["company"] = cmpl
    finalTable["compensation"] = compl
    chart_data = pd.DataFrame.from_dict(finalTable).to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    data = {'chart_data': chart_data}
    return render_template("index.html", data=data)

@app.route("/page2.html", methods = ['POST', 'GET'])
def indexThree():
    #df = pd.read_csv('data.csv').drop('Open', axis=1)
    global df
    #The current request method is available by using the method attribute
    data = df[['company','compensation']]
    print(type(data))
    maxSalary = defaultdict(int)
    for index, row in data.iterrows():
        if(int(maxSalary[row["company"]])<=int(row["compensation"])):
            maxSalary[row["company"]] = row["compensation"]
        #mydi[row["company"]] = row["compensation"]
    finalTable = defaultdict(int)
    cmpl = []
    compl = []
    for cmp, comp in maxSalary.items():
        cmpl.append(cmp)
        compl.append(comp)
    finalTable["company"] = cmpl
    finalTable["compensation"] = compl
    chart_data = pd.DataFrame.from_dict(finalTable).to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    data = {'chart_data': chart_data}
    return render_template("page2.html", data=data)

@app.route("/page3.html", methods = ['POST', 'GET'])
def indexFour():
    #df = pd.read_csv('data.csv').drop('Open', axis=1)
    global df
    #The current request method is available by using the method attribute
    data = df[['company','compensation']]
    print(type(data))
    maxSalary = defaultdict(int)
    for index, row in data.iterrows():
        if(int(maxSalary[row["company"]])<=int(row["compensation"])):
            maxSalary[row["company"]] = row["compensation"]
        #mydi[row["company"]] = row["compensation"]
    finalTable = defaultdict(int)
    cmpl = []
    compl = []
    for cmp, comp in maxSalary.items():
        cmpl.append(cmp)
        compl.append(comp)
    finalTable["company"] = cmpl
    finalTable["compensation"] = compl
    chart_data = pd.DataFrame.from_dict(finalTable).to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    data = {'chart_data': chart_data}
    return render_template("page3.html", data=data)

if __name__ == "__main__":
    df = pd.read_csv('conv.csv')
    p1 = pd.read_csv('version_shweta_1.csv')
    app.run(debug=True)
