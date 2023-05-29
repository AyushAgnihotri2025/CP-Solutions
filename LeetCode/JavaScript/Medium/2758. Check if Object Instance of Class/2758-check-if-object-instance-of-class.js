/**
 * @param {any} obj
 * @param {any} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if (obj === null || obj === undefined || !classFunction) {
        return false;
    }
    let ctor = obj.constructor;
    while (ctor) {
        if (ctor === classFunction) {
            return true;
        }
        ctor = Object.getPrototypeOf(ctor.prototype)?.constructor;
    }
    return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */