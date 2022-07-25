package cn.kk.first

import cn.kk.first.utils.TimeHelper

fun main(){

    val blue = Color.BLUE

//    println(TimeHelper.getTime())


    println(getStudyMinDuration(3000))
    println(getStudyMinDuration(29000))
    println(getStudyMinDuration(31000))
    println(getStudyMinDuration(61000))
    println(getStudyMinDuration(111000))
    println(getStudyMinDuration(411000))
}

fun getStudyMinDuration(studyDuration: Long): Int{
    val minF = studyDuration / 1000 / 60f
    val minInt = minF.toInt()
    var min = minInt

    if (minF - minInt.toFloat() > 0.5) {
        min = minInt + 1
    }
    if (min == 0){
        // 不到一分钟，按照一分钟算
        min = 1
    }
    return min
}