# String Conversion
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given two strings X and Y, the task is to check if it is possible to convert X to Y by performing the following operations.</span></p>

<ul>
	<li><span style="font-size:18px">&nbsp;Make some lowercase letters uppercase.</span></li>
	<li><span style="font-size:18px">&nbsp;Delete all the lowercase letters.</span></li>
</ul>

<p><span style="font-size:18px"><strong>NOTE:</strong> You can perform one,two or none operations to convert the string X to Y as needed.<br>
<strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong> X = "daBcd", Y = "ABC"
<strong>Output:</strong> 1
<strong>Explanation:</strong> Convert 'a' and 'c', delete
both the d's</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong> X = "ABcd", Y = "BCD"
<strong>Output:</strong> 0
<strong>Explanation:</strong> Can not delete A</span></pre>

<p><span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>stringConversion()</strong>&nbsp;which takes the strings<strong> </strong>as input and returns 1 if it is possible to convert, otherwise 0.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(|X|*|Y|)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(|X|*|Y|)<br>
<br>
<strong>Constraints:</strong><br>
1 ≤ |X|, |Y| ≤ 10<sup>3</sup></span></p>
</div>