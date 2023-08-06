# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 17:00:14 2021

@author: Sagnik.Banerje
"""
import pandas as pd


class main():
  def __init__(self):
    # Initialization of the Strings
    self.String1 =str(input("Enter your pointer scale question no. "))
    self.String2 =str(input("Enter your first demographic question "))
    self.String3= str(input("Enter your second demographic question "))



  def total_resp(self):
    proportion= df[self.String1].value_counts(normalize=True)
    total = df[self.String1].value_counts()

    d= {'Total_proportion':proportion,'Total_count':total}
    total_response_distribution = pd.DataFrame(d)
    
    tot1= total_response_distribution.loc[[df[self.String1].max()]]
    tot2= total_response_distribution.loc[[df[self.String1].min()]]

    dff_final= pd.concat([tot1,tot2], axis=0)
    dff_final.columns= ["total_proportion","total_count"]

    dff_final.to_json("total_resp.json", orient="index")

    print(dff_final)

    return



  def demo_analysis(self):
    b= pd.crosstab(df[self.String1], df[self.String2])
    c= pd.crosstab(df[self.String1], df[self.String2], normalize="columns")
    data= {"Total": b, "Percentage": c}

    dff= pd.concat(data, axis=1)

    dff.to_json("demographic_analysis.json", orient="index")

    print(dff)

    return



  def uni_demo_analysis(self):
    b= pd.crosstab(df[self.String1], df[self.String2])
    c= pd.crosstab(df[self.String1], df[self.String2], normalize="columns")
    data= {"Total": b, "Percentage": c}

    dff= pd.concat(data, axis=1)

    dff2= dff.loc[[df[self.String1].max()]]
    dff3= dff.loc[[df[self.String1].min()]]

    dff_final= pd.concat([dff2,dff3], axis=0)

    dff_final.to_json("demographic_univariate.json", orient="index")

    print(dff_final)

    return



  def bivariate_analysis(self):
    c = pd.crosstab(df[self.String1],[df[self.String2],df[self.String3]],normalize = "columns").max(axis=1)
    d = pd.crosstab(df[self.String1],[df[self.String2],df[self.String3]],normalize = "columns").idxmax(axis=1)
    e = pd.crosstab(df[self.String1],[df[self.String2],df[self.String3]]).max(axis=1)
    data = {"Percentage": c,self.String2+"_"+self.String3: d,"count":e}
    dfff = pd.concat(data,
               axis = 1)
    
    dfff.to_json("bivariate.json", orient="index")
    
    print(dfff)
    return




  def all_analysis(self):

    self.total_resp()

    self.demo_analysis()

    self.uni_demo_analysis()

    self.bivariate_analysis()

    return    