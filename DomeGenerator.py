#! /usr/bin/env python
# -*- python -*-

# ----------------------------------------------------------------
# References:
#   The calculations used in this program are all from the site
#   http://www.vb-helper.com/tutorial_platonic_solids.html
#   Many thanks for making this information available!
#
# ----------------------------------------------------------------

import math
import decimal as D
import Coordinates as C
import IcoFace as F
import GeoSphere as G
import config as CF
import statistics
try:
    import pip
except ImportError:
    raise Exception("Pip is not installed on you computer. Please see instruction 3 on the readme.")
import subprocess
import sys

try:
    import cs
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'cs'])
    import cs

try:
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'numpy'])
    import numpy as np

dPi = D.Decimal(str(math.pi))

# Centre angle of pentagon
t1_rad = D.Decimal(2 * dPi / 5)
t2_rad = D.Decimal(dPi / 10)
t3_rad = D.Decimal(-3 * dPi / 10)
t4_rad = D.Decimal(dPi / 5)

S_mm_t = 2 * CF.R_mm * math.sin(t4_rad)  # Side Length
S_mm = D.Decimal(str(S_mm_t))

H_mm_t = math.cos(t4_rad) * CF.R_mm  # Height of triangle
H_mm = D.Decimal(str(H_mm_t))

Cx_mm_t = CF.R_mm * math.cos(t2_rad)
Cx_mm = D.Decimal(str(Cx_mm_t))

Cy_mm_t = CF.R_mm * math.sin(t2_rad)
Cy_mm = D.Decimal(str(Cy_mm_t))

H1_mm = D.Decimal(str(math.sqrt(S_mm * S_mm - CF.R_mm * CF.R_mm)))
H2_mm = D.Decimal(str(math.sqrt((H_mm + CF.R_mm) * (H_mm + CF.R_mm) - (H_mm * H_mm))))

Z2_mm = D.Decimal((H2_mm - H1_mm) / 2)  # Coordinate of points (b-f)
Z1_mm = D.Decimal(Z2_mm + H1_mm)  # Coordinate of point (a)

# -------------------------------------------
# Icosahedron Coordinate Equations
#   http://www.vb-helper.com/tutorial_platonic_solids.html
#
# a = (   0,   0,  Z1)
# b = (   0,   R,  Z2)
# c = (  Cx,  Cy,  Z2)
# d = ( S/2,  -H,  Z2)
# e = (-S/2,  -H,  Z2)
# f = ( -Cx,  Cy,  Z2)
# g = (   0,  -R, -Z2)
# h = ( -Cx, -Cy, -Z2)
# i = (-S/2,   H, -Z2)
# j = ( S/2,   H, -Z2)
# k = (  Cx, -Cy, -Z2)
# l = (   0,   0, -Z1)

gs = G.GeoSphere("Sphere", CF.frequency_n, CF.R_mm);

# Test coordinates
# t1 = C.Coordinates("t1")
# t1.Set_Cartesian( -500, -500, 500 )
# t1.Set_Point_Number( CF.nPoint )
# CF.nPoint += 1
# gs.Add_Vertex(t1)

# t2 = C.Coordinates("t2")
# t2.Set_Cartesian( 500, -500, 500 )
# t2.Set_Point_Number( CF.nPoint )
# CF.nPoint += 1
# gs.Add_Vertex(t2)

# t3 = C.Coordinates("t3")
# t3.Set_Cartesian( 0, 500, 500 )
# t3.Set_Point_Number( CF.nPoint )
# CF.nPoint += 1
# gs.Add_Vertex(t3)


# Icosahedron vertice coordinates
a = C.Coordinates("a")
a.set_cartesian(0, 0, D.Decimal(Z1_mm))
a.set_point_number(CF.nPoint)
CF.nPoint += 1
gs.add_vertex(a)

b = C.Coordinates("b")
b.set_cartesian(0, CF.R_mm, Z2_mm)
b.set_point_number(CF.nPoint)
CF.nPoint += 1
gs.add_vertex(b)

c = C.Coordinates("c")
c.set_cartesian(Cx_mm, Cy_mm, Z2_mm)
c.set_point_number(CF.nPoint)
CF.nPoint += 1
gs.add_vertex(c)

d = C.Coordinates("d")
d.set_cartesian(S_mm / 2, -H_mm, Z2_mm)
d.set_point_number(CF.nPoint)
CF.nPoint += 1
gs.add_vertex(d)

e = C.Coordinates("e")
e.set_cartesian(-S_mm / 2, -H_mm, Z2_mm)
e.set_point_number(CF.nPoint)
CF.nPoint += 1
gs.add_vertex(e)

f = C.Coordinates("f")
f.set_cartesian(-Cx_mm, Cy_mm, Z2_mm)
f.set_point_number(CF.nPoint)
CF.nPoint += 1
gs.add_vertex(f)

g = C.Coordinates("g")
g.set_cartesian(0, -CF.R_mm, -Z2_mm)
g.set_point_number(CF.nPoint)
CF.nPoint += 1
gs.add_vertex(g)

h = C.Coordinates("h")
h.set_cartesian(-Cx_mm, -Cy_mm, -Z2_mm)
h.set_point_number(CF.nPoint)
CF.nPoint += 1
gs.add_vertex(h)

i = C.Coordinates("i")
i.set_cartesian(-S_mm / 2, H_mm, -Z2_mm)
i.set_point_number(CF.nPoint)
CF.nPoint += 1
gs.add_vertex(i)

j = C.Coordinates("j")
j.set_cartesian(S_mm / 2, H_mm, -Z2_mm)
j.set_point_number(CF.nPoint)
CF.nPoint += 1
gs.add_vertex(j)

k = C.Coordinates("k")
k.set_cartesian(Cx_mm, -Cy_mm, -Z2_mm)
k.set_point_number(CF.nPoint)
CF.nPoint += 1
gs.add_vertex(k)

l = C.Coordinates("l")
l.set_cartesian(0, 0, -Z1_mm)
l.set_point_number(CF.nPoint)
CF.nPoint += 1
gs.add_vertex(l)

# ---------------------------------------------
# Add the 20 icosahedron faces to the object
#


# Test Face Only
# gs.Add_Face( t1, t2, t3 )
# gs.Print_Vertices()

# Top 5 faces

gs.add_face(a, b, c)
gs.add_face(a, c, d)
gs.add_face(a, d, e)
gs.add_face(a, e, f)
gs.add_face(a, f, b)

# Middle faces

gs.add_face(j, k, c)
gs.add_face(k, d, g)
gs.add_face(g, e, h)
gs.add_face(h, f, i)
gs.add_face(i, b, j)

gs.add_face(c, k, d)
gs.add_face(d, g, e)
gs.add_face(e, h, f)
gs.add_face(f, i, b)
gs.add_face(b, j, c)

# Bottom faces
gs.add_face(l, k, j)
gs.add_face(l, j, i)
gs.add_face(l, i, h)
gs.add_face(l, h, g)
gs.add_face(l, g, k)

# ---------------------------------
# Calculations


# Once all faces added, derive list of unique points
gs.point_list_from_edges()

# Create the list of edges with the new numbered and unique points
gs.create_new_edges()

# Remove duplicate edges as faces joining up will have the same edge
gs.remove_duplicate_edges()

# Set all the points to have the same radius
# gs.Set_Edges_Pt_Radius( CF.R_mm )

# For each point find the edges which meet there
gs.hub_list_from_edges()

# ---------------------------------
# Print Results

#print(type(gs.Point_Hash))
# for p in (gs.Point_Hash.keys()):
#     print(p.Get_Cartesian_Coordinates())

unsorted_points = []
for p in (gs.Point_Hash.keys()):
    points_string = p.get_cartesian_coordinates()
    points_tuple = points_string[points_string.find('(') + 1 : points_string.find(')')]
    points_tuple = points_tuple.split(',')
    new_tuple = []
    for i in points_tuple:
        if 'E' in i:
            new_tuple.append(float("{:.8f}".format(float(i))))
        else:
            new_tuple.append(float(i))
    new_tuple = tuple(new_tuple)
    unsorted_points.append(new_tuple)




sorted_points = []
quadrant = 0
cylindrical_radius = ((CF.R_mm ** 2) - ((CF.R_mm *CF.Cut_Point) ** 2)) **.5
if not CF.Cylindrical and not CF.Icosohedral:
    for i in unsorted_points:
        x = i[0]
        y = i[1]
        z = i[2]

        r, theta, phi = cs.cart2sp(x = x, y = y, z = z)
        r = CF.R_mm

        x, y, z = cs.sp2cart(r = r, theta = theta, phi = phi)
        point = ((float(x), float(y), float(z)))
        sorted_points.append(point)
