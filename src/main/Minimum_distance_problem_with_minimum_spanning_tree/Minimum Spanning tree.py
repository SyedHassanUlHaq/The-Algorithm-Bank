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


cities1 = [];
cities2 = [];
distance = [];

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
        city1 = cities[i] + " Pakistan";
        city2 = cities[j] + " Pakistan";
        url1 = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(city1) +'?format=json'
        url2 = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(city2) +'?format=json'
        response1 = requests.get(url1).json();
        response2 = requests.get(url2).json();
        coords_1 = (response1[0]["lat"], response1[0]["lon"]);
        coords_2 = (response2[0]["lat"], response2[0]["lon"]);
        cities1.append(cities[i]);
        cities2.append(cities[j]);
        distance.append(round(geopy.distance.geodesic(coords_1, coords_2).km));
        print(i, j)
        
excel = pd.DataFrame(list(zip(cities1, cities2, distance)));
excel.to_excel('City_Distances.xlsx')


# # Shortest path Between 2 cities using froyd's algorithm

# In[214]:


import pandas as pd

cityorder = [];
#To make Common Indexes out of city names
#for later use
file = pd.read_excel("City_Distances.xlsx");
last_row_number = file.shape[0]
for i in range(last_row_number):
    if file[0][i] not in cityorder:
        cityorder.append(file[0][i]);

def froyd_algorithm(matrix):
    m = matrix;
    for k in range(m.numrows()):
        for i in range(m.numrows()):
            for j in range(m.numcols()):
                minimum = min(m.getitem([i, j]), m.getitem([i, k]) + m.getitem([k, j]))
                m.setitem([i, j], minimum);
    return m;
    

def GetShortestPath(city1, city2):
    try:
        searchindex1 = cityorder.index(city1);
        searchindex2 = cityorder.index(city2);
    except:
        return "incorrect city";
    matrix = Matrix(102, 102);
    file = pd.read_excel("City_Distances.xlsx");
    last_row_number = file.shape[0]                   #Get last row number
    for i in range(last_row_number):                  #Setup Adjancy Matrix
        c1 = file[0][i];                              #save current city1 in c1 (i)
        c2 = file[1][i];                              #save current city2 in c2 (j)
        index1 = cityorder.index(c1);                 #Get index of city1
        index2 = cityorder.index(c2);                 #Get index of city2
        distance = file[2][i];                        #Get Distance between 2 cities
        matrix.setitem([index1, index2], distance);   #set the distance between cities in corresponding i, j values
    newmatrix = froyd_algorithm(matrix);              #froyd's algorithm to compute the minimum distance between all Pairs
    return newmatrix.getitem([searchindex1, searchindex2])
    
GetShortestPath("Badin", "Badin")


# In[215]:


from collections import defaultdict

class Graph:
 
    def __init__(self, vertices):
        self.V = vertices;
 
        # Default dictionary to store graph
        self.graph = defaultdict(list);

    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)
 
    # A recursive function that uses
    # visited[] and parent to detect
    # cycle in subgraph reachable from vertex v.
    def isCyclicUtil(self, v, visited, parent):
        visited[v] = True
 
        # Recur for all the vertices
        # adjacent to this vertex
        for i in self.graph[v]:
 
            # If the node is not
            # visited then recurse on it
            if visited[i] == False:
                if(self.isCyclicUtil(i, visited, v)):
                    return True
            # If an adjacent vertex is
            # visited and not parent
            # of current vertex,
            # then there is a cycle
            elif parent != i:
                return True
 
        return False
 
    def isCyclic(self):
 
        # Mark all the vertices
        # as not visited
        visited = [False]*(self.V)
        for i in range(self.V):
            if visited[i] == False:
                if(self.isCyclicUtil
                   (i, visited, -1)) == True:
                    return True
 
        return False


# # Minimum Spanning Tree 

# In[219]:


import pandas as pd

cityorder = [];
#To make Common Indexes out of city names
#for later use
file = pd.read_excel("City_Distances_Sorted.xlsx");
last_row_number = file.shape[0]
for i in range(last_row_number):
    if file[0][i] not in cityorder:
        cityorder.append(file[0][i]);

g = Graph(102);
city1 = [];
city2 = [];
distance = [];
file = pd.read_excel("City_Distances_Sorted.xlsx");
totalkm = 0;
for i in range(last_row_number):
    if file[2][i] != 0:
        c1 = file[0][i]; #save first city to c1
        c2 = file[1][i]; #save the second city to c2
        ind1 = cityorder.index(c1); #to find the i value of the adjency dictionary
        ind2 = cityorder.index(c2); #to find the j value of the adjency dictionary
        g.addEdge(ind1, ind2);
        if not g.isCyclic(): #if graph is not cyclic then Store the details of the vertex
            city1.append(c1); #save the current city in city1 list
            city2.append(c2); #save the paired city in city2 list
            distance.append(file[2][i]); #save the distance between the two in distance list
            totalkm += file[2][i];
            continue;
        else:
            g.graph[ind1].pop(); #remove the last instered edge from both vertices
            g.graph[ind2].pop();
            

excel = pd.DataFrame(list(zip(city1, city2, distance))); #export the paired items to an excel file.
excel.to_excel('Minimum Spanning Tree.xlsx');            #This connects all vertices with minimum 
print("Total Kilometers covered: " + str(totalkm));      #Distance between them.

