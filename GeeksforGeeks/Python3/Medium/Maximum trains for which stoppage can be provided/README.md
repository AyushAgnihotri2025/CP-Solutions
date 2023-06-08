# Maximum trains for which stoppage can be provided
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">You&nbsp;are given n-platform and two main running railway tracks for both directions. Trains that need to stop at your station must occupy one platform for their stoppage and the trains which need not stop at your station will run away through either of the main track without stopping. Now, each train has three values first arrival time, second departure time, and the third required platform number. We are given m such trains you have to tell the maximum number of trains for which you can provide stoppage at your station.</span></p>

<p><span style="font-size:18px"><strong>Note: </strong>Trains&nbsp;are&nbsp;given in the&nbsp;form of {arrival time, departure time, platform Number} and the&nbsp;arrival time and departure time are represented by a 4-digit integer as 1030 will represent 10:30 and 912 will represent 09:12 (24 hour Clock).</span></p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input</strong> : n = 3, m = 6 
Train no.|  Arrival Time |Dept. Time | Platform No.
    1    |   10:00       |  10:30    |    1
    2    |   10:10       |  10:30    |    1
    3    |   10:00       |  10:20    |    2
    4    |   10:30       |  12:30    |    2
    5    |   12:00       |  12:30    |    3
    6    |   09:00       |  10:05    |    1
<strong>Output</strong> : Maximum Stopped Trains = 5
<strong>Explanation</strong> : If train no. 1 will left 
to go without stoppage then 2 and 6 can 
easily be accommodated on platform 1. 
And 3 and 4 on platform 2 and 5 on platform 3.</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>maxStop</strong></span><span style="font-size:18px"><strong>() which takes</strong>&nbsp;two integers <strong>n</strong> no of platforms, <strong>m </strong>number of trains, and array trains[]&nbsp;as input parameter and returns an integer.&nbsp;</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(M*logM</span><span style="font-size:18px">)</span><br>
<span style="font-size:18px"><strong>Expected Auxiliary Space:</strong>&nbsp;O(M)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong></span></p>

<p><span style="font-size:18px">1 &lt;= N &lt;= 100<br>
1 &lt;= M &lt;= 10<sup>4</sup></span><br>
&nbsp;</p>
</div>