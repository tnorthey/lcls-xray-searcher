import h5py
import numpy as np

# Load the "key" array from a h5 file
def load_h5data(fname,key):
 try:
  f = h5py.File(fname, 'r')
 except Exception as e:
  print('Error: %s' % e)
  return False
 print(f.keys())
 try:
  dset = f[key]
 except Exception as e:
  print('%s error: %s' % (key, e))
  return False
 print(dset.shape)
 return dset

# TN: what is this?
def safe_get(det, evt):
  try:
    return det.get(evt)
  except Exception:
    return None

def checks():
  ############################################################
  ### BEGIN CHECKS (I don't save any of this data to file)
  if evt is None: return False
  evrcodes = evr(evt)
  if evrcodes is None: return False

  # determine uvon, uvoff, dark
  dark = XRAYOFF in evrcodes
  if dark: return False

  evt_xray_pull = safe_get(x_ray, evt)
  if evt_xray_pull is None: return False
  # x-ray intensity in mJ 
  #evt_xray = evt_xray_pull.f_21_ENRC()
  #print('evt_xray: ' + str(evt_xray))

  # electron pull?
  evt_electron_pull = safe_get(electron, evt)
  if evt_electron_pull is None: return False
  #evt_electron = evt_electron_pull.ebeamCharge()
  #print('evt_electron: ' + str(evt_electron))

  # position in space of Jungfrau (distance from cell)
  evt_det_z = det_z(evt)
  if evt_det_z is None: return False
  #print('evt_det_z: ' + str(evt_det_z))
    
  # upstream/downstream correlation if there are non-linear effect (?)
  evt_xint_pulldown = safe_get(diode_downstream, evt)
  if evt_xint_pulldown is None: return False
  #evt_diode_downstream = evt_xint_pulldown.TotalIntensity()
  #print('evt_diode_downstream: ' + str(evt_diode_downstream))
  return True
  ### END CHECKS
  ############################################################

def get_xint():
  evt_xint_pull = safe_get(diode_upstream, evt)
  if evt_xint_pull is None: return False
  xint = evt_xint_pull.TotalIntensity() #; print('xint: ' + str(xint))
  if (xint < lower_threshold) or (xint >= upper_threshold): return False

# print basic stats function
def stats(dset):
  print('length:  %d' % len(dset))
  print('mean:    %f' % np.mean(dset))
  print('median:  %f' % np.median(dset))
  print('minimum: %f' % np.min(dset))
  print('maximum: %f' % np.max(dset))
  print('st. dev: %f' % np.std(dset))

def radial_avg(q,data,nbins):
  # radial avg:
  nq = nbins + 1
  q_max = np.max(q)
  q_rad = np.linspace(0,q_max,nq)
  #print('q_rad length = %d' % len(q_rad))
  #print(q_rad.shape)
  print('Averaging over %d bins...' % nbins)
  I_rad = np.zeros(nbins)
  for i in range(0, nbins):
    #print('Iteration %d' % i)
    #print('creating bin in q-range: %f - %f' % (q_rad[i], q_rad[i+1]))
    #print(q >= q_rad[i])
    #print(q < q_rad[i+1])
    condition = np.logical_and(q >= q_rad[i], q < q_rad[i+1])
    #print(condition)
    tmp = np.where(condition, 1, 0)  # 1s and 0s array of matching the condition
    counts = np.sum(tmp)  # count hits that match the condition
    #print(tmp.shape)
    #print(high_data.shape)
    #print(np.multiply(low_data,tmp))
    if counts > 0:
      I_rad[i] = np.sum(np.multiply(data,tmp), axis=None) / counts
    else: continue
  return q_rad[0:nbins],I_rad