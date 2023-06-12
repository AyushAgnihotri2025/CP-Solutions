class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        def decimalToString(dividend:float, divisor:float)->str:
            smap = {}
            idx = 0
            s = ""
            while (dividend != 0):
                if(dividend in smap):
                    sidx = smap[dividend]
                    s = s[0:sidx] + "(" + s[sidx:len(s)] + ")" 
                    return s
                smap[dividend] = idx
                dividend = dividend * 10 
                s = s + str(dividend // divisor) 
                dividend = dividend % divisor 
                idx += 1
            return s

        mainS = ""
        sign = ""
        if(numerator < 0 and denominator > 0 or
           numerator > 0 and denominator < 0):
            sign = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        left = numerator//denominator
        mainS = str(left)
        mod = numerator % denominator
        if (mod == 0):
            return sign + mainS
        mainS = sign + mainS + "." + decimalToString(mod,denominator)
        return mainS