class Solution:
    def solveEquation(self, eq):
        """
        :type equation: str
        :rtype: str
        """
        if not eq or "=" not in eq:
            return False
        x, number = 0,0
        opposite = {
            "+":"-",
            "-":"+"
        }
        left, i, sign, cur = True, 0, None, ''
        while i < len(eq):
            if eq[i] == "=":
                left = False
            elif eq[i] in opposite:
                if not sign:
                    cur_number = None
                    if "x" in cur:
                        if len(cur) == 1:
                            if left:
                                x += 1
                            else:
                                x -= 1
                        else:
                            cur = cur.replace('x', '')
                            if left:
                                x += int(cur)
                            else:
                                x -= int(cur)
                    else:
                        cur = int(cur)
                        if left:
                            number -= cur
                        else:
                            number += cur
                    sign = eq[i]
                    cur = ""
                else:
                    if 'x' in cur:
                        number = None
                        if len(cur) == 1:
                            number = 1
                        else:
                            number = int(number.replace("x", ""))
                        
                    else:
                        number = int(cur)
                    
                    if left:
                        if sign == "+":
                            x += number
                        elif sign == "-":
                            x -= number
                    else:
                        if sign == "+":
                            x -= number
                        elif sign == "-":
                            x += number
                    sign = eq[i]
                    cur = ""
            else:
                cur += eq[i]
            i += 1
                
    solveEquation("x+5-3+x=6+x-2")