#a = "   jhj  hsgt jshyu"
#print a.find('js')
#if a.startswith("h") == False:
#    start = a.find('js')
#    end = a.find('u')
#print a[start:end]
#-------------------- Exposure Time ------------------------------
column_SEQ = []
column_MJD = []
column_ET = []
column_Vmag = []
column_Bmag = []
column_Umag = []
column_W1mag = []
column_M2mag = []
column_W2mag = []
f = open("PKS0502+049_magnitudes.txt",'r')
lines = f.readlines()[:]
f.close()
line_num = 0 # line numbers / starting point
line_num_of_vMag = [] # to put each number of line which includes "Exposure" 
line_num_of_bMag = []
line_num_of_uMag = []
line_num_of_w1Mag = []
line_num_of_m2Mag = []
line_num_of_w2Mag = []
for line in lines:
# calculate number of lines which include "Exposure"
    line_num+=1 # add one to each line number
    if line.find("uvotsource: UVOT v magnitude (Vega system)")>=0:
       line_num_of_vMag.append(line_num) # list of numbers of lines which include "Exposure"
    if line.find("uvotsource: UVOT b magnitude (Vega system)")>=0:
       line_num_of_bMag.append(line_num) # list of numbers of lines which include "Exposure"
    if line.find("uvotsource: UVOT u magnitude (Vega system)")>=0:
       line_num_of_uMag.append(line_num) # list of numbers of lines which include "Exposure"
    if line.find("uvotsource: UVOT uvw1 magnitude (Vega system)")>=0:
       line_num_of_w1Mag.append(line_num) # list of numbers of lines which include "Exposure"
    if line.find("uvotsource: UVOT uvm2 magnitude (Vega system)")>=0:
       line_num_of_m2Mag.append(line_num) # list of numbers of lines which include "Exposure"
    if line.find("uvotsource: UVOT uvw2 magnitude (Vega system)")>=0:
       line_num_of_w2Mag.append(line_num) # list of numbers of lines which include "Exposure"

# Sequence column
    if line.startswith("Sequence")==True:
       start = line.find("= ")+3
       end = start +11
       column_SEQ.append(line[start:end]+" ")
# MJD column
    if line.startswith("TSTART")==True:
       start = line.find("= ")+2
       end = line.find(" # EXTENSION: 1")
       column_MJD.append(line[start:end]+3*" ")
print column_MJD
# 
# Vmag column
for j in line_num_of_vMag:
        
#    if line.startswith("  Exposure") == True:
       start = lines[j].find(":")
       end = lines[j].find(" (stat)")

       column_Vmag.append(lines[j][start+2:end]+3*" ")
#print column_Vmag
# Bmag column
for j in line_num_of_bMag:
        
#    if line.startswith("  Exposure") == True:
       start = lines[j].find(":")
       end = lines[j].find(" (stat)")

       column_Bmag.append(lines[j][start+2:end]+3*" ")
# Umag column
for j in line_num_of_uMag:
        
#    if line.startswith("  Exposure") == True:
       start = lines[j].find(":")
       end = lines[j].find(" (stat)")

       column_Umag.append(lines[j][start+2:end]+3*" ")
# W1mag column
for j in line_num_of_w1Mag:
        
#    if line.startswith("  Exposure") == True:
       start = lines[j].find(":")
       end = lines[j].find(" (stat)")

       column_W1mag.append(lines[j][start+2:end]+3*" ")
# M2mag column
for j in line_num_of_m2Mag:
        
#    if line.startswith("  Exposure") == True:
       start = lines[j].find(":")
       end = lines[j].find(" (stat)")

       column_M2mag.append(lines[j][start+2:end]+3*" ")
# W2mag column
for j in line_num_of_w2Mag:
        
#    if line.startswith("  Exposure") == True:
       start = lines[j].find(":")
       end = lines[j].find(" (stat)")

       column_W2mag.append(lines[j][start+2:end]+3*" ")

# make new files
f = open("Vardan.txt",'w')
for a,b,c,d,e, g,h,i in zip(column_SEQ,column_MJD,column_Vmag,column_Bmag, column_Umag,column_W1mag, column_M2mag, column_W2mag):
   f.write(a)
   f.write(b)
   f.write(c)
   f.write(d)
   f.write(e)
   f.write(g)
   f.write(h)
   f.write(i)
#   f.write(j)
   f.write("\n")
##for i in column_SEQ:
#   f.write(i)
#   f.write("\n")
f.close()

