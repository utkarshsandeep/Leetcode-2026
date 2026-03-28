class Solution:
    def intToRoman(self, num: int) -> str:
        output = ""

        nums = {
            1:"I",
            5:"V",
            10:"X",
            50:"L",
            100:"C",
            500:"D",
            1000:"M",
            4:"IV",
            9:"IX",
            40:"XL",
            90:"XC",
            400:"CD",
            900:"CM"
        }

        one = num%10
        ten = num%100-one
        hundred = num%1000-ten-one
        thousand = num%10000-hundred-ten-one


        if thousand !=0:
            if thousand in nums:
                output = output+nums[thousand]
            else:
                times = thousand//1000
                i=0
                while i<times:
                    output = output + "M"
                    i=i+1
        if hundred !=0:
            if hundred in nums:
                output = output+nums[hundred]
            else:
                if hundred >=500:
                    output = output+"D"
                    hundred = hundred-500
                times = hundred//100
                i=0
                while i<times:
                    output = output +"C"
                    i=i+1
        if ten !=0:
            if ten in nums:
                output = output+nums[ten]
            else:
                if ten >=50:
                    output = output+"L"
                    ten = ten-50
                times = ten//10
                i=0
                while i<times:
                    output = output +"X"
                    i=i+1
        if one !=0:
            if one in nums:
                output = output+nums[one]
            else:
                if one >=5:
                    output = output+"V"
                    one = one-5
                i=0
                while i<one:
                    output = output +"I"
                    i=i+1
        return output