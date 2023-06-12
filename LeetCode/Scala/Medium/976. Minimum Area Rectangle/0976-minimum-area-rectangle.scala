import scala.collection.mutable

object Solution {
    def minAreaRect(points: Array[Array[Int]]): Int = {
        val set = mutable.Set[(Int, Int)]()
        for (p <- points) {
            set.add((p(0), p(1)))
        }
        var smallest_area = 1e8.toInt
        for (point <- set.clone()) {
            set.remove(point)
            for (other <- set) {
                if (set.contains((point._1, other._2)) && set.contains((other._1, point._2))) {
                    val area = math.abs(point._1 - other._1) * math.abs(point._2 - other._2)
                    smallest_area = if (0 < area && area < smallest_area) area else smallest_area
                }
            }
        }
        if (smallest_area < 1e8.toInt) smallest_area else 0
    }
}