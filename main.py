import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def conditional(x_ob, y_ob, x_tf, y_tf): #field,

    x = []
    y = []
    f = []

    # Diámetro de campo de visiión de TAOS-II
    f_view = 1.7
    df = f_view/2

    for i, ii in zip(x_ob, y_ob):
        for j, jj in zip(x_tf, y_tf): #jjj,field,
            #cont += 1
            if j-df <= i <= j+df and jj-df <= ii <= jj+df:
                #print (iii,i,ii)
                x.append(i)
                y.append(ii)
                #f.append(jjj)
                print(i,ii)
    
    return x, y#, f

# COORDINATES OF THE CENTER OF THE FIELDS
fields = pd.read_csv('TAOS_fields.csv',header=1)

RA_fields = fields['RA_EQ_dec']
DEC_fields =  fields['Dec_EQ_dec']

# COORDINATES OF THE OBJECTS
obs = pd.read_csv('ob_positions.csv',header=0)

RA_ob = obs['RA']
DEC_ob =  obs['DEC']

# CALLING THE FUNCTION conditional
ra, dec = conditional(RA_ob, DEC_ob, RA_fields, DEC_fields)


