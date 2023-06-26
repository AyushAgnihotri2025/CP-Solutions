# Word Search
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a string <strong>s</strong> and matrix of characters <strong>mat</strong> having <strong>n</strong> number&nbsp;of rows and <strong>m</strong> number&nbsp;of columns. Find if string exist in the grid.</span></p>

<p><span style="font-size:18px">The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.</span></p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><strong><span style="font-size:18px">Input:</span>
</strong><span style="font-size:18px">n = 4 , m = 4</span>
<span style="font-size:18px">mat = [ ['a','b','c','d'],['e','f','g','h'],['i','j','k','l'],['m','n','o','p'] ]</span>
<span style="font-size:18px">str = "bcgkjn"</span>
<span style="font-size:18px"><strong>Output:</strong> </span><span style="font-size:18px">1</span>
<strong><span style="font-size:18px">Explanation:</span></strong>&nbsp;
<span style="font-size:18px">Follow the path ( 0,1 ),&nbsp;( 0,2&nbsp;),&nbsp;( 1,2&nbsp;),&nbsp;( 2,2&nbsp;),&nbsp;( 2,1 ),&nbsp;( 3,1 ).</span>
</pre>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><strong><span style="font-size:18px">Input:</span></strong>
<span style="font-size:18px">n = 4 , m = 4</span>
<span style="font-size:18px">mat = [ ['a','b','c','d'],['e','f','g','h'],['i','j','k','l'],['m','n','o','p'] ]</span>
<span style="font-size:18px">str = "adeijp"</span>
<span style="font-size:18px"><strong>Output:</strong> </span><span style="font-size:18px">0</span>
<strong><span style="font-size:18px">Explanation:
</span></strong><span style="font-size:18px">No path is available following which we can generate required string.</span>&nbsp;
</pre>

<div><span style="font-size:18px"><strong>Constraints:</strong></span></div>

<div><span style="font-size:18px">1 &lt;= n,m &lt;= 6</span></div>

<div><span style="font-size:18px">1 &lt;= str.length&nbsp;&lt;= 15</span></div>

<div><span style="font-size:18px"><code>mat</code>&nbsp;and str&nbsp;consists of only lowercase</span><span style="font-size:18px">&nbsp;English letters.</span></div>

<div>&nbsp;</div>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>wordSearch()</strong> which takes mat[] ,and s&nbsp;as input parameters and returns 1 or 0.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(n*m)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(n*m)</span></p>
</div>