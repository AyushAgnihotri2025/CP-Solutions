# Save Winterfell
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">As White Walkers have attacked Winterfell, Cersei has to send her army to Winterfell but through tunnels.<br>
Unwilling to do so, she wants to delay as much as she can so she take the longest route to Winterfell.<br>
You are given no of tunnels(n) followed by tunnel 'u' connecting tunnel 'v' having distance 'w'.&nbsp;<br>
Now, you being a fan of Cersei, is keen to find the longest route.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>â€‹Input :</strong> 
arr[ ] = {{1, 5, 3}, {3, 5, 5}, {5, 4, 2}, 
{2, 4, 5}, {4, 7, 6}, {7, 8, 2}, {7, 6, 1}} 
and N = 8
<strong>Output :</strong> 14
<strong>Explanation:</strong>
If we consider the path between 8 and 3 then 
it add up to the sum equal to 14.

</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input :</strong> arr[ ] = {{1, 2, 3},{2, 3, 1}} and 
N = 3 <strong>
Output :</strong>  4</span></pre>

<p><br>
<br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function <strong>longest_route()</strong> that takes a 2-d array <strong>(arr)</strong>, number of tunnels&nbsp;<strong>(N),</strong>&nbsp;and return the length of the longest route.&nbsp;The driver code takes care of the printing.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(N).<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1).</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤ 7000<br>
1 ≤ u,v ≤ N<br>
1 ≤ w ≤ 500</span></p>
</div>