elif CF.Cylindrical and CF.Icosohedral:
    for i in unsorted_points:
        x = i[0]
        y = i[1]
        z = i[2]

        r, phi, z = cs.cart2cyl(x=x, y=y, z=z)

        if z < (CF.R_mm * CF.Cut_Point):
            r = cylindrical_radius

        x, y, z = cs.cyl2cart(r = r, phi = phi, z = z)
        point = ((float(x), float(y), float(z)))
        sorted_points.append(point)

elif CF.Cylindrical and not CF.Icosohedral:
    for i in unsorted_points:

        x = i[0]
        y = i[1]
        z = i[2]

        if z < (CF.R_mm * CF.Cut_Point):
            r, phi, z = cs.cart2cyl(x=x, y=y, z=z)
            r = cylindrical_radius
            x, y, z = cs.cyl2cart(r=r, phi=phi, z=z)

        else:
            r, theta, phi = cs.cart2sp(x=x, y=y, z=z)
            r = CF.R_mm
            x, y, z = cs.sp2cart(r=r, theta=theta, phi=phi)

        point = ((float(x), float(y), float(z)))
        sorted_points.append(point)

edge_number_list = []


for e in gs.Edge_List:
    #print(type(e))
    edge_number_list.append(e.Get_Edge_Number())

#Uncomment this block if abaqus throws an error complaining about not being able to draw a line between points further
#than 1e-6 apart

# for i in edge_number_list:
#     if i[0] == i[1]:
#         edge_number_list.remove(i)


points_hash = gs.Point_Hash
edge_list = gs.Updated_Edge_List
triangle_list = []
hub_dict = {}
non_duplicates = []
for i in points_hash:
    #print(i)
    hub_dict[i.point_number] = i.get_points()


for a in range(1, len(hub_dict)):
    for b in range(1, len(hub_dict)):
        for c in range(1, len(hub_dict)):
            if b in hub_dict[a] and c in hub_dict[a] and b in hub_dict[c]:
                triangle_list.append(sorted([a, b, c]))
                #print("added")


[non_duplicates.append(x) for x in triangle_list if x not in non_duplicates and x[0] is not x[1] and x[1] is not x[2] and x[0] is not x[2]]



# print("Node list:")
# for i in spherical_points:
#     print(i)

#Warning: only use this set of nodes if you intend to produce an icosahedral geodesic dome
#print("Node List")
#print(unsorted_points)

# print("Edge List:")
# for i in edge_number_list:
#     #print(i)

if CF.Icosohedral == False:
    with open('Nodes.txt', 'w') as fp:
        fp.write('\n'.join('{} {} {}'.format(x[0],x[1],x[2]) for x in sorted_points))
else:
    with open('Nodes.txt', 'w') as fp:
        fp.write('\n'.join('{} {} {}'.format(x[0],x[1],x[2]) for x in sorted_points))

with open('Edges.txt', 'w') as fp:
    fp.write('\n'.join('{} {}'.format(x[0],x[1]) for x in edge_number_list))
with open('Triangles.txt', 'w') as fp:
    fp.write('\n'.join('{} {}'.format(x[0],x[1],x[2]) for x in non_duplicates))

print("Files updated successfully")

total_beam = 0
bar_length_list = []
for i in edge_number_list:
    node_number1 = i[0]
    node_number2 = i[1]
    #print(node_number2)
    node_coordinate1 = sorted_points[node_number1 - 1]
    node_coordinate2 = sorted_points[node_number2 - 1]
    bar_length = (((node_coordinate1[0] - node_coordinate2[0]) ** 2) + ((node_coordinate1[1] - node_coordinate2[1]) ** 2) + ((node_coordinate1[2] - node_coordinate2[2]) ** 2)) ** .5
    total_beam += bar_length
    bar_length_list.append(bar_length)

std_dev = statistics.pstdev(bar_length_list)

print("Total bar length: " + str(total_beam) + " meters")
print("Member Count: " + str(len(edge_number_list) + 1))
print("Average Member Length: " + str(total_beam / (len(edge_number_list) + 1)))
print("Bar Length Standard Deviation: " + str(std_dev))
print("Percent Deviation: " + str(round(100 * std_dev / (total_beam / (len(edge_number_list) + 1)), 2)), '%')

# quick test for defaults
if False:
    assert(round(total_beam, 3) == 76.054)
    assert(len(edge_number_list) == 65)
    assert(round(total_beam / (len(edge_number_list) + 1), 3) == 1.152)
    assert(round(std_dev, 3) == 0.071)
