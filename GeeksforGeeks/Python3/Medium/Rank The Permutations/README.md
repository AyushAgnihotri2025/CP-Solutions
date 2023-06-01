# Rank The Permutations
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a string, <strong>S</strong> find the rank of the string amongst all its permutations sorted lexicographically.The rank can be big. So print it modulo <strong>1000003</strong>.&nbsp;<br>
<strong>Note:</strong> Return 0 if the characters are repeated in the string.</span></p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong> S = "abc"
<strong>Output:</strong> 1
<strong>Explaination:</strong> It is the smallest 
lexicographically string of the permutation.</span></pre>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong> S = "acb"
<strong>Output:</strong> 2
<strong>Explaination:</strong> This is the second smallest
lexicographically string of the permutation.</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You do not need to read input or print anything. Your task is to complete the function <strong>rank()</strong> which takes string S as input parameter and returns the rank modulo 1000003 of the string.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(|S|<sup>2</sup>)<br>
<strong>Expected Auxiliary Space:</strong> O(|S|)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ |S| ≤&nbsp;15&nbsp;&nbsp;</span></p>
</div>