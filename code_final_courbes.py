# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 22:28:40 2020

@author: orion
"""
#Liste de données
import pandas as pd
tableau=pd.read_csv("C:\\Users\orion\Desktop\EIVP\Projet Informatique/EIVP_KM.csv",
                    sep=';')
Tri=tableau.sort_values(by=['sent_at'])
T=list(Tri['sent_at'])
Noise=list(Tri['noise'])
Hum=list(Tri['humidity'])
Temp=list(Tri['temp'])
Lum=list(Tri['lum'])
CO2=list(Tri['co2'])
num_capteur=list(Tri['id'])
from datetime import datetime
def tri_des_dates(L):
    S=[]
    for i in range(len(L)):
        date_str=L[i]
        bonne_date=datetime.strptime(date_str,"%Y-%m-%d %H:%M:%S %z" )
        S.append(bonne_date)
    return S

date=tri_des_dates(T)

#affichage des courbes
import matplotlib.pyplot as plt
import numpy as np
def moyenne_capteur(l,id):
    m=0
    for k in range(len(l)):
        if num_capteur[k]==id:
            m+=l[k]
    return m/len(l)
def evolution_variables(date_debut,date_fin,l,t):
    i=t.index(date_debut)
    j=t.index(date_fin)
    t= t[i: j]
    l=l[i:j]
    x=np.array(t)
    y=np.array(l)
    plt.xlabel('date d\'enregistrement')
    plt.ylabel('evolution en fonction du temps')
    if num_capteur==1:
        plt.axhline(y=moyenne_capteur(l,1),color='green',
                    linestyle="--",label="moyenne capteur 1")
        plt.plot(x,y,'r-',)
        plt.title('tracé du capteur 1')
    elif num_capteur==2:
        plt.axhline(y=moyenne_capteur(l,2),color='red',
                    linestyle="--",label="moyenne capteur 2")
        plt.plot(x,y,'b-')
        plt.title('tracé du capteur 2')
    elif num_capteur==3:
        plt.axhline(y=moyenne_capteur(l,3),color='blue',
                    linestyle="--",label="moyenne capteur 3")
        plt.plot(x,y,'g-')
        plt.title('tracé du capteur 3')
    elif num_capteur==4:
        plt.axhline(y=moyenne_capteur(l,4),color='cyan'
                    ,linestyle="--",label="moyenne capteur 4")
        plt.plot(x,y,'y-')
        plt.title('tracé du capteur 4')
    elif num_capteur==5:
        plt.axhline(y=moyenne_capteur(l,5),color='magenta',
                    linestyle="--",label="moyenne capteur 5")
        plt.plot(x,y,'c-')
        plt.title('tracé du capteur 5')
    else:
        plt.axhline(y=moyenne_capteur(l,6),color='yellow',
                    linestyle="--",
                    label="moyenne capteur 6")
        plt.plot(x,y,'m-')
        plt.title('tracé du capteur 6')
    plt.legend()
    plt.show()
    return

#fonctions statistiques

def min(y):
    r=y[0]
    for i in range(len(y)):
        if r>y[i]:
            r=y[i]
    return r
def max(y):
    r=y[0]
    for i in range(len(y)):
        if r<y[i]:
            r=y[i]
    return r
def moyenne_arith(y):
    s=0
    for i in range(len(y)):
        s+=y[i]
    return s/len(y)
def variance(y):
    moy=moyenne_arith(y)
    var=0
    for i in range(len(y)):
        var+=(y[i]-moy)**2
    return var/len(y)
def ecart_type(y):
    from math import sqrt
    return sqrt(variance(y))
def moyenne_geom(y):
    s=1
    for i in range(len(y)):
        s*=y[i]
    return s**(1/len(y))

def variance2(y):
    moy=moyenne_geom(y)
    var=0
    for i in range(len(y)):
        var+=(y[i]-moy)**2
    return var/len(y)

def ecart_type2(y):
    from math import sqrt
    return sqrt(variance2(y))

def bubbleSort(a):
    b=a
    for k in range(len(a)-1):
        for i in range(len(a)-k-1):
            if b[i]>b[i+1]:
                b[i],b[i+1]=b[i+1],b[i]
    return b
def mediane(y):
    y2=bubbleSort(y)
    n=len(y)
    if n%2==0:
        med=y2[n/2]
    else:
        med=(y2[(n+1)/2]+y2[(n-1)/2])/2
    return med
def covariance(x,y):
    moyx=moyenne_arith(x)
    moyy=moyenne_arith(y)
    cov=0
    for i in range(len(x)):
        cov+=(x[i]-moyx)*(y[i]-moyy)
    return cov/len(y)
        
def covariance2(x,y):
    moyx=moyenne_geom(x)
    moyy=moyenne_geom(y)
    cov=0
    for i in range(len(x)):
        cov+=(x[i]-moyx)*(y[i]-moyy)
    return cov/len(y)

#indice de corrélation

def correlation(x,y):
    from math import sqrt
    s=covariance(x,y)/sqrt(variance(x)*variance(y))
    print(s)

def correlation2(x,y):
    from math import sqrt
    s=covariance2(x,y)/sqrt(variance2(x)*variance2(y))
    print(s)
    
    
#Similarité 

def separation_donnees(T,id):
    assert id>0 and id<7
    j=0
    while T[j]<id:
        j+=1
    if id<6:
       k=j
       while T[k]==id:
           k+=1
       k=k-1
    else:
        k=len(T)-1
    return j,k

d1,f1=separation_donnees(num_capteur,1)

def similarites(dimension,id1,id2,temps,pourcentage):
    a,b=separation_donnees(num_capteur,id1)
    c,d=separation_donnees(num_capteur,id2)
    y1=np.array(dimension[a:b])
    y2=np.array(dimension[c:d])
    t1=temps[a:b]
    t2=temps[c:d]
    x1=np.array(t1)
    x2=np.array(t2)
    plt.axhline(y=moyenne_arith(dimension[a,b]),
    linestyle="--",label="moyenne 1er capteur")
    plt.axhline(y=moyenne_arith(dimension[c,d]),linestyle="--",
    label="moyenne 2nd capteur")
    plt.xlabel('date d\enregistrement')
    plt.ylabel('evolution en fonction du temps')
    plt.plot(x1,y1,label="1er capteur")
    plt.plot(x2,y2, label="2nd capteur")
    plt.legend()
    plt.show()


#Indice humidex 

def Calcul_humidex(date_debut,date_fin,T,H,date):
    i=date.index(date_debut)
    j=date.index
    date=date[i:j]
    for k in range(len(date)):
        Hmdx=[]
        Humidex=T[k]+5/9*(6.112*10**(7.5*(T[k]/(237.7+T[k])))*H[k]/100-10)
        Hmdx.append(Humidex)
        print(Hmdx)
        print(date_debut,date_fin)
    
        
    return Hmdx
