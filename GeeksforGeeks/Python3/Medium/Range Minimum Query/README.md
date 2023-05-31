# Range Minimum Query
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array<strong> A[ ] </strong>and its size <strong>N</strong> your task is to complete two functions&nbsp; a <strong>constructST</strong>&nbsp; function which builds the segment tree&nbsp; and a function <strong>RMQ</strong> which finds range minimum query in a range [a,b] of the given array.</span></p>

<p><span style="font-size:18px"><strong>Input</strong>:<br>
The task is to complete two functions <strong>constructST</strong> and <strong>RMQ</strong>.<br>
The constructST function builds the segment tree and takes two arguments the array <strong>A[ ]</strong> and the size of the array <strong>N</strong>.<br>
It returns a pointer to the first element of the segment tree array.<br>
The <strong>RMQ </strong>function takes 4 arguments the first being the segment tree <strong>st </strong>constructed, second being the size <strong>N</strong> and then third and forth arguments are the range of query <strong>a</strong> and<strong> b</strong>. The function RMQ returns the <strong>min</strong> of the elements in the array from index range a and b. There are multiple test cases. For each test case, this method will be called individually.</span></p>

<p><span style="font-size:18px"><strong>Output:</strong><br>
The function <strong>RMQ</strong> should return the min element in the array from range <strong>a</strong> to <strong>b</strong>.</span></p>

<p><span style="font-size:18px"><strong>Example:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input (To be used only for expected output) </strong>
1
4
1 2 3 4
2
0 2 2 3
<strong>Output</strong>
1 3
<strong>Explanation
1.</strong> For query 1 ie 0 2 the element in this range are 1 2 3 
&nbsp;  and the min element is 1. 
<strong>2.</strong> For query 2 ie 2 3 the element in this range are 3 4 
&nbsp;  and the min element is 3.</span></pre>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1&lt;=T&lt;=100<br>
1&lt;=N&lt;=10^3+1</span></p>

<p><span style="font-size:18px">1&lt;=A[i]&lt;=10^9</span><br>
<span style="font-size:18px">1&lt;=Q(no of queries)&lt;=10000<br>
0&lt;=a&lt;=b</span></p>
</div>