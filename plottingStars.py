import DirOs
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

def Tycho2_Data_Plot():
    fig = plt.figure()
    ax = Axes3D(fig)

    
    Data_VT_Name = 'OutDataVT'
    OutDataVT = open(Data_VT_Name, 'r')

    x, y, z = [], [], []

    for line in OutDataVT.readlines():
        list_theta = []
        list_phi = []
        list_theta = list_theta + list(line[2:13])
        list_phi = list_phi + list(line[14:24])
        a = ''
        list_theta_out = a.join(list_theta)
        list_phi_out = a.join(list_phi)

        theta = float(list_theta_out)
        phi = float(list_phi_out)

        x.append(math.sin(phi) * math.cos(theta))
        y.append(math.sin(phi) * math.sin(theta))
        z.append(math.cos(phi))

    OutDataVT.close()

    ax.scatter3D(x, y, z)
    plt.show()

def main():
    Tycho2_Data_Plot()

main()