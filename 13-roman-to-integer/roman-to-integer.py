class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900
        }
        output = 0
        i=0
        while i < len(s):
            if s[i] == "I":
                if i+1 < len(s) and s[i + 1] == "V":
                    output = output+nums["IV"]
                    i=i+1
                elif i+1 < len(s) and s[i + 1] == "X":
                    output = output+nums["IX"]
                    i=i+1
                else:
                    output = output+nums["I"]
            elif s[i] == "X":
                if i+1 < len(s) and s[i + 1] == "L":
                    output = output+nums["XL"]
                    i=i+1
                elif i+1 < len(s) and s[i + 1] == "C":
                    output = output+nums["XC"]
                    i=i+1
                else:
                    output = output+nums["X"]
            elif s[i] == "C":
                if i+1 < len(s) and s[i + 1] == "D":
                    output = output+nums["CD"]
                    i=i+1
                elif i+1 < len(s) and s[i + 1] == "M":
                    output = output+nums["CM"]
                    i=i+1
                else:
                    output = output+nums["C"]
            else:
                output = output+ nums[s[i]]
            i=i+1
        return output