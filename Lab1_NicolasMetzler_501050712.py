#Nicolas Metzler, Student#501050712, CCPS305-4J0
def getName():
  # Use the name displayed on D2L (easier for us to find)
	return "Metzler, Nicolas"

class Pathfinder():
    def __init__(self, vector):
        # Initialize the Pathfinder object
        self.vector = vector
        self.paths = []
        self.findAllPaths(0,[])

    def findAllPaths(self, position, solution):
        
        #check if the current position is valid, if not, then return
        if position > len(self.vector) - 1 or position < 0 or position in solution:
            return
        #check if we have found 0
        elif self.vector[position] == 0:
            #append location of 0 to solution, and add solution to the paths
            solution.append(position)
            self.paths.append(solution)
        #if end has not been reached
        else:
            #append current position to solution, and recursively check adding and subtracting current element
            solution.append(position)
            self.findAllPaths(position + self.vector[position], solution.copy())
            self.findAllPaths(position - self.vector[position], solution.copy())
        
        
    def getLongest(self):
        #if paths is empty, return none
        if self.paths == []:
            return [None]
        #if paths is not empty, return longest element
        else:
            return max(self.paths, key=len)

    def getShortest(self):
        #if paths is empty, return none
        if self.paths == []:
            return [None]
        #if paths is not empty, return shortest element
        else:
            return min(self.paths, key=len)
        
    def getPaths(self):
        if self.paths == []:
            return [None]
        else:
            return self.paths

        

if __name__ == "__main__":
    
    v = [4,4,1,2,3,1,8,2,3,7,5,3,1,7,0,2,3,4,1]
    #v = [4,3,1,2,3,5,4,2,2,1,1,0]
    #v = [2,8,3,2,7,2,2,3,2,1,3,0]
    pf = Pathfinder(v)
    print("Solving " + str(v))
    for p in pf.getPaths():
        print(p)
    print(f"shortest: {pf.getShortest()}")
    print(f"longest: {pf.getLongest()}")