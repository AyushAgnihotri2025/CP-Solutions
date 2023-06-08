# Minimum Platforms 2
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">You are in geekworld railway station. You are given train schedule as follows</span></p>

<ul>
	<li><span style="font-size:18px">arrival_time array contains arrival time of each train</span></li>
	<li><span style="font-size:18px">departure_time array contains departure time of each train</span></li>
	<li><span style="font-size:18px">days array contains the particular day when the trains runs. Also each train arrive and departs on the same day</span></li>
	<li><span style="font-size:18px">You are also given number_of_platforms you&nbsp;have.</span></li>
</ul>

<p><span style="font-size:18px">You have to tell&nbsp; if it is possible to run all the trains with the given number of platforms such that no train has&nbsp;to wait.<br>
<strong>Note:</strong> If 2 trains arrive and depart on the same time on the same day on the same platform&nbsp;then depart the train first then second train arrives. Also time in geekland <strong>does not</strong>&nbsp;follow <strong>24 hr(HHMM)</strong>&nbsp;format. So time can be 2368 or 2398, here 2398 &gt; 2368.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input</strong>: n = 6&nbsp;
arr[] = {900, 940, 950, 1100, 1500, 1800}
dep[] = {910, 1200, 1120, 1130, 1900, 2000}
days[] = {1, 2, 2, 1, 3, 4}
platforms = 2
<strong>Output</strong>: True
<strong>Explanation</strong>:
Minimum 2 platforms are required to 
safely arrive and depart all trains.</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>minimumPlatform2()</strong>&nbsp;which takes the arr, dep, days, platforms as inputs and returns a boolean value wheather it is possible to run all trains&nbsp;such that no train waits.</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ n ≤ 10^5<br>
0&nbsp;≤ arr[i] ≤ dep[i] ≤ 2399<br>
1&nbsp;≤ number_of_platforms &lt; 100<br>
1&nbsp;≤ days[i] &lt; 100</span></p>
</div>