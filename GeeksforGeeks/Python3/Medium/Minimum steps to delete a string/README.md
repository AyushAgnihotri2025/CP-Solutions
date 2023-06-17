# Minimum steps to delete a string
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given string <strong>s </strong>containing characters as integers only, the task is to delete all characters of this string in a minimum number of steps wherein one step you can delete the substring which is a palindrome. After deleting a substring remaining parts are concatenated.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: s = "2553432"
<strong>Output:</strong> 2
<strong>Explanation</strong>: In first step remove "55", 
then string becomes "23432" which is a 
palindrome<strong>.</strong></span>
</pre>

<div><span style="font-size:18px"><strong>Example 2:</strong></span></div>

<pre><span style="font-size:18px"><strong>Input: </strong>s = "1234"
<strong>Output: </strong>4
<strong>Explanation</strong>: Remove each character in 
each step</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Complete the function <strong><code>minStepToDeleteString</code>()&nbsp;</strong>which string <strong>s </strong>as input parameters and returns the integer value<br>
<br>
<strong>Expected Time Complexity:</strong> O(<strong>|s|<sup>3</sup></strong>)<br>
<strong>Expected Auxiliary Space:</strong> O(<strong>|s|<sup>2</sup></strong>)<br>
<br>
<strong>Constraints:</strong><br>
1 ≤ |s| ≤ 10<sup>3</sup></span></p>
</div>