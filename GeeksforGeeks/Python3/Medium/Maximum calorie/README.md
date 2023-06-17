# Maximum calorie
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array <strong>Arr</strong> of size <strong>N</strong>, each element of the array represents the amount of calories, the task is to calculate the maximum of amount of calories you can get remembering the fact&nbsp;that you cannot take three consecutive calories.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: N = 5, arr[] = {3, 2, 1, 10, 3}
<strong>Output:</strong> 18
<strong>Explanation</strong>: </span><span style="font-size:18px">You can take</span> <span style="font-size:18px">1st, 2nd, 4th 
and 5th calories (3 + 2 + 10 + 3) = 18</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>N = 2, arr[] = {8, 15}
<strong>Output: </strong>23
<strong>Explanation</strong>: You can take</span> <span style="font-size:18px">1st and 2nd
calories (8 + 15) = 23</span>
</pre>

<p><span style="font-size:18px"><strong>Your Task:&nbsp; </strong></span><br>
<span style="font-size:18px">You don't need to read input or print anything. Complete the function <strong><code>maxCalories</code>() </strong>which takes <strong>N</strong>&nbsp; and array <strong>Arr</strong> as input parameter and returns an integer value.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(<strong>N</strong>)<br>
<strong>Expected Auxiliary Space:</strong> O(<strong>N</strong>)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤ 10<sup>5</sup></span><br>
<span style="font-size:18px">1 ≤ Arr[i] ≤ 10<sup>4</sup></span></p>
</div>