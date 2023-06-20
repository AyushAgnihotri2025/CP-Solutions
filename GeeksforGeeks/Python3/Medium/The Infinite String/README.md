# The Infinite String
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Consider a string A = "12345".&nbsp; An infinite string&nbsp;is built by performing infinite steps on A recursively. In i<sup>th</sup> step, A is concatenated with ‘$’ i times followed by reverse of A, that is,&nbsp;<strong>A = A | $...$ | reverse(A)</strong>, where | denotes concatenation.</span></p>

<p><span style="font-size:18px">Given a position <strong>pos</strong>, find out the character at pos in the infinite string.</span><br>
<br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: pos = 3
<strong>Output: </strong>3
<strong>Explanation</strong>: A = "12345", then A[pos] is 3.
</span></pre>

<p><br>
<span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>pos = 10
<strong>Output:&nbsp;</strong>2
<strong>Explanation</strong>: A = "12345$54321", then A[pos] is 2.
</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You dont need to read input or print anything. Complete the function <strong>posInfinite()&nbsp;</strong>which takes pos&nbsp;as input parameter and returns&nbsp;the character in the infinite string at pos.</span><br>
<br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(sqrtn)<br>
<strong>Expected Auxiliary Space:</strong> O(1)<br>
<br>
<strong>Constraints:</strong><br>
1&lt;= pos&nbsp;&lt;=10<sup>12</sup></span></p>
</div>