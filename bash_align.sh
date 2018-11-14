#!/bin/bash


fPath=$PWD/
pyFuncFile=$fPath"pymolFunction_from_list.py"
IN_FILE_NAME=$1
#OUT_FILE_NAME=$2
CORES=$2

# Work out lines per file.

total_lines=$(wc -l <${IN_FILE_NAME})
((lines_per_file = (total_lines + CORES - 1) / CORES))

# Split the actual file, maintaining lines.

split --lines=${lines_per_file} ${IN_FILE_NAME} align_temp.

# Debug information

echo "Total lines     = ${total_lines}"
echo "Lines  per file = ${lines_per_file}"    
wait
count=0
for f in align_temp.*;
do 
	#python paralle_pymol_list.py $f &
	count=`expr $count + 1`	
	mkdir $count	
	mv $f $PWD/$count
	cp pymolFunction_from_list.py $PWD/$count
	cp manual_cofactor_list_with_quinone_2_atoms_ADE.txt $PWD/$count
	cd $count
	pymol -cq -d "run $pyFuncFile" \
 	-d "pyFunc $f" &
	cd ..
	
	
done

wait
mkdir temp_all	
for f in $(seq 1 $count);
do 
	echo $f
	#cd $f
	cp $PWD/$f/align_temp.*.txt $PWD/temp_all
	#cd ..
	
	
done
cd temp_all
echo "All processes done!"
echo "combine files!"
cat align_temp.*_out.txt > temp_all.txt
echo 'Sourec\tTarget\tSl\tTl\tLigand\tRMSD\tAlign CA\tRaw alignment score\tAligned Residues\tLigand center distance\tStructural Distance\n' | cat - temp_all.txt > temp && mv temp align_out_all.txt
cd ..
