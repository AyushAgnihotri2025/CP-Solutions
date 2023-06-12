import scala.annotation.tailrec

object Solution {
    def totalSteps(nums: Array[Int]): Int = {
        val huge = Int.MaxValue / 2
		@tailrec
        def helper(nums: List[Int], stack: List[(Int, Int)], res: Int): Int = nums match {
            case Nil => res
            case x::xs => {
                val (left, right) = stack.span(_._1 <= x)
                val step = if (left == Nil) 1 else left.map(_._2).max + 1
                helper(xs, (x, step)::right, res max (if (step >= huge) 0 else step))
            }
        }
        helper(nums.drop(1).toList, List((nums.head, huge)), 0)
    }
}