# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 14:08:29 2018

@author: hraanan
"""
print ('welcom to pymol align')
import os
import time
import numpy
import math
import __main__
import sys
import center

__main__.pymol_argv = ['pymol','-c'] # Pymol: quiet and no GUI
#from time import sleep
import pymol
pymol.finish_launching()




in_file_name=sys.argv[1]
#in_file_name='/home/hraanan/span/align_lists/align_cofactors.txt'
in_file=open(in_file_name,'r')
#print(in_file_name)
microen_dir='/scratch/hr253/span/all/'

out_file_name=in_file_name+'_out.txt' #_'+in_file_name.split('.')[1]+'.txt'
out_file=open(out_file_name,'w')              
#out_file.write('Sourec\tTarget\tSl\tTl\tLigand\tRMSD\tAlign CA\tRaw alignment score\tAligned Residues\tLigand center distance'+'\t'+'Structural Distance'+'\n')

t=0
start = time.time()    
print('start align')    
for line in in_file:
    pymol.cmd.reinitialize()
    #print(line)
    #time.sleep(.5)       
    t=t+1
    if t>1000:
        break
    line=line.split('\t')
    microen1=line[0][:-4]
    microen2=line[1][:-6]
    
    #PDB2='3cw9.01A_B_991'
    lig=line[0].split('_')[0]
    lig1=lig.split('.')[1]
    Fldr1=microen_dir+lig1+'/'
    if lig1=='ADE':
        lig1=lig1+'_'+line[0].split('_')[3][:-4]
    
    #PDB1=lig1.split('.')[0]
    
    lig=line[1].split('_')[0]
    lig2=lig.split('.')[1]
    Fldr2=microen_dir+lig2+'/'
    if lig2=='ADE':
        lig2=lig2+'_'+line[0].split('_')[3][:-4]
    #PDB2=lig2.split('.')[0]
    
    
    
    pdbFile_1=str(Fldr1)+microen1+".pdb"
    pdbFile_2=str(Fldr2)+microen2+".pdb"
    pymol.cmd.load(pdbFile_1,'PDB1')	
    pymol.cmd.load(pdbFile_2,'PDB2')
    Ql=pymol.cmd.count_atoms('PDB1 and name CA')
    Tl=pymol.cmd.count_atoms('PDB2 and name CA')
    if Ql<10 or Tl<10:
        continue
    #print('Ql,Tl:'+str(Ql)+str(Tl))
    res_num1=microen1.split('_')
    res_num2=microen2.split('_')
   
    res_num1=res_num1[2]
    res_num2=res_num2[2]             
    #print('res_num1:',res_num1)                    
    #print('res_num2:',res_num2)
   
    x=pymol.cmd.align('PDB1 and name CA','PDB2 and name CA',quiet=1)
    
    align_out=[x[0],x[1],x[5],x[6]]
    #print(align_out)
    atomlist=[]                    
    #print(lig1,lig2) 
    cof_atom_list=center.get_atom_list(lig1)
    if cof_atom_list==['all']:
        atomlist=pymol.cmd.get_model('PDB1 and resi '+res_num1, 1).get_coord_list()
    else:
        for atom in cof_atom_list:
            atomlist=atomlist+(pymol.cmd.get_model('PDB1 and resi '+res_num1+' and name '+atom, 1).get_coord_list())
    center1=center.get_center(atomlist)    
    #print(center1)       
    if center1=='NA':
            continue
    atomlist=[]                    
                            
    cof_atom_list=center.get_atom_list(lig1)
    if cof_atom_list==['all']:
        atomlist=pymol.cmd.get_model('PDB2 and resi '+res_num2, 1).get_coord_list()
    else:
        for atom in cof_atom_list:
            atomlist=atomlist+(pymol.cmd.get_model('PDB2 and resi '+res_num2+' and name '+atom, 1).get_coord_list())
    center2=center.get_center(atomlist)    
    #print(center2)         
    if center2=='NA':
            continue
    atomlist=[]             
    #print(center1,center2)
    Dis=math.sqrt((pow((center1[0]-center2[0]),2))+(pow((center1[1]-center2[1]),2))+(pow((center1[2]-center2[2]),2)))
    #print(Dis)
    if Dis>15:
        #print('large distance')
        continue
    #print(x)    
    D= Ql+Tl-(2*x[6])  #was x[1] in all last runs before 4.7.16
    align_out=str(Ql)+'\t'+str(Tl)+'\t'+lig1+'_'+lig2+'\t'+str(x[0])+'\t'+str(x[1])+'\t'+str(x[5])+'\t'+str(x[6])+'\t'+str(Dis)+'\t'+str(D)
    #print(align_out)
    out_file.write(microen1+'\t'+microen2+'\t'+align_out+'\n')	
    
    
pymol.cmd.quit()
end = time.time()
print ('Run time is:'+str(end - start))            
 
out_file.close()



	

	

