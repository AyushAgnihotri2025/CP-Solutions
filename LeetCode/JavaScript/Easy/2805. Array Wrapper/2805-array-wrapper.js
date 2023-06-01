/**
 * @param {number[]} nums
 */
var ArrayWrapper = function(nums) {
    this.arr=nums;
};

ArrayWrapper.prototype.valueOf = function() {
     let Sum=0;  
     let arr1=this.arr;   
     for(v of arr1)
     {
         Sum+=v;
     }
     return Sum;
}

ArrayWrapper.prototype.toString = function() {
    return JSON.stringify(this.arr);
}

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */