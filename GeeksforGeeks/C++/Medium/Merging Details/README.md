# Merging Details
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Bob, a teacher&nbsp;of St. Joseph School given a task by his principal&nbsp;to merge the details of the students where each element<strong> details[i] </strong>is a list of strings, where the first element <strong>details[i][0]</strong> is a name of the student, and the rest of the elements are emails representing emails of the student. &nbsp; Two details definitely belong to the same student if there is some common email to both detail. &nbsp;After merging the details, return the details of the student in the following format: the first element of each detail is the name of the student, and the rest of the elements are emails in sorted order. &nbsp;<br>
<strong>Note: </strong>Two details have the same name, they may belong to different people as people could have the same name. A person can have any number of details initially, but all of their details definitely have the same name.<br>
In case 2 or more same email&nbsp;belongs to&nbsp;2 or more&nbsp;different names merge with first name only. <strong>Return the 2D list in the order in a sorted way according to the name of the details.</strong></span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong> 
n: 4
details = 
[["John","johnsmith@mail.com","john_newyork@mail.com"],
["John","johnsmith@mail.com","john00@mail.com"],
["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]]
<strong>Output:</strong> 
[["John","john00@mail.com","john_newyork@mail.com",
"johnsmith@mail.com"],["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]]
<strong>Explanation:</strong>
The first and second John's are the same person as 
they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none
of their email addresses are used by other accounts.
We could return these lists in any order, for example
the answer [['Mary', 'mary@mail.com'], 
['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 
'johnsmith@mail.com']] 
would still be accepted.</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong> 
n: 5
details = 
[["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
<strong>Output:</strong> 
[["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
<strong>Explanation:
</strong>We don't have any common emails in any of the users.
We just sorted the emails of each person and we
return a list of the emails.(The details can be
returned in any order).</span>
</pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read or print anything. Your task is to complete the function&nbsp;<strong>mergeDetails</strong><strong>()&nbsp;</strong>which takes 2D List of string details denoting the details of the students and returns the list of strings denoting the details of student after merging.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(N*M*logN) - where N is the size of details length and M is the size of number of strings for a name.<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(N*M) - where N is the size of details length and M is the size of number of strings for a name.</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong></span></p>

<ul>
	<li><span style="font-size:18px">1 &lt;= details.length &lt;= 1000</span></li>
	<li><span style="font-size:18px">2 &lt;= details[i].length &lt;= 10</span></li>
	<li><span style="font-size:18px">1 &lt;= details[i][j].length &lt;= 30</span></li>
	<li><span style="font-size:18px">details[i][0]&nbsp;consists of English letters.</span></li>
	<li><span style="font-size:18px">details[i][j] (for j &gt; 0)&nbsp;is a valid email.</span></li>
</ul>

<p>&nbsp;</p>
</div>