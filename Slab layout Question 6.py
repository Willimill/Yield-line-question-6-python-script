import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# #Section 1- Setting parameters of slab
# =============================================================================
L=6
W=10
q=15 #load (kN/m**2)
delta=1 #deformation under load

#Flexural capacities
mx=20 #sagging x-direction
my=40 #sagging y-direction
mx1=20 #hogging x-direction
my1=40 #hogging y-direction

# =============================================================================
# #Section 2 -Non-optimised yield line analysis for users
# =============================================================================

# Yield line 1

L1=float(input('estimate a value for L1 which is lower than 6 (to the nearest 0.2m): ')) #(m)
L2=float(input('estimate a value for L2 which is lower than 6 (to the nearest 0.2m): ')) #(m)
theta1=(delta/(W-L2)+(delta/L2))
m1=my
#Energy Dissipation
ED1=L1*theta1*m1

#Yield line 2
#Project into components about 2 rotational axes which, in this case, means the x and y axis

L2x=(L2)
theta2x=delta/(L-L1)
m2x=mx
#Energy Dissipation
ED2x=L2x*theta2x*m2x

L2y=L-L1 
theta2y=delta/(L2)
m2y=my
#Energy Dissipation
ED2y=L2y*theta2y*m2y

#Total Energy dissipation for Yield line 2
ED2= ED2x+ED2y

#Yield line 3
L3x=(W-L2)
theta3x= delta/(L-L1)
m3x = mx
#Energy Dissipation
ED3x= L3x*theta3x*m3x

L3y= L-L1
theta3y= delta/(W-L2)
m3y=my
#Energy Dissipation
ED3y= L3y*theta3y*m3y
#Total Energy dissipation for Yield line 3
ED3=ED3x + ED3y

#Yield line 4
L4=W 
theta4=delta/(L-L1)
m4=mx1
#Energy Dissipation
ED4=L4*theta4*m4

#Yield line 5
L5=L
theta5=delta/(W-L2)
m5=my1
#Energy Dissipation
ED5=L5*theta5*m5

#Total energy dissipated
ED_all=ED1+ED2+ED3+ED4+ED5
print('Total energy dissipation is: ', ED_all)

#Work done
WD=q*(((W-L2)*L1*delta/2)+(L2*L1*delta/2)+(0.5*(W-L2)*(L-L1)*delta/3)+(0.5*L2*(L-L1)*delta/3)+(0.5*W*(L-L1)*delta/3))
print('Work done is:', WD)

#Result of analysis----------
ratio_result= ED_all/WD
print('Ratio of ED/WD for slab is: ', ratio_result)

# =============================================================================
# #Section 3 - Plotting grid to illustrate yield-line from user input
# =============================================================================
#yield line 1
x1=[(L2),(L2)]
y1=[L,(L-L1)]
#yield line 2
x2=[0,(L2)]
y2=[0,(L-L1)]
#yield line 3
x3=[(L2),W]
y3=[(L-L1),0]
#yield line 4
x4= [0,W]
y4= [0,0]
#Yield line 5
x5= [W,W]
y5= [0,L]
#plotting slab onto grid
plt.plot(x1,y1,label='sagging yield line',color='blue')
plt.plot(x2,y2,label='sagging yield line',color='blue')
plt.plot(x3,y3,label='sagging yield line',color='blue')
plt.plot(x4,y4,linestyle='dotted',label='hogging yield line',color='black')
plt.plot(x5,y5,linestyle='dotted',label='hogging yield line',color='black')
plt.grid()
plt.legend()
plt.title("Non-optimised yield-line analysis by users")
plt.xlabel('Width of slab')
plt.ylabel('Length of slab')
plt.show()

# =============================================================================
# #Section 4 - Optimised solution of slab
# =============================================================================
step= 0.25
L2_= 0
ratio_list=[]
L1_list=[]
L2_list=[]
new_L = L+step
for i in np.arange(0,new_L,step):
    L1_=i
    L1_list.append(i)
    L2_=0.0
    while L2_<= W:
        if L2_ != 0 and L2_ != W:
            theta1_opt = ((delta / (W - L2_)) + (delta / L2_))
        else:
            theta1_opt= 1000
        m1 = my
        ED1_opt = L1_ * theta1_opt * m1
        
#Yield line 2
        L2x_opt=L2_
        theta2x_opt=delta/(L-L1_)
        m2x=mx
        ED2x_opt=L2x_opt*theta2x_opt*m2x
        L2y_opt=(L-L1_)
        if L2_ != 0: 
            theta2y_opt=delta/(L2_)
        else: 
            theta2y_opt= 1000
        m2y=my
        ED2y_opt=L2y_opt*theta2y_opt*m2y
        ED2_opt=ED2x_opt+ED2y_opt
        
