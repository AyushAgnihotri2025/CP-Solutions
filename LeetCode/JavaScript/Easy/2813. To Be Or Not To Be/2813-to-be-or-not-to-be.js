/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    function throwError(message) {
        throw new Error(message);
    }

    return {
        toBe: function (otherVal) {
            return val === otherVal || throwError("Not Equal");
        },
        notToBe: function (otherVal) {
            return val !== otherVal || throwError("Equal");
        },
    };
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */