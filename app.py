import json

from flask import Flask, render_template, request, redirect, Response, jsonify
import pandas as pd
from collections import defaultdict
import numpy as np
import ast
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
            levelData = companyData[companyData['levelTag'] == request.form['level']]
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
            levelData = companyData[companyData['levelTag'] == request.form['level']]
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
    global p1
    if request.method == 'POST':
        if request.form['data'] == 'comp':
            print("Reached X comp")
            print(request.form['name1'])
            print((request.form['name2']))
            company1Data = p1[p1['company'] == request.form['name1']]
            company2Data = p1[p1['company'] == request.form['name2']]
            print(company1Data)
            print(company2Data)
            finalDF = pd.concat([company1Data,company2Data]).to_dict(orient='records')
            finalDF = json.dumps(finalDF, indent=2)
            data = {'plot_data': finalDF}
            return jsonify(data)
        elif request.form['data'] == 'compdata':
            print("Reached level compare data")
            company1Data = p1[p1['company'] == request.form['name1']]
            company2Data = p1[p1['company'] == request.form['name2']]
            cl1 = company1Data[company1Data['levelTag'] == request.form['level1']]
            cl2 = company2Data[company2Data['levelTag'] == request.form['level2']]
            print(cl1)
            print(cl2)
            avg1 = cl1.shape[0]
            avg2 = cl2.shape[0]
            cmp1Salary = cl1['salary'].sum() / avg1
            cmp2Salary = cl2['salary'].sum() / avg2
            cmp1Bonus = cl1['bonus'].sum() / avg1
            cmp2Bonus = cl2['bonus'].sum() / avg2
            cmp1Stock = cl1['stock'].sum() / avg1
            cmp2Stock = cl2['stock'].sum() / avg2
            print(cmp1Stock)
            compNames = json.dumps({"cmp1": request.form['name1'], "cmp2": request.form['name2']})
            levels = json.dumps({"lvl1": request.form['level1'], "lvl2": request.form['level2']})
            salaryVals = json.dumps({"sal1": cmp1Salary, "sal2": cmp2Salary})
            bonusVals = json.dumps({"bonus1": cmp1Bonus, "bonus2":cmp2Bonus })
            stockVals = json.dumps({"st1": cmp1Stock, "st2": cmp2Stock})
            ratingVals = json.dumps({"r1":int(cl1['rating'].iloc[0])*20 , "r2":int(cl2['rating'].iloc[0])*20 })
            rtfVals = json.dumps({"rt1":int(cl1['recommendToFriend'].iloc[0]),"rt2":int(cl2['recommendToFriend'].iloc[0])})
            idVals = json.dumps({"id1":int(cl1['interviewDifficulty'].iloc[0])*20, "id2":int(cl2['interviewDifficulty'].iloc[0])*20})
            cAVals = json.dumps({"ca1":int(cl1['ceoApproval'].iloc[0]), "ca2":int(cl2['ceoApproval'].iloc[0])})
            data = {'comp_data': compNames, 'levels': levels, 'sal': salaryVals, 'bonus': bonusVals, 'stock': stockVals,'rating':ratingVals,'rtf':rtfVals,'interviewdiff':idVals,'ceo':cAVals}
            return jsonify(data)
    print(p1['company'].unique())
    p2 = pd.DataFrame(p1['company'].unique())
    print(p2)
    chart_data = p2.to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    data = {'chart_data': chart_data}
    return render_template("page3.html", data=data)

if __name__ == "__main__":
    df = pd.read_csv('conv.csv')
    p1 = pd.read_csv('version_shweta_1.csv')
    app.run(debug=True)
