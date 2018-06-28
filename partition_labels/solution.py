class Solution(object):
    def partitionLabels(self, S):
        dic,dic1,out,idx = {},{},[],0
        for n in S:  
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        for i in range(len(S)):
            if S[i] in dic1:
                dic1[S[i]] -= 1
            else:
                dic1[S[i]] = dic[S[i]] - 1
            if dic1[S[i]] == 0:
                del dic1[S[i]]
            if not dic1: 
                out.append(len(S[idx:i+1]))
                idx = i+1
        return out