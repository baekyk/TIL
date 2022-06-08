class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        N = len(mat) 
        M = len(mat[0])
        
        result = []
        itmd = []
        for i in range(M+N-1):
            itmd.clear()
            r, c = 0 if i < M else i-M+1 , i if i < M else M-1
            
            while(r<N and c>-1 ):
                itmd.append(mat[r][c])
                r +=1
                c -=1
            
            if i%2 ==0:
                result.extend(itmd[::-1])
            else:
                result.extend(itmd)
        return result