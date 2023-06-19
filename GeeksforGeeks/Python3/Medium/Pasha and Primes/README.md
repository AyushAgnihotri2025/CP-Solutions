# Pasha and Primes
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array of N integers and another array R containing Q queries(of l and r). Answer all Q queries asking the number of primes in the subarray ranging from l to r (both inclusive).<br>
Note: A is 0-based but the queries will be 1-based.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N=5,Q=3
A={2,5,6,7,8}
R={{1,3},{2,5},{3,3}}
<strong>Output:</strong>
2 2 0
<strong>Explanation:</strong>
There are 2 primes in the range [1,3], 
which are 2 and 5.
There are 2 primes in the range [2,5],
which are 5 and 7.
There are no primes in the range [3,3].</span></pre>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N=5,Q=3
A={1,2,3,4,5}
R={{1,4},{2,5},{2,3}}
<strong>Output:</strong>
2 3 2
<strong>Explanation:</strong>
There are 2 primes in range [1,4],
which are 2 and 3.
There are 3 primes in the range [2,5],
which are 2,3 and 5.
There are 2 primes in the range [3,3],
which are 2 and 3.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function primeRange() which takes the two numbers N and Q as well as the two arrays A and Q as input parameters and returns the answers of all Q queries.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong>O(Max(A[i])*Log(Log (Max(A[i]) )))<br>
<strong>Expected Auxillary Space:</strong>O(Max(A[i]))</span></p>

<p><span style="font-size:18px">Note:&nbsp;&nbsp;Max(A[i]) represents the maximum value in the array A</span><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1&lt;=N,Q,A[i]&lt;=10<sup>6</sup><br>
1&lt;=l&lt;=r&lt;=N</span></p>
</div>