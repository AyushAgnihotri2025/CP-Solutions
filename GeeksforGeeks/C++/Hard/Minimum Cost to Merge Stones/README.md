# Minimum Cost to Merge Stones
## Hard
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">There are <strong>N</strong>&nbsp;piles of <strong>stones </strong>arranged in a row. The <strong>i<sup>th</sup></strong>&nbsp;pile has <strong>stones [ i ]</strong> stones.<br>
A move consists of merging exactly <strong>K</strong> <strong>consecutive</strong> piles into one piles, and the cost of this move is equal to the total number of stones in these K piles.<br>
Return the <strong>minimum</strong> cost to merge all piles of stones into one&nbsp;pile. If it is impossible, return<strong> -1</strong>&nbsp;.</span></p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<div style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#222426; --darkreader-inline-border-top:#3e4446; --darkreader-inline-border-right:#3e4446; --darkreader-inline-border-bottom:#3e4446; --darkreader-inline-border-left:#3e4446;"><span style="font-size:18px"><strong>Input:</strong><br>
N = 4<br>
K = 2<br>
stones [ ] = {3, 2, 4, 1}<br>
<strong>Output:&nbsp;</strong>20<br>
<strong>Explanation:&nbsp;</strong>We start with {3, 2, 4, 1}<br>
We merge {3, 2} for a cost of 5, and we are left with {5, 4, 1}.<br>
We merge {4, 1} for a cost of 5, and we are left with {5, 5}.<br>
We merge {5, 5} for a cost of 10, and we are left with {10}.<br>
The total cost was 20, and it is proven that this is the minimum possible cost.</span></div>

<p><br>
<span style="font-size:18px"><strong>Example 2:</strong></span></p>

<div style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor:#222426; --darkreader-inline-border-top:#3e4446; --darkreader-inline-border-right:#3e4446; --darkreader-inline-border-bottom:#3e4446; --darkreader-inline-border-left:#3e4446;"><span style="font-size:18px"><strong>Input:</strong><br>
N = 4<br>
K = 3<br>
stones [ ] = {3, 2, 4, 1}<br>
<strong>Output:</strong>&nbsp;-1<br>
<strong>Explanation:</strong>&nbsp;After any merge operation, there are 2 piles left, and we can't merge anymore. So the task is impossible.</span></div>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>mergeStones</strong>()&nbsp;which takes the&nbsp;array of&nbsp;integers <strong>stones</strong>&nbsp;,integer&nbsp;<strong>N</strong> and an integer <strong>K&nbsp;</strong>as parameters and returns the minimum cost to merge all stones.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(N<sup>3</sup>)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(N<sup>3</sup>)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤ 30<br>
2 ≤ K&nbsp;≤ 30<br>
1 ≤ stones</span>&nbsp;<span style="font-size:18px"><sub>i</sub></span><span style="font-size:18px">&nbsp; ≤ 100</span></p>
</div>