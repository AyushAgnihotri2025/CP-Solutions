# Non-overlapping Intervals
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an 2D array<strong>&nbsp;intervals </strong>of size <strong>N</strong> representing intervals where <strong>intervals [ i ] = [start<sub>i</sub>&nbsp;, end<sub>i&nbsp;</sub>)</strong>, return the<strong> minimum</strong> number of intervals you need to remove to make the rest of the intervals <strong>non-overlapping</strong>.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<div style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#222426; --darkreader-inline-border-top:#3e4446; --darkreader-inline-border-right:#3e4446; --darkreader-inline-border-bottom:#3e4446; --darkreader-inline-border-left:#3e4446;"><span style="font-size:18px"><strong>Input:</strong><br>
N = 4<br>
intervals [ ] = {{1, 2}, {2, 3}, {3, 4}, {1, 3}}<br>
<strong>Output: </strong>1<br>
<strong>Explanation:</strong>&nbsp;<br>
{1, 3} can be removed and the rest of the intervals are non-overlapping.</span></div>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<div style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#222426; --darkreader-inline-border-top:#3e4446; --darkreader-inline-border-right:#3e4446; --darkreader-inline-border-bottom:#3e4446; --darkreader-inline-border-left:#3e4446;"><span style="font-size:18px"><strong>Input:</strong><br>
N = 3<br>
intervals [ ] = {{1, 3}, {1, 3}, {1, 3}}<br>
<strong>Output:</strong> 2<br>
<strong>Explanation:</strong>&nbsp;<br>
You need to remove two {1, 3} to make the rest of the intervals non-overlapping.</span></div>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>minRemoval()</strong>&nbsp;which takes the interger <strong>N&nbsp;</strong>and 2D integer array <strong>intervals [ ] </strong>as parameters and returns the <strong>minimum</strong> number of intervals needs to remove in order to make the remaining intervals non-overlapping.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(NlogN)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤&nbsp; 10<sup>5</sup><br>
|intervals<sub>i</sub>|&nbsp;== 2<br>
-5*10<sup>4&nbsp;</sup>≤ start<sub>i&nbsp;</sub>&lt; end<sub>i</sub>&nbsp;&lt;=5*10<sup>4</sup></span></p>

<p>&nbsp;</p>
</div>