# Lots of Work
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Ronit had always wished to become a writer. He became a very popular writer. However he knew that with popularity comes lots of work. Time passed and Ronit was deprived of sleep. His parents were now&nbsp;concerned. They advised him to minimize the amount of time he works each day. However Ronit has to complete <strong>n</strong>&nbsp;books in <strong>m</strong>&nbsp;days.<br>
He has to&nbsp;write the books in the given order but he can&nbsp;write any&nbsp;number of books each day.&nbsp;He can&nbsp;complete all the books before m&nbsp;days.&nbsp;He knew that he would take an amount of time<strong> Arr[i]</strong> to write his i<sup>th</sup> book. He wanted to find out the minimum amount of time T such that if he worked&nbsp;for a time less than or equal to T each day, he could complete his work on or before m&nbsp;days.&nbsp;He is a very good writer but is weak in algorithms. So he wants you to help him out.</span><br>
<span style="font-size:18px"><strong>Note</strong>: Ronit cannot start working on a book on one day and complete it on the next day.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
n = 5, m = 2
Arr = {1, 3, 2, 1, 2}
<strong>Output:</strong> 5
<strong>Explaination:</strong> Ronit has 2 days to complete 5 
books. He&nbsp;completes the first 2 books on the 
first day and takes a total time of 4 ≤ 5. He 
completes the remaining books on the second day 
and takes a total time of 5 ≤ 5. Hence T = 5.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
n = 4, m = 3
Arr = {1, 3, 4, 2}
<strong>Output:</strong> 4
<strong>Explaination:</strong> Ronit has 3 days to complete 4 
books. He&nbsp;completes the first 2 books on the 
first day and takes a total time of 4 ≤ 4. 
He completes the remaining two books on the 
second and third day. Hence T = 4.</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>minAmountOfTime()</strong>&nbsp;which takes the array <strong>Arr[]</strong> and its size <strong>n</strong>&nbsp;and <strong>m</strong>&nbsp;as input parameters&nbsp;and returns the minimum amount of time.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(n*m)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ n&nbsp;≤&nbsp;1000<br>
1 ≤ m&nbsp;≤ n<br>
1 ≤&nbsp;Arr[i] ≤&nbsp;100</span></p>
</div>