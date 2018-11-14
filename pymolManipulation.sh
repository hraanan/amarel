#!/bin/bash
clear

fPath=$PWD/
#$1=='alpha'
pyFuncFile=$fPath"pymolFunction_from_list.py"
#pdbFldr=$fPath"PDB/"
part=100
IN_FILE=$1
#PDB1=1fdn_SF4_56
#PDB2=1fdn_SF4_57

pymol -c -d "run $pyFuncFile" -d "pyFunc $IN_FILE"  



#-cq  
 # -d "set transparency_mode, 1"\
 #-d "set ray_shadow, off"\
 #-d "ray"\
 #  -d "set depth_cue, 0"\
 #  -d "set orthoscopic, off"\
 #  -d "set field_of_view,8"\
