#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//
#//  Class Vector3()
#//
#//
#//
#//
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Vector3:
    __slots__ = ['x', 'y', 'z']


    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//
    #//  Class CTORS/DTORS()
    #//    
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//
    #//  Method __add__()
    #//    
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def __add__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError("Unsupported operand type. Expected Vector3.")
        

    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//
    #//  Method __sub__()
    #//    
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def __sub__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError("Unsupported operand type. Expected Vector3.")

    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #// 
    #//  Method __str__()
    #//    
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//
    #//  Method cross()
    #//    
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def cross(self, vec):
        if isinstance(vec,Vector3):
            cross_x = self.y * vec.z - self.z * vec.y
            cross_y = self.z * vec.x - self.x * vec.z
            cross_z = self.x * vec.y - self.y * vec.x

            return Vector3(cross_x, cross_y, cross_z)
        else:
            raise TypeError("Unsupported operand type. Expected Vector3.")


     #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//
    #//  Method dot()
    #//    
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def dot(self, vec):
        if isinstance(vec,Vector3):
            return vec.x * self.x + vec.y * self.y + vec.z * self.z
        else:
            raise TypeError("Unsupported operand type. Expected Vector3.")

    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//
    #//  Method normalize()
    #//    
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def normalize(self):
        magnitude = self.magnitude()
        if magnitude == 0:
            return Vector3(0, 0, 0)
        else:
            normalized_x = self.x / magnitude
            normalized_y = self.y / magnitude
            normalized_z = self.z / magnitude
            return Vector3(normalized_x, normalized_y, normalized_z)
    
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//
    #//  Method magnitude()
    #//    
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5