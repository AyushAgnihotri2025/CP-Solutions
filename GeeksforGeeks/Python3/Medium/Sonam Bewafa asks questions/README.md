# Sonam Bewafa asks questions
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px">They declared Sonam as bewafa. Although she is not, believe me! She asked a number of queries to people regrading their position in a test. Now its your duty to remove her bewafa&nbsp;tag by answering simple queries. All the students who give test can score from 1 to 10^18. Lower the marks, better the rank. Now instead of directly telling the marks of student they have been assigned groups where marks are distributed in continuous intervals, you have been given l(i) lowest mark of interval i and r(i) highest marks in interval i. So marks distribution in that interval is given as l(i), l(i)+1, l(i)+2 . . . r(i).</span></span></p>

<p><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px">Now Sonam ask queries in which she gives rank of the student (<em>rank<sub>i</sub></em>) and you have to tell marks obtained by that student. Simply, for each query output marks obtain by student whose rank is <em>rank<sub>i</sub></em>(1&lt;=<em>rank<sub>i</sub></em>&lt;=10<sup>18</sup>).</span></span></p>

<p><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Note: </strong>rank1 is better than rank2 and rank2 is better than rank3 and so on and the first interval starts from 1.</span></span></p>

<p><br>
<br>
<span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Example 1:</strong></span></span></p>

<pre><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Input:</strong></span><span style="font-size:20px">
n=3, q=3 </span><span style="font-size:20px">
l[] = {1, 12, 22} </span><span style="font-size:20px">
r[] = {10, 20, 30} </span><span style="font-size:20px">
rank[] = {5, 15, 25}</span>

<span style="font-size:20px"><strong>Output:</strong>
5 16 27</span>

<span style="font-size:20px"><strong>Intervals are from 1 to 10, second
interval from 12 to 20 and third 22 to 30.</strong>
In this test case, from 1 to 10 , they
are given the ranks from 1 to 10 but
in the second interval, it is starting
from 12 , so we will have to give its rank
11 and so on like this.</span>

<span style="font-size:20px"><strong>Rank:    </strong>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15......</span>
<span style="font-size:20px"><strong>Marks:</strong> 1 2 3 4 5 6 7 8 9 10 12 13 14 15 16.....</span>

<span style="font-size:20px">So 5th rank will score 5 marks,15th rank will
score 16 marks and 25th rank will score 27 marks.</span></span></pre>

<p>&nbsp;</p>

<p><span style="font-family:arial,helvetica,sans-serif"><span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>getTestMarks()</strong>&nbsp;which takes the array <strong>l[]</strong>, <strong>r[]</strong>, its size <strong>n </strong>and array <strong>rank[]</strong>,&nbsp;<strong>StoreAnswer[]</strong>, its size <strong>q</strong><strong> </strong>as inputs and fill the <strong>StoreAnswer[]</strong> array. This array stores the answer of every query.<br>
<br>
<strong>Expected Time Complexity:</strong> O(n. log(n))<br>
<strong>Expected Auxiliary Space:</strong> O(n.q)</span></span></p>

<p><br>
<span style="font-family:arial,helvetica,sans-serif"><span style="font-size:20px"><strong>Constraints:</strong></span><br>
<span style="font-size:20px">1&lt;=n&lt;=10<sup>5</sup><br>
1&lt;=q&lt;=10<sup>5</sup><br>
1&lt;= l(i) &lt; r(i) &lt;=10<sup>18</sup><br>
1&lt;=<em>rank<sub>i</sub></em>&lt;=10<sup>18</sup></span></span><br>
&nbsp;</p>
</div>