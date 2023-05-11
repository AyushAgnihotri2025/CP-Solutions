object Solution {
    def removeDuplicates(nums: Array[Int]): Int = {
        if (nums.isEmpty) return 0 // handle empty array case
        var k = 1 // keep track of number of unique elements
        for (i <- 1 until nums.length) {
            if (nums(i) != nums(i-1)) { // current element is unique
            nums(k) = nums(i) // move it to the next available position in the array
            k += 1 // increment count of unique elements
            }
        }
        k // return the number of unique elements
    }
}