# Your Social Network
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Influenced by Social Networking sites, Rahul launches his own site&nbsp;Friendsbook. Each user in Friendsbook is given a unique number, first user being numbered 1. There are N users in Friendsbook numbered from 1 to N. In Friendsbook, i th user can make j th user his friend without becoming his friend himself, i.e. in Friendsbook, there is a one-way link rather than a two-way link as in Facebook. Moreover i th user can make j th user his friend iff i&gt;j. Also one user should have no more and no less than one friend except user 1 who will have no friend. Rahul wants to modify Friendsbook and find out whether one user is somehow linked to some other user. Help Rahul do so.</span></p>

<p><span style="font-size:18px">Print all possible connections between the users in the following format:&nbsp;<br>
4 2 2 means 4 is linked to 2 via 2 connections.<br>
5 2 3 means 5 is linked to 2 via 3 connections, and so on.</span></p>

<p><span style="font-size:18px">The order of display should be as follows:</span><br>
<span style="font-size:18px">Print all possible connections starting from user 2 to user N with other users starting from 1 to The Current User Number - 1. In case one user is not connected at all with another user, that connection should not be printed.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong></span>
<span style="font-size:18px"><strong>N = </strong>3</span>
<span style="font-size:18px"><strong>arr[] = </strong>{1, 2}</span>
<span style="font-size:18px"><strong>Output:</strong></span>
<span style="font-size:18px">2 1 1 3 1 2 3 2 1
<strong>Explanation:</strong></span>
<span style="font-size:18px">2 is directly linked to 1 and hence 2 is
linked to 1 via 1 connection. 3 is directly
linked to 2 which in turn is directly
linked to 1. Hence 3 is linked to 1 via 
2 connections and to 2 via 1 connection.</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong></span>
<span style="font-size:18px"><strong>N = </strong>3</span>
<span style="font-size:18px"><strong>arr[] = </strong>{1, 1}</span>
<span style="font-size:18px"><strong>Output:</strong></span>
<span style="font-size:18px">2 1 1 3 1 1
<strong>Explanation:</strong></span>
<span style="font-size:18px">Both 2 and 3 are directly linked to 1.
Hence both 2 and 3 are linked to 1 via
1 connection.</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>socialNetwork()</strong> which takes an Integer N and an array arr[] of N-1 integers as input and returns s string representing the answer.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N<sup>2</sup>)<br>
<strong>Expected Auxiliary Space:</strong> O(N<sup>2</sup>)</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong></span><br>
<span style="font-size:18px">2 &lt;= N &lt;= 500</span><br>
<span style="font-size:18px">1 &lt;= arr[i] &lt;= i</span></p>
</div>