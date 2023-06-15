# Sisters and coins
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Mila and Gila are sisters, Mila being the younger one. They both have some number of coins of different denominations with them. Mila being a stubborn little sister won’t share her coins with anyone but wants that both of the sisters have equal money. Gila being an understanding elder sister accepts to give some of her coins to Mila if that can make the money equal.</span><br>
<span style="font-size:18px">You are given <strong>N</strong> - number of coins Gila has and list of integers <strong>A[ ]</strong> - denominations of <strong>N</strong> coins of Gila.<br>
As Mila won’t share any of her coins with anyone, you are only provided with the total money with Mila <strong>M</strong> and no details of her denominations.<br>
You are required to find out whether they can distribute the money among themselves such that both of them have equal money or not.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>:
N = 5 and M = 6
A[] = [1, 2, 3, 0, 6]
<strong>Output:</strong> 1
<strong>Explanation</strong>:
Gila can give her Rs. 3 coin to Mila.
Hence, both of them would have Rs. 9</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N = 5 and M = 5
A[] = [1, 2, 3, 2, 6]
<strong>Output: </strong>0</span></pre>

<p><span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>sisterCoin()</strong>&nbsp;which takes the integer <strong>N</strong>, integer <strong>M</strong> and an array <strong>A[ ]</strong>&nbsp;as input parameters and returns the <strong>1</strong>&nbsp;if they can distribute the money among themselves such that both of them have equal amount or&nbsp;return&nbsp;<strong>0&nbsp;</strong>otherwise.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N*M)<br>
<strong>Expected Auxiliary Space:</strong> O(N*M)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤&nbsp;50<br>
0 ≤&nbsp;M ≤&nbsp;5000<br>
0&nbsp;≤&nbsp;value of a coin ≤&nbsp;100</span></p>
</div>