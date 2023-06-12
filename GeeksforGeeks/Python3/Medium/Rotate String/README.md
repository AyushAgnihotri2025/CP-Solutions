# Rotate String
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a string S of size N and Q queries.Each query is either of the following types:<br>
Type 1- Rotate the string by K character from the end.<br>
Type 2- Print the character at the I'th index of the resulting string at that instant.<br>
Answer all queries.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N=7 Q=5
S=abcdefg
Query<sub>1</sub>: Type=1 K=2
Query<sub>2</sub>: Type=2 I=0
Query<sub>3</sub>: Type=2 I=6
Query<sub>4</sub>: Type=1 K=4
Query<sub>5</sub>: Type=2 I=1
<strong>Output:</strong>
f
e
c
<strong>Explanation:</strong>
After First query String becomes-"fgabcde"
Second query returns - 'f'
Third query returns -'e'
After Fourth Query String becomes-"bcdefga"
Fifth Query returns -'c'</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N=5 Q=2
S=geeks
Query<sub>1</sub>: Type=1 K=4
Query<sub>2</sub>: Type=2 I=4
<strong>Output:</strong>
g
<strong>Explanation:</strong>
After first query,string becomes "eeksg".
Second query returns 'g'.</span>
</pre>

<p><span style="font-size:18px"><strong>Your task:</strong><br>
You don't need to read input or print anything.Your task is to complete&nbsp;the function <strong>StringQuery() </strong>which takes an integer N,an integer Q, a string S and two arrays Q1 and Q2(containing Query type and K/I respectively) and returns an array containing the answers to the queries.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>O(Q)<br>
<strong>Expected Auxillary Space:</strong>O(1)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1&lt;=N&lt;=10<sup>5</sup><br>
1&lt;=Q&lt;=10<sup>4</sup><br>
1&lt;=Type&lt;=2<br>
1&lt;=K&lt;=10<sup>9</sup><br>
0&lt;=I</span></p>
</div>