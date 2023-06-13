# Top k numbers in a stream
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given <strong>N</strong> numbers in an array. Your task is to keep at-most <strong>K</strong> numbers at the top (According to their frequency).&nbsp; We basically need to print top k numbers when input stream has included k distinct elements, else need to print all distinct elements sorted by frequency.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N=5, K=4
arr[] = {5, 2, 1, 3, 2} 
<strong>Output:</strong> 5 2 5 1 2 5 1 2 3 5 2 1 3 5&nbsp;
<strong>Explanation</strong>:
Firstly their was 5 whose frequency
is max till now. so print 5.
Then 2 , which is smaller than 5 but
their frequency is same so print 2 5.
Then 1, which is smallet among all the
number arrived, so print 1 2 5.
Then 3 , so print 1 2 3 5
Then again 2, which has the highest
frequency among all number so 2 1 3 5.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N=5, K=4
arr[] = {5, 2, 1, 3, 4} 
<strong>Output:</strong> 5 2 5 1 2 5 1 2 3 5 1 2 3 4&nbsp;
<strong>Explanation</strong>:
Firstly their was 5 whose frequency is
max till now. so print 5.
Then 2 , which is smaller than 5 but
their frequency is same so print 2 5.
Then 1, Which is smallest among all the
number arrived, so print 1 2 5.
Then 3 , so print 1 2 3 5.
Then 4, so 1 2 3 4 as K is 4 so print
at-most k elements.
</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function <strong>kTop()</strong> that takes <strong>array a</strong>,&nbsp;<strong>integer n</strong> <strong>and integer&nbsp;k</strong>&nbsp;as parameters and returns the array that contains our desired&nbsp;output.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N*K).<br>
<strong>Expected Auxiliary Space:</strong> O(N).</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N,K ≤ 10<sup>3</sup></span></p>

<p>&nbsp;</p>
</div>