# Split the string
## Easy
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a string S, you have to check if we can split it into four strings such that each string&nbsp;is non-empty and distinct from each other.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input :</strong>
S = "geeksforgeeks"
<strong>Output:
</strong>1
<strong>Explanation:</strong>
"geeks", "for", "gee", "ks" are four
distinct strings that can form from
given string.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: 
</strong>S = "aaabb" 
<strong>Output:
</strong>0
</span><strong><span style="font-size:18px">Explanation:
</span></strong><span style="font-size:18px">It's not possible to split string S in four
distinct strings</span>
</pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>isPossible()</strong>&nbsp;which takes the string&nbsp;S<strong>&nbsp;</strong>as input parameter and returns 1 if it's possible to split S into four strings such that each string is non-empty and distinct&nbsp;from each other or return 0 otherwise.&nbsp;</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(|S|<sup>3</sup>)<br>
<strong>Expected Space Complexity:</strong> O(1)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1&lt; |S| &lt;=10000</span></p>
</div>