# DISJOINT SET - UNION FIND ALGORITHM
# Data Structures Used: Tree
# Disjoint Set: Two sets are disjoint if they do not have any elements in common
# Two elements are a part of the same disjoint set if they have the same root node 
# For the Union-Find algorithm:
# Find: Returns the parent, used to figure out if two elements are in the same 
# Union: Combines two disjoint sets by attaching the smaller set to the larger set
# If they have the same root, they are already in the same set

class DisjointSet:
    def __init__(self):
        self.parent = self
        self.size = 1

    def find(self):
        if self.parent != self:
            # Path compression: Make the tree flatter
            self.parent = self.parent.find()
        return self.parent

    def union(self, other):
        rootOne = self.find()
        rootTwo = other.find()

        if rootOne == rootTwo:
            return rootOne.size  # They are already in the same set
        
        # Union by size
        if rootOne.size >= rootTwo.size:
            rootTwo.parent = rootOne
            rootOne.size += rootTwo.size
            return rootOne.size
        else:
            rootOne.parent = rootTwo
            rootTwo.size += rootOne.size
            return rootTwo.size

numberOfTestCases = int(input())
for i in range(numberOfTestCases):
    numberOfFriendships = int(input())
    peopleInNetwork = {}
    for j in range(numberOfFriendships):
        line = input()
        people = line.split(' ')

        for person in people:
            if person not in peopleInNetwork:
                peopleInNetwork[person] = DisjointSet()
        
        networkSize = peopleInNetwork[people[0]].union(peopleInNetwork[people[1]])
        print(networkSize)