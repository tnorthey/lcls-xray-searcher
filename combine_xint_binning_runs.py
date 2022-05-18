import numpy as np
from global_vars import *
from myfunctions import *

# write more general...
zero_array = np.zeros((20, 8, 512, 1024))
data_total = zero_array

for run in runs:
 print('Run: %s' % run)
 h5file = '%sxint_binning_run%d.h5' % (scratch_dir, run)
 print('Loading %s...' % h5file)
 x = load_h5data(h5file,'data')
 if x==False: print('Skipping run %s' % run); continue
 data_total += x

hf = h5py.File('combined_runs_xint_binning.h5', 'w')
hf.create_dataset('data_total', data=data_total)
hf.close()
