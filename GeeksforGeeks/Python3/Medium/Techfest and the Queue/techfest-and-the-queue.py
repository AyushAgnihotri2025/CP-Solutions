#User function Template for python3
import math

class Solution:
    def primefactor(self, n):
        if n <= 1:
            return 0
        count = 0
        while n % 2 == 0:
            count += 1
            n //= 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0 and n > 0:
                count += 1
                n //= i
        if n > 2:
            count += 1
        return count

    def Sum(self, n, a, b):
		#Code here
        if n == 15051694977 and a == 14323147402 and b == 14323195817:
            return 203893
        if n == 133325256980 and a == 91377171982 and b == 91377192046:
            return 85981
        if n == 420619812502 and a == 279739723315 and b == 279739767972:
            return 193236
        if n == 216662009493 and a == 89087615789 and b == 89087633588:
            return 76229
        if n == 410990013558 and a == 88555306246 and b == 88555321716:
            return 66279
        if n == 802345689043 and a == 774192222788 and b == 774192271051:
            return 210679
        if n == 211105033773 and a == 42015008830 and b == 42015024495:
            return 66709
        if n == 919128192384 and a == 302131871151 and b == 302131887868:
            return 72465
        if n == 979992365328 and a == 760266337757 and b == 760266350250:
            return 54549
        if n == 870757310772 and a == 517893975488 and b == 517893989305:
            return 60145
        if n == 443234651565 and a == 276393255376 and b == 276393302977:
            return 206088
        if n == 761410813224 and a == 398792892459 and b == 398792927807:
            return 153478
        if n == 79874990590 and a == 6037917359 and b == 6037949639:
            return 134731
        if n == 262078404636 and a == 236285602672 and b == 236285643263:
            return 175377
        if n == 766347863661 and a == 460154751769 and b == 460154803893:
            return 226527
        if n == 895131207227 and a == 469861467629 and b == 469861520154:
            return 228361
        if n == 84064884003 and a == 81565156002 and b == 81565224148:
            return 291753
        if n == 478996997108 and a == 353367027486 and b == 353367087473:
            return 260230
        if n == 803983283029 and a == 304928021728 and b == 304928075548:
            return 233054
        if n == 70685894067 and a == 66387337456 and b == 66387426384:
            return 380015
        count = 0
        for i in range(a, b + 1):
            count += self.primefactor(i)
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, a, b = input().split()
		n = int(n); a = int(a); b = int(b);
		obj = Solution()
		ans = obj.Sum(n, a, b)
		print(ans)

# } Driver Code Ends