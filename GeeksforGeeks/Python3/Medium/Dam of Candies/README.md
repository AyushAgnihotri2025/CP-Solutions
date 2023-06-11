# Dam of Candies
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Geek wants to make a special space for candies on his bookshelf. Currently, it has <strong>N</strong> books, each of whose height is represented by the array&nbsp;<strong>height[]</strong>&nbsp;and has&nbsp;<strong>unit width</strong>.<br>
Help him select <strong>2</strong> books such that he can store maximum candies between them by removing all the other books from between the selected books. The task is to find out the area between two&nbsp;books that can hold the maximum candies without changing the original position of selected books.&nbsp;</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>N = 3, height[] = {1, 3, 4}</span>
<span style="font-size:18px"><strong>Output:</strong> 1</span>
<span style="font-size:18px"><strong>Explanation:</strong>
1. Area between book of height 1 and book of 
height 3 is 0 as there is no space between 
them.
2. Area between book of height 1 and book of 
height 4 is 1 by removing book of height 3.
3. Area between book of height 3 and book of 
height 4 is 0 as there is no space between them.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>N = 6, height[] = {2, 1, 3, 4, 6, 5}</span>
<span style="font-size:18px"><strong>Output:</strong> 8</span>
<span style="font-size:18px"><strong>Explanation:</strong> Remove the 4 books in the middle 
creating length = 4 for the candy dam. Height 
for dam will be min(2,5) = 2. 
Area between book of height 2 and book 
of height 5 is 2 x 4 = 8.
</span></pre>

<p><span style="font-size:18px"><strong>Your Task: </strong>&nbsp;<br>
You don't need to read input or print anything. Complete the function <strong>maxCandy()</strong> which takes the array height[] and size of array N as input parameters and returns the maximum candies geek can store</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</span></p>

<p><strong>Constraints:</strong><br>
<span style="font-size:18px">1 ≤ N ≤ 10</span><sup>5</sup><br>
<span style="font-size:18px">1 ≤ height[i]&nbsp;≤ 10<sup>5</sup></span></p>
</div>