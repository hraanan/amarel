# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:03:05 2018

@author: hraanan
"""
import numpy
import time
atoms_file=open('f:/programs/span/data/manual_cofactor_list_with_quinone_2_atoms_ADE.txt','r')
atoms_file.readline()
al_dict={}
for line in atoms_file:
    line=line.split('\t')
    if line[3]=='all':
        continue
    al_dict[line[1]]=[line[3],line[4][:-1]]

#time.sleep(5)

def get_atom_list(cof):
    if cof not in al_dict and cof[0:3]!='ADE':
        return ['all']
    ade=0 #if not ade read the first list of atoms 
    cof=cof.split('_')
    #print(cof)
    if cof[0]=='ADE':
        ade=1 #if not ade read the second list of atoms 
        cof=cof[1]
    else:
        cof=cof[0]
    
    #print(ade)
    atom_list=al_dict.get(cof)[ade]
    return atom_list.split(';')
     
    
def get_center(atom_coord_list):
    x=0
    y=0
    z=0    
        
    for atom in atom_coord_list:
        
        x=x+atom[0]
        y=y+atom[1]
        z=z+atom[2]
        
    try:
            x=x/len(atom_coord_list)
            y=y/len(atom_coord_list)
            z=z/len(atom_coord_list)
            center=numpy.array([x,y,z])
    except:
            return 'NA'   
    center=numpy.array([x,y,z])
    return center;

#test get_atom_list function

print(get_atom_list('sf4'))
print(get_atom_list('NAD'))
print(get_atom_list('ADE_FAD'))



