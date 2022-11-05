package timer

import kotlin.random.Random
import kotlin.math.round
import kotlin.math.abs

val PI = 3.14
val l = 1.255 // meters
val n = 12
val swings = 50
val l_err = 0.1 // meters

fun newTime(): Double = Random.nextDouble(2.014, 2.278) // seconds

fun _round(arg: Double): Double = round(arg * 100) / 100

fun newExperiment(): Double = (Array(swings) {_round(newTime())}.asList()).sum()

fun sqr(arg: Int): Int = arg * arg

fun sqr(arg: Double): Double = arg * arg

fun main() {
    var times = Array(n) {_round(newExperiment())}.asList()
    println("Mesured time -> $times")
    var time_median = _round(times.sum() / n)
    println("Time median is $time_median")
    var abs_av_t_err = 0.0
    for (time in times) {
        abs_av_t_err += abs(time - time_median)
        print("${_round(abs(time - time_median))}, ")
    }
    abs_av_t_err = _round(abs_av_t_err / n)
    println("\nAbsolute average time error is ${abs_av_t_err}")
    var gravi_accel = _round(4 * sqr(PI) * l * sqr(swings) / sqr(time_median))
    println("Gravitational acceleration $gravi_accel")
    var rel_time_err = abs_av_t_err / time_median
    println("Relative time error is $rel_time_err")
    var rel_length_err = _round(l_err / l)
    println("Relative lenth mesurement error $rel_length_err")
    var rel_gr_ac_err = _round(rel_length_err + 2 * rel_time_err)
    var delta_g = rel_gr_ac_err * gravi_accel
    println("Delta g is ${delta_g}")
    println("${_round(gravi_accel - delta_g)} <= g <= ${_round(gravi_accel + delta_g)}")
}
