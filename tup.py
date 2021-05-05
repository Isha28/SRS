import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

totalTime_2048 = [6405579909,6339623075,5394737507,3562329278,0,6672791507,6761151800,6156675416,4912164848,0,12640739086,13108690932,11600825343,11360574558]
buildTime_2048 = [147091910,273310092,171483390,93613902,0,177174306,218331590,173464950,89016608,0,2673143604,4626233533,2692273941,4125666001]
probeTime_2048 = [6258014903,972614667,4295404381,1197795834,0,6495078611,1315458958,4715492166,1594570108,0,9967104698,2825465733,7269303127,2880308580]
partitionTime_2048 = [473096,5093698316,927849736,2270919542,0,538590,5227361252,1267718300,3228578132,0,490784,5656991666,1639248275,4354599977]

names = ['No','Parallel','Indep','Radix','','No','Parallel','Indep','Radix','','No','Parallel','Indep','Radix']
r = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]

#fig, ax = plt.subplots(nrows=1, ncols=2)
plt.figure(figsize=(20, 8))
plt.subplot(1, 2, 1)
bars = np.add(partitionTime_2048, buildTime_2048).tolist()
plt.bar(r,partitionTime_2048, color='blue', edgecolor='white', label='Partition')
plt.bar(r,buildTime_2048, bottom=partitionTime_2048, color='red', edgecolor='white', label='Build')
plt.bar(r,probeTime_2048, bottom=bars, color='green', edgecolor='white', label = 'Probe')

plt.rc('xtick',labelsize=30)
plt.rc('ytick',labelsize=30)
#plt.rcParams['ytick.labelsize']=30

#matplotlib.rcParams.update({'font.size': 40})

plt.title("Vary tuple sizes with Materialisation\n", fontsize=20)
plt.xticks(r, names, rotation='vertical', fontsize=20)
plt.ylabel('CPU Ticks', fontsize=30)
plt.legend(fontsize=22)

plt.savefig('finaltupmateuni.jpg', bbox_inches='tight')
plt.show()

#out_png = 'matetup.png'
#plt.savefig(out_png, dpi=150)

