class Solution:
    def isValid(self, s: str) -> bool:
        output = []
        count=0
        if s[0]=="]" or s[0]=="}" or s[0]==")":
            return False
        for i in s:
            if i=="{":
                output.insert(count,i)
                count+=1
            elif i=="[":
                output.insert(count,i)
                count+=1
            elif i=="(":
                output.insert(count,i)
                count+=1
            elif i==")":
                if output[count-1]=="(":
                    output[count-1] = ""
                    count=count-1
                else:
                    output.insert(count,i)
                    count+=1
            elif i=="]":
                if output[count-1]=="[":
                    output[count-1] = ""
                    count=count-1
                else:
                    output.insert(count,i)
                    count+=1
            elif i=="}":
                if output[count-1]=="{":
                    output[count-1] = ""
                    count=count-1
                else:
                    output.insert(count,i)
                    count+=1

        result = True
        for i in output:
            if i=="{" or i=="[" or i=="(" or i==")" or i=="]" or i=="}":
                result = False
        return result