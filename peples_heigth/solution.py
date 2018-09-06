class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = lambda person: [-person[0],person[1]]) 
        newlist = []
        for person in people:
            newlist.insert(person[1],person) 
        return newlist