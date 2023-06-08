# Geek fight
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px"><strong>Geek</strong>&nbsp;is playing a video game that contains&nbsp;<strong>N</strong>&nbsp;monsters having varying power denoted by&nbsp;<strong>power[i]</strong>.&nbsp;<strong>Geek</strong>&nbsp;will play total&nbsp;<strong>Q</strong>&nbsp;rounds and for each round, the power of&nbsp;<strong>Geek</strong>&nbsp;is <strong>Q[i]</strong>. He can kill all monsters having power <strong>&lt;=</strong>&nbsp;<strong>Q[i]</strong>.<br>
All the monsters which were dead in the previous round will be reborn, such that for each round there will be <strong>N</strong>&nbsp;monsters.<br>
Since&nbsp;<strong>Geek&nbsp;</strong>wants to win each round, he wants to count the number of monsters he can kill in each round and total sum of their powers. Can you help him?</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 7
powers[] = {1, 2, 3, 4, 5, 6, 7}
Q[] = {3, 10, 2}
<strong>Output: 
</strong>{{3, 6}, {7, 28}, {2, 3}}
<strong>Explanation:</strong>
1. For round 1, Geek has power 3, hence, it can kill
the monsters with power 1, 2 and 3. Hence, count is 3 and
total sum = 1 + 2 + 3 = 6.
2. For round 2, Geek has power 10, hence, it can kill
all the monsters. Hence, count is 7 and
total sum = 1 + 2 + ...+ 7 = 28.
3. For round 3, Geek has power 2, hence, it can kill
the first two monsters. Hence, count is 2 and
total sum = 1 + 2 = 3.

</span></pre>

<p><span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>win()</strong>&nbsp;which takes an array of size N and another array of size Q and return list of pairs as output.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N*logN)<br>
<strong>Expected Auxiliary Space:</strong> O(N)</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= N&nbsp;&lt;= 10<sup>4</sup><br>
1 &lt;= power[i]&nbsp;&lt;= 10<sup>2</sup><br>
1&lt;= Q &lt;=10<sup>4</sup><br>
1 &lt;= Q[i[&nbsp;&lt;= 10<sup>2</sup></span></p>
</div>