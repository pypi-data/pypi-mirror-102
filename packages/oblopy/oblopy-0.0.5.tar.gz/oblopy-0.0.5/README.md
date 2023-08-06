# oblopy

## toblo
A toolbox for analysing Lidar observational data and related meteorological data

## retrieval
Toolbox to retrieve the 3D wind vector from profiling Lidar observations in Doppler beam swinging mode (DBS). In the current state of the retrieval module the input of radial (LOS) velocity observations need to be prepared. For all functions, the LOS velocity input needs to be prepared carefully, such that the the LOS velocity input is consistent with the coordinate of the utilized Lidar system and the retrieval coordinate system. Each beam in the retrieval coordinate system corresponds to a certain azimuth and zenith angle:
### azimuth, a, unit = deg
Lidar beam pointing in the following direction

(x,y) = ( 1, 0) : a = 180 

(x,y) = ( 0, 1) : a = 270 

(x,y) = (-1, 0) : a =   0

(x,y) = ( 0,-1) : a =  90 

### zenith, z, unit = deg
The zenith angle corresponds either to the cone angle of the DBS (e.g. z=28 deg) or is upward pointing (z=0)

### An example for utilizing the retrieval module: Simulate a wind speed series of a Lidar, that is installed on a moving platform 
#### Import the necesary python modules
`from oblopy.retrieval import *`

`import numpy as np`

`import pandas as pd`

#### Make a sample velocity vector
Define a series of time stamps

`time = np.arange(0,40*np.pi, 0.1)`

Define the 3 wind speed components (artificial)

`u = 2*(np.cos(time*2.5)+np.cos(time*1.5)+np.sin(time/2.5)+np.cos(time/3.5))+np.random.rand(len(time))*2` 

`v = -2*(np.cos(time*3.5)+np.sin(time*1.5)+np.sin(time/3.5)-np.cos(time/4.5))-np.random.rand(len(time))*2`

`w = np.cos((time-np.pi)/2*3.5)-np.random.randn(len(time))*0.5`

#### Define a series of roll pitch and yaw angles 
Note: If you do not want to include motion angles and corresponding correction in your retrieval, set the series of roll, pitch and yaw to zero

Define the motion angles (artificial)

`roll  = np.ones(len(time))`       

`pitch = -np.ones(len(time)) + 10`

`yaw   = np.zeros(len(time)) + 45`

Get the corresponding rotation matrix

`R = get_R(roll, pitch, yaw, time, order = 'zyx')`

rotate the simulated wind speed vector 

`vec_u_ = multi_dim_matrix_mult(R,vec_u,time)`

`u_ = vec_u_[0,0,:]`

`v_ = vec_u_[1,0,:]`

`w_ = vec_u_[2,0,:]`

#### Make a sample radial velocity vector
The input to the retrieval should be of similar type. The amount of beams is free to choose. Beams are seperated by azimuth and zenith coordinates. The beams need to be organized in a pandas DataFrame as following. Naming of the collumns (time series corresponding to one beam) is free.

Define the cone angle of the DBS scan

`theta = np.deg2rad(28)`

B1: pointing in oposite x-direction (az=0, ze = 28)

`B1 = pd.DataFrame({'B1':u_[0::5]*np.sin(theta)+w_[0::5]*np.cos(theta)}, index = time[0::5])`

B2: pointing in oposite y-direction (az=90, ze = 28)

`B2 = pd.DataFrame({'B2':v_[1::5]*np.sin(theta)+w_[1::5]*np.cos(theta)}, index = time[1::5])`

B3: pointing in x-direction (az=180, ze = 28)

`B3 = pd.DataFrame({'B3':-u_[2::5]*np.sin(theta)+w_[2::5]*np.cos(theta)}, index = time[2::5])`

B4: pointing in oposite x-direction (az=270, ze = 28)

`B4 = pd.DataFrame({'B4':-v_[3::5]*np.sin(theta)+w_[3::5]*np.cos(theta)}, index = time[3::5])`

B5: vertical pointing beam (az=*, ze = 0), here the choice of azimuth is free

`B5 = pd.DataFrame({'B5':w_[4::5]}, index = time[4::5])`


Define the corresponding azimuth and zenith list. 

Note: Needs to be the same length as the amount of utilized beams

`az = [0,90,180,270,0]`

`ze = [28,28,28,28,0]`

Create a pandas DataFrame contaning the time series of all defined beams

`all_beams = pd.DataFrame(index=time)`

`all_beams['B1'] = B1.copy()`

`all_beams['B2'] = B2.copy()`

`all_beams['B3'] = B3.copy()`

`all_beams['B4'] = B4.copy()`

`all_beams['B5'] = B5.copy()`

#### Do a retrieval of the sample radial velocity vector
Correct the beams by the ship velocity. 

`corr_beams = correct_LOS_vel(all_beams.interpolate(method='pchip'), u_plat, 
                             az = az, ze = ze)`

Retrieve the 3D velocity vector. 

`retr_int = DBS_least_squares_retrieval(corr_beams, roll, pitch, yaw, 
                                       az = az, ze = ze, 
                                       rot=True, order = 'xyz')`