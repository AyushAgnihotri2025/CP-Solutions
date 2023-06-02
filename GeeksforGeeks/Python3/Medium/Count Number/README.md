# Count Number
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array arr consisting of integers of size n and 2 additional integers k and x, you need to find the number of subsets of this array of size k, where Absolute difference between the <strong>Maximum</strong> and <strong>Minimum</strong> number of the subset is at most x.</span></p>

<p><span style="font-size:18px"><strong>Note: </strong>As this number that you need to find can be rather large, print it <strong>Modulo</strong> 10<sup>9</sup>+7</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
n = 5, k = 3, x = 5
arr[] = {1, 2, 3, 4, 5}
<strong>Output:</strong>
10
<strong>Explanation :</strong>
Possible subsets of size 3 are :-
{1,2,3} {1,2,4} {1,2,5} {1,3,4}
{1,3,5} {1,4,5} {2,3,4} {2,3,5}
{2,4,5} {3,4,5} having difference
of maximum and minimum
element less than equal to 5.</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
n = 8, k = 4, x = 6
arr[] = {2, 4, 6, 8, 10, 12, 14, 16}
<strong>Output:</strong>
5
<strong>Explanation :</strong>
Possible subsets of size 4 are:-
{2,4,6,8} {4,6,8,10} {6,8,10,12}
{8,10,12,14} {10,12,14,16} having
difference of maximum and minimum 
element less than equal to 6.</span></pre>

<p><br>
<br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You <strong>don't</strong> have to print anything, printing is done by the driver code itself. Your task is to complete the function<strong> getAnswer() </strong>which takes the array <strong>arr[]</strong>, its size <strong>n </strong>and two integers <strong>k</strong> and <strong>x</strong> as inputs and returns<strong> </strong>the required result, <strong>Modulo</strong> 10<sup>9</sup>+7.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity: </strong>O(n. log(n))<br>
<strong>Expected Auxiliary Space: </strong>O(n)</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ n ≤ 5×10<sup>5</sup><br>
1 ≤ k ≤ n<br>
1 ≤ arr[i], x ≤ 10<sup>9</sup></span></p>
</div>