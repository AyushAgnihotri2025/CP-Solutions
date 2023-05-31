# Archana and her tricky string
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:20px">Archana is very fond of strings.&nbsp; Help her&nbsp;to solve a problem. The problem is as follows:-<br>
Given is a string of length L. Her&nbsp;task is to find the longest string from the given string with characters arranged in descending order of their ASCII code and in arithmetic progression. She&nbsp;wants the common difference should be as low as possible(at least 1) and the characters of the string to be of higher ASCII value.&nbsp;</span></p>

<p><span style="font-size:20px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:20px"><strong>Input:</strong>
s = "ABCPQR"<strong>
Output: </strong>"RQP"
<strong>Explanation: </strong>Two strings of maximum length
&nbsp;            are possible- “CBA” and “RPQ”.
&nbsp;            But he wants the string to be 
&nbsp;            of higher ASCII value 
&nbsp;            therefore, the output is “RPQ”.</span></pre>

<p><span style="font-size:20px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:20px"><strong>Input:
</strong>s = "ADGJPRT"
<strong>Output: </strong>"JGDA"
<strong>Explanation: </strong>The String of maximum length
&nbsp;            is “JGDA”.</span></pre>

<p><span style="font-size:20px"><strong>User Task:</strong><br>
Your task is to complete the function&nbsp;<strong>findString()&nbsp;</strong>which takes a single argument(string s) and returns the answer. You need not take any input or print anything.</span></p>

<p><span style="font-size:20px"><strong>Expected Time Complexity:&nbsp;</strong>O(|s|)<br>
<strong>Expected Auxiliary Space:&nbsp;</strong>O(number of distinct alphabets)</span></p>

<p><span style="font-size:20px"><strong>Constraints:</strong><br>
3 &lt;= L &lt;= 1000<br>
A &lt;= s[i] &lt;= Z<br>
The string contains minimum three&nbsp;different characters.</span></p>
</div>