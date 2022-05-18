from psana import *

experiment = 'cxilv0418'
scratch_dir = '/reg/d/psdm/cxi/%s/scratch/northeyt/' % experiment

runs=[43, 44, 45, 46, 47, 48, 56, 57, 61, 62, 63, 64, 68, 70, 71, 72, 73, 74, 79, 80, 81, 82, 83]

run = 43  # for initial detector setup; changes later when looping over runs
ds = MPIDataSource('exp=%s:run=%d'% (experiment, run)) 

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
# Each pixel threshold; ADU or keV units 
lb = 2	# lower bound (ADU) for a hit
ub = 80    # Upper bound (ADU) for a hit

# EVR codes
LASERON  = 183
LASEROFF = 184
XRAYOFF  = 162
XRAYOFF1 = 163

