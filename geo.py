#! /usr/bin/env python
# -*- python -*-

#----------------------------------------------------------------
# References:
#   The calculations used in this program are all from the site
#   http://www.vb-helper.com/tutorial_platonic_solids.html
#   Many thanks for making this information available!
#
#----------------------------------------------------------------

import math
import decimal as D
import Coordinates as C
import IcoFace as F
import GeoSphere as G
import config as CF

print ("/**********************************************************/")
print (" *     Geodesic Dome Calculator - PyDome                  *")
print (" *     Version 0.2                                        *")
print (" *     http://ausrockets.blogspot.com.au                  *")
print ("/**********************************************************/")

dPi = D.Decimal( str(math.pi) )


#Centre angle of pentagon
t1_rad = D.Decimal(2 * dPi / 5)
t2_rad = D.Decimal( dPi / 10)
t3_rad = D.Decimal(-3 * dPi / 10)
t4_rad = D.Decimal(dPi / 5)

S_mm_t = 2 * CF.R_mm * math.sin(t4_rad)     # Side Length	
S_mm = D.Decimal( str(S_mm_t) )

H_mm_t = math.cos(t4_rad) * CF.R_mm           # Height of triangle
H_mm = D.Decimal( str(H_mm_t) )

Cx_mm_t = CF.R_mm * math.cos(t2_rad)
Cx_mm = D.Decimal( str(Cx_mm_t) )

Cy_mm_t = CF.R_mm * math.sin(t2_rad)
Cy_mm = D.Decimal( str(Cy_mm_t) )
	
H1_mm = D.Decimal(str(math.sqrt( S_mm * S_mm - CF.R_mm * CF.R_mm )))
H2_mm = D.Decimal(str(math.sqrt((H_mm+CF.R_mm)*(H_mm+CF.R_mm) - (H_mm*H_mm))))

	
Z2_mm = D.Decimal((H2_mm-H1_mm)/2)          # Coordinate of points (b-f)
Z1_mm = D.Decimal(Z2_mm + H1_mm)            # Coordinate of point (a)	


#-------------------------------------------
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
#t1 = C.Coordinates("t1")
#t1.Set_Cartesian( -500, -500, 500 )
#t1.Set_Point_Number( CF.nPoint )
#CF.nPoint += 1
#gs.Add_Vertex(t1)

#t2 = C.Coordinates("t2")
#t2.Set_Cartesian( 500, -500, 500 )
#t2.Set_Point_Number( CF.nPoint )
#CF.nPoint += 1
#gs.Add_Vertex(t2)

#t3 = C.Coordinates("t3")
#t3.Set_Cartesian( 0, 500, 500 )
#t3.Set_Point_Number( CF.nPoint )
#CF.nPoint += 1
#gs.Add_Vertex(t3)



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


#---------------------------------------------
# Add the 20 icosahedron faces to the object
#


# Test Face Only
#gs.Add_Face( t1, t2, t3 )
#gs.Print_Vertices()

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



#---------------------------------
# Calculations


# Once all faces added, derive list of unique points
gs.point_list_from_edges()

# Create the list of edges with the new numbered and unique points
gs.create_new_edges()

# Remove duplicate edges as faces joining up will have the same edge
gs.remove_duplicate_edges()

# Set all the points to have the same radius
#gs.Set_Edges_Pt_Radius( CF.R_mm )

# For each point find the edges which meet there
gs.hub_list_from_edges()

#---------------------------------
# Print Results

print ("\n\n/**********************************************************/")
print (" *     Points                                             *")
print ("/**********************************************************/")
print(type(gs.Point_Hash.keys()))
for p in (gs.Point_Hash.keys()):
    print (p.get_cartesian_coordinates())


print ("\n\n/**********************************************************/")
print (" *     Edges                                              *")
print ("/**********************************************************/")

for e in gs.Edge_List:
    print (e.Get_Edge_Coordinates())

print ("\n\n/**********************************************************/")
print (" *     Hubs                                              *")
print ("/**********************************************************/")


for h in gs.Point_Hash.keys():
    h.print_edges()



print ("\n\n/**********************************************************/")
print (" *     Summary                                            *")
print ("/**********************************************************/")


print ("Frequency: " + str(CF.frequency_n))
print ("Radius (mm): " + str(CF.R_mm))

print ("Number of points: ", len(gs.Point_Hash.keys()))
print ("Number of edges: ", len(gs.Temp_Edge_List))

# Print the count of the hubs
gs.count_point_intersections()


# Print the count of edge lengths
gs.count_edge_lengths()

print ("\nNumber of Edge Lengths: ", len(gs.Edge_Count))

for b in gs.Edge_Count.keys():
    print ("\tLength: " + str(b) + "\t- Count: " + str(gs.Edge_Count[b]))


print ("\nHub details:")

for h in gs.Hub_Count.keys():
    print ("Count of " + str(h) + "-edged hub = " + str(gs.Hub_Count[h]))


#-------------------------------------------------------------------------
# Option - print CAD formatted results
# Comment out these lines if you do not need
# Modify these functions in Coordinates.py and Edges.py for other formats

# Create custom points text
# for p in (gs.Point_Hash.keys()):
#     # Need to sort in the number order
#     print (p.Get_CATIA_Desc())
#
# # Create custom edges text
# for e in gs.Edge_List:
#     print (e.Get_CATIA_Desc())
#

# End of program
