# Maximum Intervals Overlap
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Consider a big party where N guests came to it and a log register for guest’s entry and exit times was&nbsp;maintained. Find the minimum time at which there were maximum guests at the party. Note that entries in the register are not in any order.</span></p>

<p><span style="font-size:18px"><strong>Note:&nbsp;</strong>Guests&nbsp;are leaving&nbsp;after the exit times.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 5
Entry= {1, 2,10, 5, 5}
Exit = {4, 5, 12, 9, 12}
<strong>Output: </strong>3 5
<strong>Explanation: </strong>At time 5 there were 
&nbsp;            guest number 2, 4 and 5 present.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 7
Entry= {13, 28, 29, 14, 40, 17, 3}
Exit = {107, 95, 111, 105, 70, 127, 74}
<strong>Output: </strong>7 40
<strong>Explanation: </strong>At time 40 there were 
&nbsp;            all 7 guests present in the party.</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything.&nbsp;</span><span style="font-size:18px">Your task is to complete the function <strong>findMaxGuests() </strong>which takes 3 arguments(Entry array, Exit array, N) and returns the maximum number of guests present at a particular time and that time as a pair.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:&nbsp;</strong>O(N*Log(N) ).<br>
<strong>Expected Auxiliary Space:&nbsp;</strong>O(1).</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= N &lt;= 10<sup>5</sup><br>
1 &lt;= Entry[i],Exit[i] &lt;= 10<sup>5</sup></span></p>
</div>