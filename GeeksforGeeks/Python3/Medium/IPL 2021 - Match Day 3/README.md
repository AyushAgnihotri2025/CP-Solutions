# IPL 2021 - Match Day 3
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Due to the rise of covid-19 cases in India, this year BCCI decided to organize knock-out matches in IPL rather than a league. </span></p>

<p><span style="font-size:18px">Today is matchday 3 and it is between Geek's favorite team Royal Challengers Banglore and the most powerful batting team - Sunrisers Hyderabad. Virat Kholi captain of the team RCB tried everything to win the trophy but never succeeded. He went to guruji to seek the blessing, but the guruji gave him a problem and asked him to solve it. Guruji gave him a tree-like structure, asked him to stand at the<strong> target</strong> node and find the sum of all nodes within a maximum distance of<strong> k</strong> from the <strong>target</strong> node. can Kholi solve this problem to qualify for the next round?<br>
<br>
<strong>Note:</strong> The target node should be included in the sum. </span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
    &nbsp;              1
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;/&nbsp;&nbsp; &nbsp;\
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;   2&nbsp; &nbsp; &nbsp; 9
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;    /&nbsp; &nbsp; &nbsp;&nbsp;/&nbsp;&nbsp;\
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;     4&nbsp; &nbsp; &nbsp; 5&nbsp; &nbsp; &nbsp;7
&nbsp; &nbsp; &nbsp; &nbsp;     /&nbsp; &nbsp;\&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;/&nbsp; \
&nbsp; &nbsp; &nbsp;      8&nbsp; &nbsp;  19&nbsp; &nbsp; &nbsp;20&nbsp; &nbsp; 11
&nbsp; &nbsp;       /&nbsp; &nbsp; &nbsp;/&nbsp; \
 &nbsp;       30&nbsp; &nbsp;40&nbsp; &nbsp;50
target = 9, K = 1
<strong>Output:</strong>
22
<strong>Explanation:</strong>
Nodes within distance 1 from 9 are 9, 5, 7, 1  
</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
    &nbsp;              1
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;/&nbsp;&nbsp; &nbsp;\
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;   2&nbsp; &nbsp; &nbsp; 9
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;    /&nbsp; &nbsp; &nbsp;&nbsp;/&nbsp;&nbsp;\
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;     4&nbsp; &nbsp; &nbsp; 5&nbsp; &nbsp; &nbsp;7
&nbsp; &nbsp; &nbsp; &nbsp;     /&nbsp; &nbsp;\&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;/&nbsp; \
&nbsp; &nbsp; &nbsp;      8&nbsp; &nbsp;  19&nbsp; &nbsp; &nbsp;20&nbsp; &nbsp; 11
&nbsp; &nbsp;       /&nbsp; &nbsp; &nbsp;/&nbsp; \
 &nbsp;       30&nbsp; &nbsp;40&nbsp; &nbsp;50
target = 40, K = 2
<strong>Output:</strong>
113
<strong>Explanation:</strong>
Nodes within distance 2 from 40 are 40, 19, 50, 4
</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Complete the function <strong>sum_at_distK() </strong>which takes the root of the&nbsp;tree, target, and K&nbsp; as input parameter and returns the&nbsp;sum of all nodes within&nbsp;a max&nbsp;distance of<strong> k</strong> from the <strong>target</strong> </span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N, Node Value ≤ 10<sup>5</sup><br>
1 ≤ K ≤ 20</span></p>
</div>