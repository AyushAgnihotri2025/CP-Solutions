# Rotate and delete
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array <strong>arr[]</strong> of <strong>N</strong> integers. Do the following operation <strong>n-1</strong> times. For every <strong>K<sup>th</sup></strong> operation:</span></p>

<ul>
	<li><span style="font-size:18px">Right rotate the array clockwise by 1.</span></li>
	<li><span style="font-size:18px">Delete the (<strong>n-k+1</strong>)<strong><sup>th</sup></strong> last element.</span></li>
</ul>

<p><span style="font-size:18px">Now, find the element which is left at last.</span></p>

<p><span style="font-size:18px"><strong>Example:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>2
4
1 2 3 4
6
1 2 3 4 5 6</span>

<span style="font-size:18px"><strong>Output:</strong>
2
3</span>

<span style="font-size:18px"><strong>Explanation:
</strong></span><span style="font-size:18px">A = {1, 2, 3, 4, 5, 6}. Rotate the array clockwise i.e. after rotation the array A = {6, 1, 2, 3, 4, 5} and delete the last element that is {5} that will be A = {6, 1, 2, 3, 4}.
Again rotate the array for the second time and deletes the second last element that is {2} that will be
A = {4, 6, 1, 3}, doing these steps when he reaches 4<sup>th</sup> time, 4<sup>th</sup> last element does not exist. Then he deletes 1<sup>st</sup> element ie {1} that will be A={3, 6}. So, continuing this procedure the last element in A is {3}.
So, the output will be 3.</span></pre>

<p><span style="font-size:18px"><strong>Input:</strong><br>
The first line of input contains an integer <strong>T </strong>denoting the number of test cases. Then <strong>T </strong>test cases follow. Each test case contains two lines. The first line of each test case contains an integer <strong>N</strong>. Then in the next line are <strong>N </strong>space separated values of the array <strong>arr[]</strong>.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Output:</strong><br>
For each test case in a new line print the required result.</span></p>

<p><span style="font-size:18px"><strong>Your task:</strong><br>
The task is to complete the function <strong>rotateDelete</strong>() which does operations as per the given query.</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= T &lt;= 110<br>
1 &lt;= N &lt;= 10<sup>6</sup><br>
1 &lt;= A[i] &lt;= 10<sup>7</sup></span></p>
</div>