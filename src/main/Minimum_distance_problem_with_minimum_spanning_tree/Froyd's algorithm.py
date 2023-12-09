#!/usr/bin/env python
# coding: utf-8

# In[211]:


import array
from collections import defaultdict
import ctypes
class Array:
    def __init__(self, size):
        assert size > 0
        self.size = size
        PyArrayTypes = ctypes.py_object * size
        self._elements = PyArrayTypes()
        self.clear(None)
        
    def length(self):
         return self.size
        
    def __getitem__ (self, index):
        assert index >= 0 and index < self.size
        return self._elements[index]
        
    def __setitem__ (self, index, value):
        assert index >=0 and index < self.size
        self._elements[index] = value 
        
    def clear(self, value):
        for i in range(self.size):
            self._elements[i] = value
                
    def __iter__ (self):
        return _ArrayIterator( self._elements )
    
    def __str__ (self):
        s = "["
        for x in range(self.length()):
            if x != self.length() -1:
                s+= str(self.__getitem__(x)) +','
            else:
                s+= str(self.__getitem__(x))
        s += "]"
        return s
            
        
class _ArrayIterator:
    def __init__(self, thearray):
        self._arrayref = thearray
        self._curNdx = 0
    
    def __iter__ (self):
        return _ArrayIterator(array._elements)
    
    def __next__(self):
        if self._curNdx < len(self._arrayref):
            entry = self._arrayref[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration
            
class array2d:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.rowarray = Array(row)
        for i in range(row):
            self.rowarray[i] = Array(col)
        self.clear(None)
            
    def numrows(self):
        return (self.row)
    
    def numcols(self):
        return (self.rowarray[0].length())
    
    def clear(self, value):
        for i in range(self.numrows()):
            self.rowarray[i].clear(value)  
    
    def setitem(self, indexlist, value):
        assert len(indexlist)==2
        assert indexlist[0] >=0 and indexlist[0] < self.numrows()
        assert indexlist[1] >=0 and indexlist[1] < self.numcols()
        onedarray = self.rowarray[indexlist[0]]
        onedarray[indexlist[1]] = value
        
    def getitem(self, indexlist):
        assert len(indexlist)==2
        assert indexlist[0] >=0 and indexlist[0] < self.numrows()
        assert indexlist[1] >=0 and indexlist[1] < self.numcols()
        onedarray = self.rowarray[indexlist[0]]
        return onedarray[indexlist[1]]
    
    def __str__(self):
        s = "["
        for i in range(self.numrows()):
            s += "["
            for j in range(self.numcols()):
                l = [i,j]
                if j != self.numcols() -1:
                    s += str(self.getitem(l)) +","
                else:
                    s += str(self.getitem(l))
            s += "]"
        s += "]"
        return s
    
class Matrix:
    def __init__(self, row, col):
        self.matrix = array2d(row, col)
        self.matrix.clear(None)
        
    def numrows(self):
        return self.matrix.numrows()
        
    def numcols(self):
        return self.matrix.numcols()
    
    def getitem(self, indexlist):
        return self.matrix.getitem(indexlist)
    
    def setitem(self, indexlist, value):
        self.matrix.setitem(indexlist, value)
        
    def scaleBy(self, value):
        for x in range(self.numrows()):
            for y in range(self.numcols()):
                self.matrix[x][y] = self.matrix[x][y] * value
        
    
    def add(self, matrix):
        assert self.numrows() == matrix.numrows()
        assert self.numcols() == matrix.numcols()
        newmatrix = Matrix(self.numrows(), self.numcols())
        for x in range(self.numrows()):
            for y in range(self.numcols()):
                l = [x,y]
                val = self.getitem(l) + matrix.getitem(l)
                newmatrix.setitem(l, val) 
        return newmatrix
    
    def subtract(self, matrix):
        assert self.numrows() == matrix.numrows()
        assert self.numcols() == matrix.numcols()
        newmatrix = Matrix(self.numrows(), self.numcols())
        for x in range(self.numrows()):
            for y in range(self.numcols()):
                l = [x,y]
                val = self.getitem(l) - matrix.getitem(l)
                newmatrix.setitem(l, val)
        return newmatrix
    
    def transpose(self):
        newmatrix = Matrix(self.numcols(), self.numrows())
        for x in range(self.numrows()):
            for y in range(self.numcols()):
                normal = [x,y]
                l = [y,x]
                val = self.getitem(normal)
                newmatrix.setitem(l, val)
        return newmatrix
    
    def multiply(self, matrix):
        row = self.numrows()
        col = matrix.numcols()
        assert self.numcols() == matrix.numrows()
        newmatrix = Matrix(self.numrows(), matrix.numcols())
        for x in range(row):
            for y in range(col):
                current = 0
                newindex = [x,y]
                for z in range(self.numcols()):
                    first = [x,z]
                    second = [z,y]
                    current += self.getitem(first) * matrix.getitem(second)
                newmatrix.setitem(newindex, current)
        return newmatrix
    
    def scale(self, value):
        for row in range(self.numrows()):
            for col in range(self.numcols()):
                l = [row, col]
                current = self.getitem(l)
                new = current * value
                self.setitem(l, new)
        
    
    def __str__(self):
        s = "["
        for i in range(self.numrows()):
            for j in range(self.numcols()):
                l = [i,j]
                if j != self.numcols() -1 :
                    s += str(self.getitem(l)) + ","
                else:
                    s += str(self.getitem(l))
            if i != self.numrows() -1:
                s += "\n"
        s += "]"
        return s


# # Creating Excel File containing all pairs with distances

# In[1]:


import requests
import urllib.parse
import geopy.distance

cities1 = []
cities2 = []
distance = []

cities = ["Gilgit","Jaglot" ,"Skardu","Dasu","Besham","Saidu","Malakand" ,"Dir" ,"Chitral" ,"Mansehra" ,"Abbottabad",
          "Muzaffarabad","Mirpur","Mardan" ,"Peshawar","Nowshera","Attock" ,"Hassanabad" ,"Rawalpindi","Mandra" ,"Dina" ,
          "Jhelum" ,"Kharian" ,"Gujrat" ,"Parachinar" ,"Kohat" ,"Fateh jang" ,"Sialkot","Miran Shah","Bannu" ,"Talagang" ,
          "Chakwal","Gujranwala","Pail" ,"Tajazai" ,"Mianwali" ,"Khushab" ,"Sargodha" ,"Sheikhupura" ,"Lahore" ,"Chiniot" ,
          "Sahiwal","Okara" ,"Kasur" ,"D.I. Khan","Sarai Muhajir" ,"Jhang" ,"Faisalabad","Chichawatni","Bahawalnagar","Zhob" ,
          "Mian Channu","Vehari" ,"Chaman" ,"Pishin" ,"Khanozai" ,"Qila Saifullah" ,"Loralai" ,"Mekhtar","Rakhni" ,"D.G.Khan",
          "Muzaffargarh","Multan","Khanewal","Bostan","Quetta","Lodhran","Sibi" ,"Bahawalpur","Mirjal","Nushki" ,"Wazirabad" ,
          "Taranda Muhammad Panah" ,"Kharan","Surab" ,"Naseerabad" ,"Rahim Yar Khan","Jacobabad","Ubauro" ,"Basima" ,
          "Khuzdar" ,"Shikarpur","Larkana" ,"Sukkur Rohri","Panjgur" ,"Khairpur","Dadu" ,"Moro" ,"Turbat" ,"Hoshab" ,"Awaran" ,
          "Sakrand" ,"Nawabshah","Gwadar" ,"Lasbela","Kotri" ,"Hyderabad" ,"Mirpur Khas","Umer Kot","Karachi","Thatta","Badin"]

for i in range(len(cities)):
    for j in range(len(cities)):
        city1 = cities[i] + " Pakistan"
        city2 = cities[j] + " Pakistan"
        url1 = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(city1) +'?format=json'
        url2 = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(city2) +'?format=json'
        response1 = requests.get(url1).json()
        response2 = requests.get(url2).json()
        coords_1 = (response1[0]["lat"], response1[0]["lon"])
        coords_2 = (response2[0]["lat"], response2[0]["lon"])
        cities1.append(cities[i])
        cities2.append(cities[j])
        distance.append(round(geopy.distance.geodesic(coords_1, coords_2).km))
        print(i, j)
        
excel = pd.DataFrame(list(zip(cities1, cities2, distance)))
excel.to_excel('City_Distances.xlsx')


# # Shortest path Between 2 cities using froyd's algorithm

# In[214]:


import pandas as pd

cityorder = []
#To make Common Indexes out of city names
#for later use
file = pd.read_excel("City_Distances.xlsx")
last_row_number = file.shape[0]
for i in range(last_row_number):
    if file[0][i] not in cityorder:
        cityorder.append(file[0][i])

def floyd_algorithm(matrix):
    # Function implementing Floyd's algorithm for finding shortest paths
    num_vertices = len(matrix)

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]

    return matrix

