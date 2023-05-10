/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    var res = init 
    for(let i of nums) res = fn(res, i);
    return res
};