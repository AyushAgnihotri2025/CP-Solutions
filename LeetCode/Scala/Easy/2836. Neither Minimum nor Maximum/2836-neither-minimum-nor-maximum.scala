import scala.collection.mutable.ListBuffer

object Solution {
    def findNonMinOrMax(nums: Array[Int]): Int = {
        val minVal = nums.min
        val maxVal = nums.max
        val nonMinMax = new ListBuffer[Int]()
        for (n <- nums) {
            if (n != minVal && n != maxVal) {
                nonMinMax += n
            }
        }
        if (nonMinMax.isEmpty) -1 else nonMinMax.head
    }
}