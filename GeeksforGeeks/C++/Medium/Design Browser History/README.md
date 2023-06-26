# Design Browser History
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">You have a&nbsp;<strong>browser</strong>&nbsp;of one tab where you start on the&nbsp;<code>homepage</code>&nbsp;and you can visit another&nbsp;<code>url</code>, get back in the history number of&nbsp;<code>steps</code>&nbsp;or move forward in the history number of&nbsp;<code>steps</code>.</span></p>

<p><span style="font-size:18px">Implement the&nbsp;<code>BrowserHistory</code>&nbsp;class:</span></p>

<ul>
	<li><span style="font-size:18px"><code>BrowserHistory (string homepage)</code>&nbsp;Initializes the object with the&nbsp;<code>homepage</code>&nbsp;of the browser.</span></li>
	<li><span style="font-size:18px"><code>void visit (string url)</code>&nbsp;Visits&nbsp;<code>url</code>&nbsp;from the current page. It clears up all the forward history.</span></li>
	<li><span style="font-size:18px"><code>string back (int steps)</code>&nbsp;Move&nbsp;<code>steps</code>&nbsp;back in history. If you can only return&nbsp;<code>x</code>&nbsp;steps in the history and&nbsp;<code>steps &gt; x</code>, you will&nbsp;return only&nbsp;<code>x</code>&nbsp;steps. Return the current&nbsp;<code>url</code>&nbsp;after moving back in history&nbsp;<strong>at most</strong>&nbsp;<code>steps</code>.</span></li>
	<li><span style="font-size:18px"><code>string forward (int steps)</code>&nbsp;Move&nbsp;<code>steps</code>&nbsp;forward in history. If you can only forward&nbsp;<code>x</code>&nbsp;steps in the history and&nbsp;<code>steps &gt; x</code>, you will&nbsp;forward only&nbsp;<code>x</code>&nbsp;steps. Return the current&nbsp;<code>url</code>&nbsp;after forwarding in history&nbsp;<strong>at most</strong>&nbsp;<code>steps</code>.</span></li>
</ul>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
homepage = "gfg.org"
visit("google.com");
visit("facebook.com");
visit("youtube.com");
back(1);
back(1);
forward(1);
visit("linkedin.com");
forward(2);
back(2);
back(7);

<strong>Output:</strong></span>
<span style="font-size:18px">facebook.com</span>
<span style="font-size:18px">google.com</span>
<span style="font-size:18px">facebook.com</span>
<span style="font-size:18px">linkedin.com</span>
<span style="font-size:18px">google.com</span>
<span style="font-size:18px">gfg.org

<strong>Explanation: </strong>
query1: you are now at "google.com"
query2: you are now at "facebook.com"
query3: you are now at "youtube.com"
query4: move one step back, you will be at
&nbsp;       "facebook.com" again.
query5: move one more step back, you will be
&nbsp;       at "google.com"
query6: move one step forward, you will be 
&nbsp;       at "facebook.com"
query7: jump to "linkedin.com"
query8: No forward steps available, be at 
&nbsp;       "linkedin.com"
query9: move two steps back, you will go to 
&nbsp;       "facebook.com" and then "google.com"
query10: required 7 steps backward but only 
&nbsp;        1 step available, so move 1 step  
&nbsp;        back, you will be at "gfg.org"</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
homepage = "google.com"
visit("youtube.com");
back(2);

<strong>Output:
</strong>google.com

<strong>Explanation:</strong>
Required 2 steps backward, but only 1 step
available. So move 1 step back and you will
be at "google.com"</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to design your data structure inside&nbsp;<strong>class&nbsp;BrowserHistory</strong>&nbsp;and&nbsp;complete&nbsp;the functions <strong>visit()</strong>, <strong>back(),&nbsp;forward()&nbsp;</strong>and the <strong>constructor</strong>.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(1) for back(), forward() and O(n) for visit()</span></p>

<p><span style="font-size:18px"><strong>Expected Space Complexity:</strong> O(n)</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong></span></p>

<ul>
	<li><span style="font-size:18px"><code>1 &lt;= no. of queries &lt;= 5000</code></span></li>
	<li><span style="font-size:18px"><code>1 &lt;= homepage.length &lt;= 20</code></span></li>
	<li><span style="font-size:18px"><code>1 &lt;= url.length &lt;= 20</code></span></li>
	<li><span style="font-size:18px"><code>1 &lt;= steps &lt;= 100</code></span></li>
	<li><span style="font-size:18px"><code>homepage</code>&nbsp;and&nbsp;<code>url</code>&nbsp;consist of&nbsp; '.' or lower case English letters.</span></li>
</ul>
</div>