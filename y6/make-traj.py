import gsd.hoomd
import numpy as np
# First, load the atomistic gsd file used during the KMC sim
# We need the box information from it.

gsd_file = "../trajectory.gsd"
with gsd.hoomd.open(name=gsd_file, mode='rb') as f:
    snap = f[-1]
box = snap.configuration.box

positions = np.load('kmc/carrier_pathfiles/0.npy',allow_pickle = True)

# Iterate throuh positions, create a new snapshot for each
with gsd.hoomd.open("charge-trajectory.gsd", "wb") as traj:
    for pos in positions:
        temp_snap = gsd.hoomd.Snapshot()
        temp_snap.configuration.box = box
        temp_snap.particles.N = 1
        temp_snap.particles.types = ["A"]
        temp_snap.particles.typeid = [0]
        temp_snap.particles.position = np.array(pos)       
        traj.append(temp_snap)
