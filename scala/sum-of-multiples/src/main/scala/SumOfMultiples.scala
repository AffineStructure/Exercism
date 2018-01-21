object SumOfMultiples {


  def sum(factors: Set[Int], limit: Int): Int = {
    if (factors.toList.lengthCompare(1) > 0) {
      var original = (1 until limit).filter(_ % factors.toList.head == 0).toSet
      for (i <- 1 until factors.toList.length) {
        var updateSet = (1 until limit).filter(_ % factors.toList(i) == 0).toSet
        original = original.union(updateSet)
      }
      original.sum
    }  else if (factors.toList.lengthCompare(1) == 0) {
      (1 until limit).filter(_ % factors.toList.head == 0).sum
    } else {
      0
    }
  }
}

