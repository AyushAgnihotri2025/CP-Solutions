# Restrictive Candy Crush
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a string <strong>s</strong>&nbsp;and an integer <strong>k</strong>, the task is to reduce the string by applying the following operation:<br>
Choose a group of <strong>k</strong>&nbsp;consecutive identical characters and remove them.</span></p>

<p><span style="font-size:18px">The operation can be performed any number of times until it is no longer possible.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>k = 2
s = "geeksforgeeks"
<strong>Output:</strong>
gksforgks
<strong>Explanation:</strong>
Modified String after each step: 
<strong>"</strong>g<strong>ee</strong>ksforg<strong>ee</strong>ks" -&gt; "gksforgks"</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>k = 2
s =<strong> "</strong>geegsforgeeeks" 
<strong>Output:</strong>
sforgeks
<strong>Explanation:</strong>
Modified String after each step:
<strong>"</strong>g<strong>ee</strong>gsforg<strong>eee</strong>ks" -&gt; "<strong>gg</strong>sforgeks" -&gt; "sforgeks"</span>
</pre>

<p><span style="font-size:18px"><strong>Your Task: </strong>&nbsp;<br>
You don't need to read input or print anything. Complete the function <strong>Reduced_String()</strong> which takes integer <strong>k</strong> and string&nbsp;<strong>s</strong>&nbsp;as input parameters and returns the reduced string.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(|s|)<br>
<strong>Expected Auxiliary Space:</strong> O(|s|)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ |s|&nbsp;≤ 10<sup>5</sup><br>
1&nbsp;≤ k&nbsp;≤ |s|</span></p>
</div>