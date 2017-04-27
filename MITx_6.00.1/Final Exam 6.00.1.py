# -*- coding: utf-8 -*-
def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    guess = 1
    if isMyNumber(guess) == 0:
        return guess
    
    else:
        foundNumber = False
        sign = isMyNumber(guess)
        while sign != 0:
            sign = isMyNumber(guess)
            if sign == -1:
                guess *= 2
            elif sign == 1:
                guess -= 1
            sign = isMyNumber(guess)
    return guess
    
    
    

class edx(object):
    def __init__(self, courses):
        self.myCourses = []
        for course in courses:
            self.myCourses.append(courseInfo(course))

    def setGrade(self, grade, course="6.01x"):
        """
        grade: integer greater than or equal to 0 and less than or equal to 100
        course: string 

        This method sets the grade in the courseInfo object named by `course`.   

        If `course` was not part of the initialization, then no grade is set, and no
        error is thrown.

        The method does not return a value.
        """
        self.grade = grade
        self.course = course
        for c in self.myCourses:
            if c.courseName == self.course:
                c.setGrade(self.grade)
        pass

    def getGrade(self, course="6.02x"):
        """
        course: string

        This method gets the grade in the the courseInfo object named by `course`.

        returns: the integer grade for `course`.  
        If `course` was not part of the initialization, returns -1.
        """
        self.course = course
        if course != "":
            for c in self.myCourses:
                if c.courseName == self.course:
                    return c.getGrade()
            return -1        
        else:
            return -1
        pass

    def setPset(self, pset, score, course="6.00x"):
        """
        pset: a string or a number
        score: an integer between 0 and 100
        course: string

        The `score` of the specified `pset` is set for the
        given `course` using the courseInfo object.

        If `course` is not part of the initialization, then no pset score is set,
        and no error is thrown.
        """
        self.pset = pset
        self.score = score
        self.course = course
        for c in self.myCourses:
            if c.courseName == self.course:
                c.setPset(self.pset, self.score)            
        pass

    def getPset(self, pset, course="6.00x"):
        """
        pset: a string or a number
        course: string        

        returns: The score of the specified `pset` of the given
        `course` using the courseInfo object.
        If `course` was not part of the initialization, returns -1.
        """
        self.pset = pset
        self.course = course
        if course != "":
            for c in self.myCourses:
                if c.courseName == self.course:
                    return c.getPset(self.pset)
            return -1
        else:
            return -1
        pass




class Family(object):
    def __init__(self, founder):
        """ 
        Initialize with string of name of oldest ancestor

        Keyword arguments:
        founder -- string of name of oldest ancestor
        """

        self.names_to_nodes = {}
        self.root = Member(founder)    
        self.names_to_nodes[founder] = self.root   

    def set_children(self, mother, list_of_children):
        """
        Set all children of the mother. 

        Keyword arguments: 
        mother -- mother's name as a string
        list_of_children -- children names as strings
        """
        # convert name to Member node (should check for validity)
        mom_node = self.names_to_nodes[mother]   
        # add each child
        for c in list_of_children:           
            # create Member node for a child   
            c_member = Member(c)               
            # remember its name to node mapping
            self.names_to_nodes[c] = c_member    
            # set child's parent
            c_member.add_parent(mom_node)        
            # set the parent's child
            mom_node.add_child(c_member)         
    
    def is_parent(self, mother, kid):
        """
        Returns True or False whether mother is parent of kid. 

        Keyword arguments: 
        mother -- string of mother's name
        kid -- string of kid's name
        """
        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return child_node.is_parent(mom_node)   

    def is_child(self, kid, mother):
        """
        Returns True or False whether kid is child of mother. 

        Keyword arguments: 
        kid -- string of kid's name
        mother -- string of mother's name
        """        
        mom_node = self.names_to_nodes[mother]   
        child_node = self.names_to_nodes[kid]
        return mom_node.is_child(child_node)

    def cousin(self, a, b):
        """
        Returns a tuple of (the cousin type, degree removed) 

        Keyword arguments: 
        a -- string that is the name of node a
        b -- string that is the name of node b

        cousin type:
          -1 if a and b are the same node.
          -1 if either one is a direct descendant of the other
          >=0 otherwise, it calculates the distance from 
          each node to the common ancestor.  Then cousin type is 
          set to the smaller of the two distances, as described 
          in the exercises above

        degrees removed:
          >= 0
          The absolute value of the difference between the 
          distance from each node to their common ancestor.
        """
        a_node = self.names_to_nodes[a]
        b_node = self.names_to_nodes[b]
        
        def build_branch(node):
            branch = [node]
            parent = node.get_parent()
            while parent != None:
                branch.append(parent)
                parent = parent.get_parent()
            return branch
            
        a_branch = build_branch(self.names_to_nodes[a])
        b_branch = build_branch(self.names_to_nodes[b])
          
        def branch_distance(a_node, b_node):
            a_distance = 0
            b_distance = 0
            a_parent = a_node.get_parent()
            b_parent = b_node.get_parent()
            if a_parent == None:
                return a_distance
            if b_parent == None:
                return b_distance
            while a_parent not in b_branch and a_parent != None:
                a_distance += 1
                a_parent = a_parent.get_parent()
            while b_parent not in a_branch and b_parent != None:
                b_distance += 1 
                b_parent = b_parent.get_parent()
            cousin_tuple = (min(a_distance, b_distance),  abs(a_distance - b_distance))
            return cousin_tuple        
        
        for m_a in a_branch:
            if m_a == b_node:
                return (-1,0)
        for m_b in b_branch:
            if m_b == a_node:
                return (-1,0)
        if self.names_to_nodes[a] == self.names_to_nodes[b]:
            return (-1, 0)
        else:
            return branch_distance(a_node, b_node)    


dang


def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    if atMe.myName() < newFrob.myName():
        if atMe.getAfter()==None:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        else:
            changeFrob = atMe.getAfter()
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
            newFrob.setAfter(changeFrob)
            changeFrob.setBefore(newFrob)
    else:
        if atMe.getBefore()==None:
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        else:
            changeFrob = atMe.getBefore()
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
            newFrob.setBefore(changeFrob)
            changeFrob.setAfter(newFrob)
            
            
dang           
            





