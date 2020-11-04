 import numpy as np
C2b=matrix([[1,0,0],[0,cos(gamma),sin(gamma)],[0,-sin(gamma),cos(gamma)]])
C12=matrix([[cos(theta),0,-sin(theta) ],[ 0,1,0],[sin(theta),0,cos(theta)]])
Cn1=matrix([[cos(phi),sin(phi),0],[-sin(phi),cos(phi),0],[0,0,1])
Cbn12=sin(gamma)*sin(theta)*cos(phi)-cos(gamma)*sin(phi)
Cbn12=sin(gamma)*sin(phi)+cos(gamma)*sin(theta)*cos(phi)
Cbn22=cos(phi)*sin(gamma)+sin(gamma)*sin(theta)*sin(phi)
Cbn23=sin(phi)*sin(theta)*cos(gamma)-sin(gamma)*cos(phi)
#Cbn is the coordinate transformation matrix from B to N system
Cbn=matrix([[cos(phi)*cos(theta),Cbn12,Cbn13],[cos(theta)*sin(phi),Cbn22,Cbn23],[-sin(theta),sin(gamma)*cos(theta),cos(theta)*cos(gamma)]])
#wnb is angular velocity of B system relative to N
wnb=matrix([[wnbxb],[wnbyb],[wnbzb]])
#
#wnb=(C2b@C12)@np.array([[0],[0],[-phi]])+C2@np.array([[0],[theta],[0]])+np.array([gamma],[0],[0]])
#
matrix([[gamma],[theta],[phi]])=np.linalg.inv(matrix([[1,0,-sin(theta)],[0,cos(gamma),sin(gamma)*cos(theta)],[0,-sin(gamma),cos(gamma)*cos(theta)]]))*wnb
ab=matrix([[axb],[ayb],[azb]])    #already did the transpose
an1=matrix([[axn1],[ay1],[azn1]])
an1=Cbn*ab
an=matrix([[axn],[ayn],[azn]])
an=an1-matrix([[0],[0],[9.8]])
dellt=0.0001;
dellv=matrix([[dellvxn],[dellvyn],[dellvzn]])
dellv=an*dellt
vn(t+1)=matrix([[vxn(t+1)],[vyn(t+1)],[vzn(t+1]])
vn(t+1)=matrix([[vxn(t)],[vyn(t)],[vzn(t)]])+dellv
dellXn=matrix([[dellXxn],[dellXyn],[dellXzn]])
dellXn=matrix([[vxn],[vyn],[vzn]])@dellt+0.5*an*dellt*dellt
Xn(t+1)=matrix([[Xxn(t+1)],[Xyn(t+1)],[Xzn(t+1]])
Xn(t+1)=matrix([[Xxn(t)],[Xyn(t)],[Xzn(t)]])+dellXn
