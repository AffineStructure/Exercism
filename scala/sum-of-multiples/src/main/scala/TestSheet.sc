

val numbers = List(7,2)
val numbers2 = List(2,2,7,1)


val x = numbers.grouped(2).map(e => (e.head.toInt,e.reverse.head.toInt)).toMap
val y = numbers2.grouped(2).map(e => (e.head,e.reverse.head)).toMap
val keys = x.keySet & y.keySet


val mp = keys.map(k => k -> math.min(x(k), y(k))).toMap

mp.flatten {case (a,b) => List(a,b)}.toList

val p = List((5,4), (2,3), (7,2), (3,1))

p.sortBy(_._1)
