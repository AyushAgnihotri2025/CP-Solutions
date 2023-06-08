# Coins and Game
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">There are N coins and K people. Each of them can propose a method of distribution of the coins amongst themselves when their chance comes and a vote will occur in favour or against his distribution method between all those members. The person proposing that method of distribution wins the vote if he gets equal or more votes in favour&nbsp;than in against his proposal else he loses. Loosing he would be eliminated and then the next member will now propose his method of distribution amongst the remaining members.</span></p>

<p><span style="font-size:18px">Each person while proposing his method of distribution wants to get the maximum number of coins as well as win the vote.</span></p>

<p><span style="font-size:18px">Each person is smart and knows all the possibilities that may occur from their vote and will cast their vote&nbsp;accordingly.</span></p>

<p><span style="font-size:18px">The first proposal will always be given by 1 if he loses will be followed by 2 and so on (till the Kth person).</span></p>

<p><span style="font-size:18px">In the distribution of the 1<sup>st</sup> person print the amount of coins each of K people is proposed to get so that he wins the vote.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>:
N = 100 and K = 2
<strong>Output:</strong>&nbsp;100 0
<strong>Explanation</strong>:
To get the maximum coins the 1<sup>st</sup> person will propose the 
distribution 100,0 when the vote occurs he will obviously
vote for himself and the second person against him. 
The result of the vote will be 1-1 which means he will 
survive (tie here means victory) the vote.
</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N = 100 and K = 1
<strong>Output: </strong>100
</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>coinsGame()</strong>&nbsp;which takes the integer N and an integer K&nbsp;as input parameters and returns the&nbsp;K space-separated Integers denoting the distribution proposed by the 1<sup>st</sup> person.<br>
<br>
<strong>Expected Time Complexity:</strong> O(K)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong></span></p>

<p><span style="font-size:18px">1&lt;=N&lt;=10<sup>9</sup></span></p>

<p><span style="font-size:18px">1&lt;=K&lt;=10<sup>4</sup></span></p>

<p><span style="font-size:18px">N&gt;=K</span></p>

<p>&nbsp;</p>
</div>