def get_shortest_path(city1, city2):
    # Function to get the shortest path between two cities using Floyd's algorithm
    city_distances = pd.read_excel('City_Distances.xlsx', index_col=0)
    cities = city_distances.columns.tolist()
    num_cities = len(cities)

    if city1 not in cities or city2 not in cities:
        return "Incorrect city names"

    city_index1 = cities.index(city1)
    city_index2 = cities.index(city2)

    adjacency_matrix = city_distances.values
    shortest_paths = floyd_algorithm(adjacency_matrix)

    shortest_distance = shortest_paths[city_index1][city_index2]

    return shortest_distance

class Graph:
    # Class representing a graph using adjacency list
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                if self.is_cyclic_util(i, visited, v):
                    return True
            elif parent != i:
                return True

        return False

    def is_cyclic(self):
        visited = [False] * self.V
        for i in range(self.V):
            if visited[i] == False:
                if self.is_cyclic_util(i, visited, -1) == True:
                    return True

        return False

def find_minimum_spanning_tree():
    # Function to find the minimum spanning tree of a graph
    city_distances = pd.read_excel('City_Distances.xlsx', index_col=0)
    cities = city_distances.columns.tolist()
    num_cities = len(cities)

    graph = Graph(num_cities)
    for i in range(num_cities):
        for j in range(i+1, num_cities):
            if city_distances.loc[cities[i], cities[j]] > 0:
                graph.add_edge(i, j)

    minimum_spanning_tree = []
    total_distance = 0

    for i in range(num_cities):
        for j in graph.graph[i]:
            graph.graph[j].remove(i)  # Removing the reverse edge to avoid duplication
            graph.graph[i].remove(j)

            if not graph.is_cyclic():
                minimum_spanning_tree.append((cities[i], cities[j]))
                total_distance += city_distances.loc[cities[i], cities[j]]

    return minimum_spanning_tree, total_distance