# Neeman's Shoes
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Due to the second wave of&nbsp;Gorona virus,&nbsp;Geekland imposed another&nbsp;lockdown and&nbsp;Geek has gained some wieght. Now Geek has decided to exercise.<br>
There are <strong>N</strong> intersections in the city numbered from <strong>0</strong> to <strong>N-1</strong> and <strong>M</strong> bidirectional roads each road connecting two intersections. All the intersections are connected to each-other through some set of roads,<strong> i<sup>th</sup></strong> road connect intersections&nbsp;<strong>A[i][0] </strong>and<strong> A[i][1]</strong> and is of length<strong> A[i][2]</strong>.<br>
Every morning Geek will start at intersection <strong>src</strong> and will run/walk upto intersection <strong>dest</strong>. Geek only has one hour in the morning so he will choose to cover the shortest path from <strong>src</strong> to <strong>dest</strong>.<br>
After planning his exercising schedule, Geek wants to buy the perfect shoes to walk/run in the morning. He goes to&nbsp;Neeman's Shoe factory which is the National Shoe factory of Geekland.&nbsp;</span></p>

<p><span style="font-size:18px">Geek sees that there are two types of shoes "Neeman's Wool Joggers" and "Neeman's Cotton Classics", "Neeman's Wool Joggers" are good for running and "Neeman's Cotton Classics" are good for walking.<br>
Geek is confused which shoes to buy, so he comes up with a strategy. If the distance he has to cover in the morning is less than or equal to X, then he will walk the distance, therefore he will buy "Neeman's Cotton Classics". If the distance is greater than X, he will buy "Neeman's Wool Joggers". Geek is too lazy to calculate the shortest distance between two intersections src and dest. Help him decide which shoes to buy.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:&nbsp;</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N = 3, M = 2, src = 0, dest = 2, X = 5
A[][] = {{0, 1, 3},
&nbsp;        {1, 2, 3}}
<strong>Output:</strong>
Neeman's Wool Joggers
<strong>Explanation</strong>: 
Shortest path from src to dest is 6 
which is greater than X, hence Geek will
buy "Neeman's Wool Joggers".
</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 2:&nbsp;</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong> 
N = 3, M = 2, src = 0, dest = 2, X = 6 
A[][] = {{0, 1, 3},
&nbsp;      &nbsp; {1, 2, 3}} 
<strong>Output:</strong> 
Neeman's Cotton Classics 
<strong>Explanation</strong>: 
Shortest path from src to dest is 6
which is not greater than X, hence Geek 
will â€‹buy "Neeman's Cotton Classics".</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>exercise( )</strong>&nbsp;which takes&nbsp;<strong>N</strong>, <strong>M</strong>, <strong>A[ ][ ]</strong>, <strong>src</strong>,<strong> dest</strong>&nbsp;and <strong>X</strong>&nbsp;as input parameters and returns string representing the shoes he selects. Either&nbsp;<strong>"Neeman's Wool Joggers"</strong>&nbsp;or <strong>"Neeman's Cotton Classics".</strong></span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O((N + M) * Log(M))<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(N + M)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
2 ≤ N&nbsp;≤ 10<sup>4</sup><br>
1 ≤ M&nbsp;≤ min((N*(N-1))/2, 2*10<sup>5</sup>)<br>
0 ≤ A[i][0], A[i][1]&nbsp;&lt; N<br>
0 ≤ src, dest &lt; N<br>
1 ≤ A[i][2], X ≤ 10<sup>9</sup></span></p>
</div>