from psana import *

# Experiment and run number
experiment = 'cxilv0418'
run = 43
Nevents = 100000 #Number of detector events to process

# TN: psana experimental stuff,
# TN: setup detector etc.
ds = MPIDataSource('exp=%s:run=%d'% (experiment, run)) 
# FILENAME:
smldata = ds.small_data('/reg/d/psdm/cxi/%s/scratch/northeyt/upstream_stats_run%d.h5' %(experiment, run), gather_interval=100)  #This creates a 'small-data file' in your scratch folder, which is later loaded into the i_ub script

front = Detector('jungfrau4M', ds.env())
diode_upstream = Detector('CXI-DG2-BMMON', ds.env())
diode_downstream = Detector('CXI-DG3-BMMON', ds.env())
x_ray = Detector('FEEGasDetEnergy', ds.env())
electron = Detector('EBeam', ds.env())
uvint = Detector('Acqiris', ds.env())
stageencoder = Detector('CXI:LAS:MMN:04.RBV', ds.env())
ttfltpos = Detector('CXI:TIMETOOL:FLTPOS', ds.env())
chamber_pressure = Detector('CXI:MKS670:READINGGET', ds.env())
det_z = Detector('Jungfrau_z', ds.env())

#This section is for choosing the correct evr detector, which occasionally switches
# TN: Can rewrite shorter I think. Also why does this happen, what exactly is going on?
evr = Detector('evr1')
evt0 = ds.events().next()
evrcodes = evr(evt0)
if evrcodes is None:
    evr = Detector('evr2')
    evrcodes_otherdetector = evr(evt0)
    if evrcodes_otherdetector is None:
        print('evr error')
    else:
        print('evr detector found')

#These diode values are from the diode which measures the pulse by pulse X-ray pulse intensity. 
diode_avg = 25000
lower_threshold = 10
upper_threshold = 50000
# TN: I thought the diode values are the pulse intensity, then what is this?
# Each pixel threshold; ADU or keV units 
lb = 2	# lower bound (ADU) for a hit
ub = 80    # Upper bound (ADU) for a hit

# EVR codes
LASERON  = 183
LASEROFF = 184
XRAYOFF  = 162
XRAYOFF1 = 163

