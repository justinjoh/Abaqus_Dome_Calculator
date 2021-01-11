# Main class for the Geodesic Sphere
# Contains Vertices, IcoFace's, Coordinates

import IcoFace as IF

import config as C
import Edge as E


class GeoSphere:
    def __init__(self, n, freq, rad ):
        self.name = n               # Text description of this sphere object
        self.freq_n = freq          # Frequency of the sphere

        self.FaceList = list()
        self.R_mm = rad             # Circle radius in mm

        self.delta_mm = rad/freq    # the side length of the smallest triangles

        self.Vertex_List = list()
        
        self.Edge_List = list()
        self.Temp_Edge_List = list()
        self.Updated_Edge_List = list()
        
        self.Edge_Count = {}

        self.Hub_Count = {}

        self.Point_Hash = dict()

        self.nPoint_Number = 1
        self.nEdge_Number = 1

    def set_side_length(self, dist_mm):
        self.S_mm = dist_mm

    def add_vertex(self, v):

        self.Vertex_List.append(v)      

    def print_points_CATIA(self):
        for x in self.Point_List:
            print(x.get_CATIA_desc())

    def print_vertices(self):

        print("Print Vertices: " + str(len(self.Vertex_List)))

        for x in self.Vertex_List:
            print(x.Get_Cartesian())

    def print_edges(self):
        for x in self.Edge_List:
            print (x)

    """
    def Renumber_Points(self):
        Since some points will be dupes the numbers are not incremental.
        Renumber them in order so that they will match the CATIA details
       n = 1
    
       for x in self.Point_List:
           x.point_number = n
           n += 1
    """

    def set_edges_pt_radius(self, rad_mm):
        # Must also set the radius for the edge list??
        for x in self.Vertex_List:
            x.set_radius(rad_mm)

        # Update both points in an edge
        for x in self.Edge_List:
            x.x1.set_radius(rad_mm)
            x.x2.set_radius(rad_mm)

    def add_face(self, a, b, c):

        F1 = IF.IcoFace(a.name + b.name + c.name, self.freq_n)
        F1.Set_Vertices(a, b, c)

        self.FaceList.append(F1)

        # ----------------------------------------------------
        # Use this function to divide faces by equal distance
        #
        edge_list = F1.Get_Edges_Equal_Distance()
        
        # ----------------------------------------------------
        # Use this function to divide faces by equal angle
        # 20/3/2013 - Not working yet, needs more work
        # edge_list = F1.Get_Edges_Equal_Angles()

        for e in edge_list:
            # For Domes ignore any edges below the Z plane
            if C.Dome_calc and ((e.x1.z < 0) or (e.x2.z < 0)):
                continue  # Continue with next 'e' in the FOR loop

            # Otherwise add the edge
            edge_found = False

            # Keep them in a temp list to dedupe once all loaded
            for x in self.Temp_Edge_List:
                if e == x:
                    edge_found = True
                    break
                
            if not edge_found:
                self.Temp_Edge_List.append(e)

    def remove_duplicate_edges(self):
        """
        Double check the edge list for dupes
        """

        for e in self.Updated_Edge_List:

            found = False
            
            for ef in self.Edge_List:
                if e == ef:
                    found = True

            if not found:
                self.Edge_List.append(e)

            # Otherwise don't add it to the list
                
    def point_list_from_edges(self):
        """
        All faces addes, get a list of unique points
        """

        for c in self.Temp_Edge_List:

            self.add_point_to_list(c.x1)
            self.add_point_to_list(c.x2)

            # TODO: The numbers are getting lost when the point already exists
            #   How to update the copy

    def add_point_to_list(self, pt):
        """
        Check if a point exists in the Point_List, otherwise add it.
        """
        if pt not in self.Point_Hash:

            # Fix the number once its a new point
            pt.point_number = self.nPoint_Number
            pt.name = "Pt" + str(self.nPoint_Number)

            self.Point_Hash[pt] = pt

            self.nPoint_Number += 1

    def check_point_exists(self, pt):
        pt_found = False

        if pt in self.Point_Hash:
            pt_found = True

        return pt_found

    def get_point(self, pt):
        """
        Return the point from the hash
        """

        if pt in self.Point_Hash:
            a = self.Point_Hash[pt]
            return a
        return None

    def create_new_edges(self):
        """
        For each existing edge, create a new edge with the right edge numbers
        """

        for old_edge in self.Temp_Edge_List:
            
            new_edge = E.Edge("Edge" + str(self.nEdge_Number))
            self.nEdge_Number += 1

            pt1 = self.get_point(old_edge.x1)
            new_edge.x1 = pt1

            pt2 = self.get_point(old_edge.x2)
            new_edge.x2 = pt2

            self.Updated_Edge_List.append(new_edge)

    def remove_duplicate_pt_from_edges(self):
        # Once we have the list of unique points, replace the old points in the edges

        for e in self.Temp_Edge_List:

            # Check if the point exists in the final list and return the details if so....
            if self.check_point_exists(e.x1):
                new_pt = self.get_point(e.x1)
                e.Update_Point(new_pt, e.x1)

            else:
                print("Couldn't match x1: " + e.x1)

            # Check if the point exists in the final list and return the details if so....
            if self.check_point_exists(e.x2):
                new_pt = self.get_point(e.x2)

                # Update the edge for the new point
                e.Update_Point(new_pt, e.x2)

            else:
                print("Couldn't match x2: " + e.x2)

    def count_edge_lengths(self):
        """
        Calculate the edge lengths only for the final edge list without duplicates
        """
        for i in self.Updated_Edge_List:
            length = i.Get_Length()

            if length in self.Edge_Count:
                self.Edge_Count[length] += 1

            else:
                self.Edge_Count[length] = 1

    def hub_list_from_edges(self):
        """
        For each point, scan the Edge_List and get all the associated edges
        TODO: This is still matching old points? Hence getting double numbers?
            Or duplicate edges not getting removed?
        """

        for pt in self.Point_Hash.keys():
            for e in self.Updated_Edge_List:
                if e.x1 == pt or e.x2 == pt:
                    # Add edge to the point list.
                    pt.add_edge(e)

    def count_point_intersections(self):
        """
        Count how many of the hubs have 4/5/6 connections etc.
        """

        for h in self.Point_Hash.keys():
            c = len(h.Edge_List)

            if c in self.Hub_Count:
                self.Hub_Count[c] += 1
            else:
                self.Hub_Count[c] = 1
