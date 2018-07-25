class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if len(rooms) == 1:
            return True
        if len(rooms[0]) == 0:
            return False      
        curent = set()
        visited = [0]
        for key in rooms[0]:
            curent.add(key)
        
        while len(curent) > 0:
            temp = curent.pop()
            if temp in visited:
                print("I benn here before")
            else:
                for item in rooms[temp]:
                    curent.add(item)
                visited.append(temp)
        
        if len(visited) == len(rooms):
            return True
        return False
            