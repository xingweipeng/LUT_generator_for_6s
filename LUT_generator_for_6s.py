# -*- coding: utf-8 -*-
"""
Created on Thu May 17 16:59:41 2018

@author: xwp
"""
import sys,os

sun_zenith=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85]#dim=18
satellite_zenith=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85]#dim=18
relative_azimuth=[0.01,15,30,45,60,75,90,105,120,135,150,165,180]#dim=7
aot=[0.001,0.05,0.1,0.3,0.5,0.8,1,1.2,1.5,1.8,2,2.5]#dim=12
list=[]
lookup_table=open('lut_red_whole.txt','w+')

for  i in range(0,len(sun_zenith)):

  for  j in range(0,len(satellite_zenith)):

   for k in range(0,len(relative_azimuth)):
   
    for t in range(0,len(aot)):
		f=open('in_put.txt','r+')
		input_parametre=f.readlines()
		#print flist[12]
		
		input_parametre[1]=str(sun_zenith[i])+' '+str(relative_azimuth[k])+' '+str(satellite_zenith[j])+' '+'0 1 7'+'\n'
		input_parametre[5]=str(aot[t])+'\n'
		#input_parametre[12]='-'+blue_top[i]
		f=open('in_put.txt','w+')
		f.writelines(input_parametre)
		f.close()
		command="sixs.exe"+"<in_put.txt>"+"out.txt"
		#print command
		os.system(command)
		f=open("out.txt",'r+')#edit by xwp
		out_result=f.readlines()#edit by xwp
		#sur_str=out_result[135]
		aod=str(aot[t])
		ggt=out_result[95].split()[7] #the value need
		tt=out_result[107].split()[7]
		sa=out_result[113].split()[6]
		pa=out_result[116].split()[5]
		angle=str(sun_zenith[i])+' '+str(relative_azimuth[k])+' '+str(satellite_zenith[j])
		lookup_table.writelines(angle+' '+aod+' '+ggt+' '+tt+' '+sa+' '+pa+'\n')
		print i,j,k,t
	
		f.close()#edit by xwp

lookup_table.close()

