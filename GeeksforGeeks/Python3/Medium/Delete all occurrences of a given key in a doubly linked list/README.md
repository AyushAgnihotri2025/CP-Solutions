# Delete all occurrences of a given key in a doubly linked list
## Medium
<div class="problems_problem_content__Xm_eO"><p dir="ltr"><span style="font-size: 18px;">You are given the head of a doubly Linked List and a Key. Your task is to delete all occurrences of the given key and return the new DLL.</span></p>
<p dir="ltr"><strong><span style="font-size: 18px;">Example:</span></strong></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> </span>
<span style="font-size: 18px;">2&lt;-&gt;2&lt;-&gt;10&lt;-&gt;8&lt;-&gt;4&lt;-&gt;2&lt;-&gt;5&lt;-&gt;2</span>
<span style="font-size: 18px;">2</span>
<span style="font-size: 18px;"><strong>Output:</strong> </span>
<span style="font-size: 18px;">10&lt;-&gt;8&lt;-&gt;4&lt;-&gt;5</span>
<strong><span style="font-size: 18px;">Explanation: </span></strong>
<span style="font-size: 18px;">All Occurences of 2 have been deleted.
</span></pre>
<p dir="ltr"><strong><span style="font-size: 18px;">Your Task:</span></strong></p>
<p dir="ltr"><span style="font-size: 18px;">Complete the function void deleteAllOccurOfX(struct Node** head_ref, int key), which takes the reference of the head pointer and an integer value key. Delete all occurrences of the key from the given DLL.</span></p>
<p dir="ltr"><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(N).</span></p>
<p dir="ltr"><span style="font-size: 18px;"><strong>Expected Auxiliary Space:</strong> O(1).</span></p>
<p dir="ltr"><strong><span style="font-size: 18px;">Constraints:</span></strong></p>
<p dir="ltr"><span style="font-size: 18px;">0&lt;=Number of Nodes&lt;=10<sup>4</sup></span></p>
<p dir="ltr"><span style="font-size: 18px;">-10<sup>3</sup>&lt;=Node Value &lt;=10<sup>3</sup></span></p>
<p>&nbsp;</p></div>