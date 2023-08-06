# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 07:30:14 2020

@author: merve.tascioglu@barkhauseninstitut.org
"""

import cmath
import numpy as np
import matplotlib.pyplot as plt
from math import sin,pi,log,cos
import numpy as np



'''Description of the functions:
    
af_asym_phasescannig: Array factor pattern for Uniform or Asymmetrical Arrays with Phase Shifting Technique
af_asym_timescannig:  Array factor pattern for Uniform or Asymmetrical Arrays with Time Delay Technique
af_symmetrical_phasescannig: Array factor pattern for Symmetrical Arrays with Phase Shifting Technique
af_symmetrical_timescannig:  Array factor pattern for Symmetrical Arrays with True Time Delay Technique

cartesian_plot: Plot Normalized Array Factor [dB] vs Incident Angle [°]
polar_plot: Plot Array Factor [Unitless] vs Incident Angle [°]
'''

''' Description of the input variables that are required for functions below.
    
    bx, by, bz:     The coefficient represents the association of distance and wavelength along the relevant axis. (d=bλ)
    f:              Frequency of the signal sent
    f0:             Carrier frequency
    steering_angle: Steering angle
    Nx:             Number of elements along x axis
    Ny:             Number of elements along y axis
    Nz:             Number of elements along z axis
    increaserate:   This is the amount of change of distances between the elements in the case of NON-UNIFORM spacing. For uniform array, it must be set as 0.

'''
#%% Function for calculating the array factor

def af_asym_phasescannig (bx,by,bz,f,f0,steering_angle,Nx,Ny,Nz,increase_rate,plane):
    
    c=3e8
    lamda=c/f   
    lamda0=c/f0
    
    k=2*pi/lamda
    k0=2*pi/lamda0
    
    #%%
    ''' 
    This section is all about defining the inter element spacing which depends on lambda and increase rate.
    '''
    #To create an asymmetrical array:
    if Nx>0:
        distances_along_x=[0]
        dx=0 #origin
        for n in range(0,Nx-1):
            dx=dx+(bx+(n*increase_rate))
            distances_along_x.append(dx*lamda0)  #distances_along_x contains the position of each element along x axis
            
    if Ny>0:
        distances_along_y=[0]
        dy=0 #origin
        for n in range(0,Ny-1):
            dy=dy+(by+(n*increase_rate))
            distances_along_y.append(dy*lamda0)  #distances_along_y contains the position of each element along y axis
    
    if Nz>0:
        distances_along_z=[0]
        dz=0 #origin
        for n in range(0,Nz-1):
            dz=dz+(bz+(n*increase_rate))
            distances_along_z.append(dz*lamda0)  #distances_along_z contains the position of each element along z axis
        
    #%%

    incoming_angle=np.arange(-180,180.2,0.2) # To define the x-axis of plot (incoming angle,theta)
    

    array_factor_x=np.zeros(len(incoming_angle)) #to create an empty array which will be filled via for loop below with respect to the incoming angle, theta.
    array_factor_y=np.zeros(len(incoming_angle)) #to create an empty array which will be filled via for loop below with respect to the incoming angle, theta.
    array_factor_z=np.zeros(len(incoming_angle)) #to create an empty array which will be filled via for loop below with respect to the incoming angle, theta.

    for i in range(len(incoming_angle)):
        
        #%%
        ''' This section is all about the implementation of the equations come about the theory.
        To clarify these equations, please check the 'Theory of Array Factor.pdf'.
        '''
        #Array Factor along X axis
        if Nx>0:
            
            # Based on the plane, either phi or theta must be kept constant. 
            if plane=='E':
                phi=np.zeros(len(incoming_angle)) 
                phi0=phi
                
                theta=incoming_angle
                theta0=np.ones(len(incoming_angle))*steering_angle
                
            if plane=='H':
                theta=np.ones(len(incoming_angle))*90 
                theta0=theta
                
                phi=incoming_angle
                phi0=np.ones(len(incoming_angle))*steering_angle

            all_received_signals_x=[]
            for n in range(0,Nx):
                
                dist=distances_along_x[n]
                received_signal_x=cmath.exp(1j*((k*dist*sin(theta[i]*pi/180*cos(phi[i]*pi/180)))-(k0*dist*sin(theta0[i]*pi/180)*cos(phi0[i]*pi/180))))
                all_received_signals_x.append(received_signal_x)
                
            array_factor_x[i]=(abs(sum(all_received_signals_x)))*(1/Nx)
        else:
            array_factor_x=int(1)
        
        
        #%%Array Factor along Y axis
        if Ny>0:
        # Based on the plane, either phi or theta must be kept constant. 
            if plane=='E':
                phi=np.ones(len(incoming_angle))*90 
                phi0=phi
                
                theta=incoming_angle
                theta0=np.ones(len(incoming_angle))*steering_angle
                
            if plane=='H':
                theta=np.ones(len(incoming_angle))*90 
                theta0=theta
                
                phi=incoming_angle
                phi0=np.ones(len(incoming_angle))*steering_angle
        

            all_received_signals_y=[]
            for n in range(0,Ny):
                dist=distances_along_y[n]
                received_signal_y=cmath.exp(1j*((k*dist*sin(theta[i]*pi/180)*sin(phi[i]*pi/180))-(k0*dist*sin(theta0[i]*pi/180)*sin(phi0[i]*pi/180))))
                all_received_signals_y.append(received_signal_y)
    
            array_factor_y[i]=(abs(sum(all_received_signals_y)))*(1/Ny)
        
        else:
            array_factor_y=int(1)
        
        #%%Array Factor along Z axis
        if Nz>0:
            all_received_signals_z=[]
            for n in range(0,Nz):
                dist=distances_along_z[n]
                received_signal_z=cmath.exp(1j*((k*dist*cos(incoming_angle[i]*pi/180))-(k0*dist*cos(steering_angle*pi/180))))
                all_received_signals_z.append(received_signal_z)
            array_factor_z[i]=(abs(sum(all_received_signals_z)))*(1/Nz)
        else:
            array_factor_z=int(1)
        array_factor=array_factor_x*array_factor_y*array_factor_z
    
    return incoming_angle,array_factor

def af_asym_timescannig (bx,by,bz,f,f0,steering_angle,Nx,Ny,Nz,increase_rate,plane):
    
    ''' 
    This section is all about defining the inter element spacing which depends on lambda and increase rate.
    '''
  
    #To create an asymmetrical array:
    if Nx>0:
        distances_along_x=[0]
        dx=0 #origin
        for n in range(0,Nx-1):
            dx=dx+(bx+(n*increase_rate))
            distances_along_x.append(dx)   #distances_along_x contains the position of each element along x axis
            
    if Ny>0:
        distances_along_y=[0]
        dy=0 #origin
        for n in range(0,Ny-1):
            dy=dy+(by+(n*increase_rate))
            distances_along_y.append(dy)   #distances_along_y contains the position of each element along y axis
    
    if Nz>0:
        distances_along_z=[0]
        dz=0 #origin
        for n in range(0,Nz-1):
            dz=dz+(bz+(n*increase_rate))
            distances_along_z.append(dz)  #distances_along_z contains the position of each element along z axis
        
    c=3e8
    lamda=c/f
    lamda0=c/f0
    k=2*pi/lamda
    

    incoming_angle=np.arange(-180,180.2,0.2) #define the x-axis of the plot.

    array_factor_x=np.zeros(len(incoming_angle)) #to create empty array which will be filled by for loop below
    array_factor_y=np.zeros(len(incoming_angle)) #to create empty array which will be filled by for loop below
    array_factor_z=np.zeros(len(incoming_angle)) #to create empty array which will be filled by for loop below

    for i in range(len(incoming_angle)):
        
        #%%Array Factor along X axis
        if Nx>0:
            # Based on the plane, either phi or theta must be kept constant. 
            if plane=='E':
                phi=np.zeros(len(incoming_angle)) 
                phi0=phi
                
                theta=incoming_angle
                theta0=np.ones(len(incoming_angle))*steering_angle
                
            if plane=='H':
                theta=np.ones(len(incoming_angle))*90 
                # theta=np.transpose(theta)
                theta0=theta
                
                phi=incoming_angle
                phi0=np.ones(len(incoming_angle))*steering_angle
            
            phase_function_x=(sin(theta[i]*pi/180)*cos(phi[i]*pi/180))-sin(theta0[i]*pi/180)*cos(phi0[i]*pi/180)

            all_received_signals_x=[]
            for n in range(0,Nx):
                
                dist=distances_along_x[n]*lamda0
                received_signal_x=cmath.exp(1j*k*dist*phase_function_x)
                all_received_signals_x.append(received_signal_x)
                
            array_factor_x[i]=(abs(sum(all_received_signals_x)))*(1/Nx)
        else:
            array_factor_x=int(1)
        
        if Ny>0:
        #%%Array Factor along Y axis
        # Based on the plane, either phi or theta must be kept constant. 
   
            if plane=='E':
                phi=np.ones(len(incoming_angle))*90 
                phi0=phi
                
                theta=incoming_angle
                theta0=np.ones(len(incoming_angle))*steering_angle
                
            if plane=='H':
                theta=np.ones(len(incoming_angle))*90 
                theta0=theta
                
                phi=incoming_angle
                phi0=np.ones(len(incoming_angle))*steering_angle
        
            phase_function_y=(sin(theta[i]*pi/180)*sin(phi[i]*pi/180))-(sin(theta0[i]*pi/180)*sin(phi0[i]*pi/180))
            all_received_signals_y=[]
            for n in range(0,Ny):
                
                dist=distances_along_y[n]*lamda0
                received_signal_y=cmath.exp(1j*k*dist*phase_function_y)
                all_received_signals_y.append(received_signal_y)
    
            array_factor_y[i]=(abs(sum(all_received_signals_y)))*(1/Ny)
        
        else:
            array_factor_y=int(1)
        
        #%%Array Factor along Z axis
        if Nz>0:
            theta=incoming_angle
            theta0=np.ones(len(incoming_angle))*steering_angle

            phase_function_z=cos(theta[i]*pi/180)-cos(theta0[i]*pi/180)
            all_received_signals_z=[]
            for n in range(0,Nz):
                
                dist=distances_along_z[n]*lamda0
                received_signal_z=cmath.exp(1j*k*dist*phase_function_z)
                all_received_signals_z.append(received_signal_z)
    
            array_factor_z[i]=(abs(sum(all_received_signals_z)))*(1/Nz)
            
        
        else:
            array_factor_z=int(1)
        
        array_factor=array_factor_x*array_factor_y*array_factor_z

    return incoming_angle,array_factor

def af_symmetrical_phasescannig (bx,by,bz,f,f0,steering_angle,Nx,Ny,Nz,increase_rate,plane):
    
    c=3e8
    lamda=c/f
    lamda0=c/f0
    
    k=2*pi/lamda
    k0=2*pi/lamda0
    
    ''' 
    This section is all about defining the inter element spacing which depends on lambda and increase rate.
    '''
    #To create an symmetrical array:
    
    if Nx>1:
        distances_along_x=[]
        dx=bx #origin
        for n in range(int(Nx/2)):
            distances_along_x.append(dx)
            dx=dx+increase_rate
        
        new_list_x=sorted(distances_along_x,reverse=True)
        new_list_x.remove(bx)
        new_list_x.extend(distances_along_x)
        new_list_x.insert(0, 0)    #new_list_x contains the position of each element along x axis
         
    if Ny>1:
        distances_along_y=[]
        dy=by #origin
        for n in range(int(Ny/2)):
            distances_along_y.append(dy)
            dy=dy+increase_rate
        new_list_y=sorted(distances_along_y,reverse=True)
        new_list_y.remove(by)
        new_list_y.extend(distances_along_y)
        new_list_y.insert(0, 0)     #new_list_y contains the position of each element along y axis
    
    if Nz>1:
        distances_along_z=[]
        dz=bz #origin
        for n in range(int(Nz/2)):
            distances_along_z.append(dz)
            dz=dz+increase_rate
        new_list_z=sorted(distances_along_z,reverse=True)
        new_list_z.remove(bz)
        new_list_z.extend(distances_along_z)
        new_list_z.insert(0, 0)   #new_list_z contains the position of each element along z axis

    incoming_angle=np.arange(-180,180.2,0.2) #define the x-axis(start,stop,step)
    

    array_factor_x=np.zeros(len(incoming_angle)) #create empty array
    array_factor_y=np.zeros(len(incoming_angle)) #create empty array
    array_factor_z=np.zeros(len(incoming_angle)) #create empty array

    for i in range(len(incoming_angle)):
        
        #%%Array Factor along X axis
        if Nx>1:
            # Based on the plane, either phi or theta must be kept constant. 
            if plane=='E':
                phi=np.zeros(len(incoming_angle)) 
                phi0=phi
                
                theta=incoming_angle
                theta0=np.ones(len(incoming_angle))*steering_angle
                
            if plane=='H':
                theta=np.ones(len(incoming_angle))*90 
                # theta=np.transpose(theta)
                theta0=theta
                
                phi=incoming_angle
                phi0=np.ones(len(incoming_angle))*steering_angle
            
            all_received_signals_x=[]
            for n in range(0,Nx):
                
                dist=sum(new_list_x[:n+1])*lamda0
                received_signal_x=cmath.exp(1j*((k*dist*sin(theta[i]*pi/180*cos(phi[i]*pi/180)))-(k0*dist*sin(theta0[i]*pi/180)*cos(phi0[i]*pi/180))))
                all_received_signals_x.append(received_signal_x)
                
            array_factor_x[i]=(abs(sum(all_received_signals_x)))*(1/Nx)
        else:
            array_factor_x=int(1)
        
        if Ny>1:
        #%%Array Factor along Y axis
        # Based on the plane, either phi or theta must be kept constant. 
   
            if plane=='E':
                phi=np.ones(len(incoming_angle))*90 
                phi0=phi
                
                theta=incoming_angle
                theta0=np.ones(len(incoming_angle))*steering_angle
                
            if plane=='H':
                theta=np.ones(len(incoming_angle))*90 
                theta0=theta
                
                phi=incoming_angle
                phi0=np.ones(len(incoming_angle))*steering_angle
        
        
            all_received_signals_y=[]
            for n in range(0,Ny):
                dist=sum(new_list_y[:n+1])*lamda0
                received_signal_y=cmath.exp(1j*((k*dist*sin(theta[i]*pi/180)*sin(phi[i]*pi/180))-(k0*dist*sin(theta0[i]*pi/180)*sin(phi0[i]*pi/180))))
                all_received_signals_y.append(received_signal_y)
    
            array_factor_y[i]=(abs(sum(all_received_signals_y)))*(1/Ny)
        
        else:
            array_factor_y=int(1)
        
        #%%Array Factor along Z axis
        if Nz>1:
            all_received_signals_z=[]
            for n in range(0,Nz):
                dist=sum(new_list_z[:n+1])*lamda0
                received_signal_z=cmath.exp(1j*((k*dist*cos(theta[i]*pi/180))-(k0*dist*cos(theta0*pi/180))))
                all_received_signals_z.append(received_signal_z)
    
            array_factor_z[i]=(abs(sum(all_received_signals_z)))*(1/Nz)
            
        
        else:
            array_factor_z=int(1)
        
        array_factor=array_factor_x*array_factor_y*array_factor_z

    return incoming_angle,array_factor

def af_symmetrical_timescannig (bx,by,bz,f,f0,steering_angle,Nx,Ny,Nz,increase_rate,plane):
    
    ''' 
    This section is all about defining the inter element spacing which depends on lambda and increase rate.
    '''
  
    #To create an symmetrical array:

    if Nx>1:
        distances_along_x=[]
        dx=bx #origin
        for n in range(int(Nx/2)):
            distances_along_x.append(dx)
            dx=dx+increase_rate
        new_list_x=sorted(distances_along_x,reverse=True)
        new_list_x.remove(bx)
        new_list_x.extend(distances_along_x)
        new_list_x.insert(0, 0)     #new_list_x contains the position of each element along x axis
        
    if Ny>1:
        distances_along_y=[]
        dy=by #origin
        for n in range(int(Ny/2)):
            distances_along_y.append(dy)
            dy=dy+increase_rate
        new_list_y=sorted(distances_along_y,reverse=True)
        new_list_y.remove(by)
        new_list_y.extend(distances_along_y)
        new_list_y.insert(0, 0)     #new_list_y contains the position of each element along y axis
    
    if Nz>1:
        distances_along_z=[]
        dz=bz #origin
        for n in range(int(Nz/2)):
            distances_along_z.append(dz)
            dz=dz+increase_rate
        new_list_z=sorted(distances_along_z,reverse=True)
        new_list_z.remove(bz)
        new_list_z.extend(distances_along_z)
        new_list_z.insert(0, 0)         #new_list_z contains the position of each element along z axis
        
    c=3e8
    lamda=c/f
    lamda0=c/f0
    k=2*pi/lamda
    

    incoming_angle=np.arange(-180,180.2,0.2) #define the x-axis of the plot.

    array_factor_x=np.zeros(len(incoming_angle)) #to create empty array which will be filled by for loop below
    array_factor_y=np.zeros(len(incoming_angle)) #to create empty array which will be filled by for loop below
    array_factor_z=np.zeros(len(incoming_angle)) #to create empty array which will be filled by for loop below

    for i in range(len(incoming_angle)):
        
        #%%Array Factor along X axis
        if Nx>1:
            # Based on the plane, either phi or theta must be kept constant. 
            if plane=='E':
                phi=np.zeros(len(incoming_angle)) 
                phi0=phi
                
                theta=incoming_angle
                theta0=np.ones(len(incoming_angle))*steering_angle
                
            if plane=='H':
                theta=np.ones(len(incoming_angle))*90 
                # theta=np.transpose(theta)
                theta0=theta
                
                phi=incoming_angle
                phi0=np.ones(len(incoming_angle))*steering_angle
            
            phase_function_x=(sin(theta[i]*pi/180)*cos(phi[i]*pi/180))-sin(theta0[i]*pi/180)*cos(phi0[i]*pi/180)

            all_received_signals_x=[]
            for n in range(0,Nx):
                
                dist=sum(new_list_x[:n+1])*lamda0
                received_signal_x=cmath.exp(1j*k*dist*phase_function_x)
                all_received_signals_x.append(received_signal_x)
                
            array_factor_x[i]=(abs(sum(all_received_signals_x)))*(1/Nx)
        else:
            array_factor_x=int(1)
        
        if Ny>1:
        #%%Array Factor along Y axis
        # Based on the plane, either phi or theta must be kept constant. 
   
            if plane=='E':
                phi=np.ones(len(incoming_angle))*90 
                phi0=phi
                
                theta=incoming_angle
                theta0=np.ones(len(incoming_angle))*steering_angle
                
            if plane=='H':
                theta=np.ones(len(incoming_angle))*90 
                theta0=theta
                
                phi=incoming_angle
                phi0=np.ones(len(incoming_angle))*steering_angle
        
            phase_function_y=(sin(theta[i]*pi/180)*sin(phi[i]*pi/180))-(sin(theta0[i]*pi/180)*sin(phi0[i]*pi/180))
            all_received_signals_y=[]
            for n in range(0,Ny):
                
                dist=sum(new_list_y[:n+1])*lamda0
                received_signal_y=cmath.exp(1j*k*dist*phase_function_y)
                all_received_signals_y.append(received_signal_y)
    
            array_factor_y[i]=(abs(sum(all_received_signals_y)))*(1/Ny)
        
        else:
            array_factor_y=int(1)
        
        #%%Array Factor along Z axis
        if Nz>1:
            theta=incoming_angle
            theta0=np.ones(len(incoming_angle))*steering_angle

            phase_function_z=cos(theta[i]*pi/180)-cos(theta0[i]*pi/180)
            all_received_signals_z=[]
            for n in range(0,Nz):
                
                dist=sum(new_list_z[:n+1])*lamda0
                received_signal_z=cmath.exp(1j*k*dist*phase_function_z)
                all_received_signals_z.append(received_signal_z)
    
            array_factor_z[i]=(abs(sum(all_received_signals_z)))*(1/Nz)
            
        
        else:
            array_factor_z=int(1)
        
        array_factor=array_factor_x*array_factor_y*array_factor_z

    return incoming_angle,array_factor

def cartesian_plot(x_axis,y_axis):
    y_axis_db=20*(np.log10(abs(y_axis)))

    plt.figure(figsize=(12,8))
    plt.plot(x_axis,y_axis_db,c='green',label='...')
    
    plt.ylim(-40,0)
    plt.xlim(-90,90)
    
    plt.xlabel('Incident Angle°',size=12)
    plt.ylabel('Normalized Array Factor in dB', size=12)
    plt.grid('on', linestyle='--',alpha=1)
    plt.show()
    
    return

def polar_plot(x_axis,y_axis):

    theta_incoming_angle_radian=x_axis*pi/180
    
    plt.figure(figsize=(12,8))
    plt.axes(projection='polar')
    plt.polar(theta_incoming_angle_radian,y_axis,c='red')
    plt.show()
    return
