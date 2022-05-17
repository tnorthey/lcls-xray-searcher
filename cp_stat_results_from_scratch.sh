runs=(43 44 45 46 47 48 56 57 61 62 63 64 68 70 71 72 73 74 79 80 81 82 83)
echo "total runs:"
len=${#runs[@]}
echo $len

for (( i=0; i<$len; i++ ))
do
 run=${runs[i]}
 dir=stats_run$run
 echo "Copying h5 file from scratch to $dir"
 cp /reg/d/psdm/cxi/cxilv0418/scratch/northeyt/upstream_stats_run"$run".h5 $dir
done

