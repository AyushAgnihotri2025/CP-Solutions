# Water the plants
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">A gallery with plants&nbsp;is divided into <strong>n</strong> parts, numbered :&nbsp;0,1,2,3...n-1. There are provisions&nbsp;for attaching water sprinklers at every partition. A sprinkler with range&nbsp;<strong>x</strong> at partition <strong>i</strong> can water all partitions from <strong>i-x</strong> to <strong>i+x</strong>.<br>
Given an array <strong>gallery[ ]</strong>&nbsp;consisting of <strong>n</strong>&nbsp;integers, where <strong>gallery[i]</strong> is the range of sprinkler at partition <strong>i</strong> (power==-1 indicates no sprinkler attached), return the minimum number of sprinklers that need to be turned on to water the complete gallery.<br>
If there is no possible way to water the full length using the given sprinklers, print -1.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
n = 6
gallery[ ] = {-1, 2, 2, -1, 0, 0}
<strong>Output:
</strong>2
<strong>Explanation: </strong>Sprinklers at index 2 and 5
can water thefull gallery, span of
sprinkler at index 2 = [0,4] and span
â€‹of sprinkler at index 5 = [5,5].</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
n = 9
gallery[ ] = {2, 3, 4, -1, 2, 0, 0, -1, 0}
<strong>Output:
</strong>-1
<strong>Explanation: </strong>No sprinkler can throw water
at index 7. Hence all plants cannot be
watered.</span></pre>

<p><span style="font-size:18px"><strong>Example 3:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
n = 9
gallery[ ] = {2, 3, 4, -1, 0, 0, 0, 0, 0}
<strong>Output:
</strong>3
<strong>Explanation: </strong>Sprinkler at indexes 2, 7 and
8 together can water all plants.</span></pre>

<p><span style="font-size:18px"><strong>Your task:</strong><br>
Your task is to complete the function&nbsp;<strong>min_sprinklers()</strong>&nbsp;which takes the array&nbsp;<strong>gallery[ ]</strong>&nbsp;and the integer&nbsp;<strong>n</strong>&nbsp;as input parameters and returns the value to be printed.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(NlogN)<br>
<strong>Expected Auxiliary Space:</strong> O(N)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ n ≤&nbsp;10<sup>5</sup><br>
gallery[i] ≤&nbsp;50</span></p>
</div>