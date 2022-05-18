import h5py

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