#Yield line 3
        L3x_opt=(W-L2_)
        theta3x_opt= delta/(L-L1_)
        m3x=mx
        ED3x_opt = L3x_opt*theta3x_opt*m3x
        
        L3y= (L-L1_)
        if L2_ != W:
            theta3y_opt= delta/(W-L2_)
        else: 
            theta3y_opt = 1000
        m3y=my
        ED3y_opt= L3y*theta3y_opt*m3y
        ED3_opt= ED3x_opt+ED3y_opt
                
#Yield line 4
        L4_opt=W
        theta4_opt=delta/(L-L1_)
        m4=mx1
        ED4_opt=L4_opt*theta4_opt*m4
        
#Yield line 5
        L5_opt=L
        if L2_ != W:
            theta5_opt=delta/(W-L2_)
        else:
            theta5_opt = 1000
        m5=my1
        ED5_opt=L5_opt*theta5_opt*m5
        
#Total Energy Dissipated
        ED_all_opt=ED1_opt+ED2_opt+ED3_opt+ED4_opt+ED5_opt
#Work done
        WD_opt=q*(((W-L2_)*L1_*delta/2)+(L2_*L1_*delta/2)+(0.5*(W-L2_)*(L-L1_)*delta/3)+(0.5*L2_*(L-L1_)*delta/3)+(0.5*W*(L-L1_)*delta/3))
        ratio= ED_all_opt/ WD_opt
        ratio_list.append(ratio)
        L2_list.append(L2_)
        L2_=L2_+ step
corrected_list=[]
k=0
for d in ratio_list:
    if ratio_list[k]<0:
        e=ratio_list[k]*(-1)
        corrected_list.append(e)
    else:
        corrected_list.append(ratio_list[k])
    k=k+1  
print('The minimum ratio between energy dissipated and work done is: ',min(corrected_list))
# =============================================================================
# #Section 5 - Creating matrix to input result of iterations for optimisation
# =============================================================================
v=int((L/step)+1) 
q=int((W/step)+1)
z=len(ratio_list)
empty_array= np.zeros((v,q))
empty_array_2= np.zeros((v,q))
ten_percent=min(corrected_list)*0.1
valid= ((min(corrected_list))+ten_percent)
x=v*q
p=0
while p <= x - 1: 
    for r in range(0,v):
        for t in range(0,q):
            empty_array[r,t]=corrected_list[p]
            if corrected_list[p] <= valid:
                empty_array_2[r,t]=corrected_list[p]
            else:
                empty_array_2[r,t]=10
            p=p+1
ratio_list_2d_old=empty_array
valid_array=empty_array_2
# =============================================================================
# #Section 6 - Rotating matrix as python plots matrices in a reversed manner
# =============================================================================
rotated= ratio_list_2d_old[::-1]
rotated_2=valid_array[::-1]
ratio_list_2d=rotated
valid_array_2d=rotated_2
# =============================================================================
# #Section 7 - Creating lists to illustrate users input onto contour plan
# =============================================================================
UG_result_x=[3,7,1.9,5,2.3,2.3,4,7.5,5,4,6]
UG_result_y=[1,1.5,3.3,3,2.5,0.8,1.5,1,6,4,2]
staff_result_x=[3.3,4.1,3.1]
staff_result_y=[6,2.5,3.1]
eng_result_x=[5,3,3]
eng_result_y=[5,3,5]
# =============================================================================
# #Section 8 - Creating contour plot of slab to show optimisation and scatter plot to illustrate users input
# =============================================================================
xlist = np.linspace(0, W, q)
ylist = np.linspace(0, L, v)
X, Y = np.meshgrid(xlist, ylist)
for i in range(len(ratio_list_2d)):
    for x in range(len(ratio_list_2d[i])):
        if(ratio_list_2d[i][x]) > (min(corrected_list)+0.000001):
            ratio_list_2d[i][x] = min(corrected_list)+1
Z = ratio_list_2d
Z_2 = valid_array_2d
fig,ax=plt.subplots(1,1)
cp = ax.contourf(X, Y, Z)
cp_2 = ax.contour(X, Y, Z_2 , 1)
plt.scatter(UG_result_x,UG_result_y, c ='indigo', label='student')
plt.scatter(staff_result_x,staff_result_y, c = 'red', label= 'teaching staff')
plt.scatter(eng_result_x,eng_result_y, c ='yellow', label= 'engineer')
plt.legend(bbox_to_anchor= (1.65,1), loc='upper right')
fig.colorbar(cp) # Add a colorbar to a plot
ax.set_title('Filled Contours Plot based on ED/WD ratio')
ax.set_xlabel('Width of slab')
ax.set_ylabel('Length of slab')
plt.axis('scaled')
plt.show()