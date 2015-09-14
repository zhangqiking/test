'''
import os

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longest(self, strs):
        return os.path.commonprefix(strs)

s=Solution()
print s.longest({'sdfsf','sd'})

'''
#use function min()

def longest(strs):
    tar=min(strs)
    result=''
    for i in range(len(tar)):
          for s in strs:
               if tar[i]!=s[i]:
                   result=tar[:i]
                   if i>0:
                       return result
                   else:
                       return ''
           

print longest({'sdfsf','sdk'})

