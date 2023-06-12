/**
 * @param {Generator} generator
 * @return {[Function, Promise]}
 */
var cancellable = function(generator) {
    let resolve;
    let reject;
    let isCancelled = false;

    const promise = new Promise((res, rej) => {
        resolve = res;
        reject = rej;
    });

    const cancel = () => {
        isCancelled = true;
        try {
            const obj = generator.throw("Cancelled");
            resolve(obj.value);
        } catch (e) {
            reject(e);
        }
    };

    function helper(val, err) {
        if (isCancelled) return;
        try {
            const obj = err ? generator.throw(err) : generator.next(val);
            if (obj.done) {
                resolve(obj.value);
            } else {
                Promise.resolve(obj.value)
                .then((result) => helper(result))
                .catch((e) => helper(undefined, e));
            }
        } catch (e) {
            reject(e);
        }
    }
    helper();
    return [cancel, promise]; 
};

/**
 * function* tasks() {
 *   const val = yield new Promise(resolve => resolve(2 + 2));
 *   yield new Promise(resolve => setTimeout(resolve, 100));
 *   return val + 1;
 * }
 * const [cancel, promise] = cancellable(tasks());
 * setTimeout(cancel, 50);
 * promise.catch(console.log); // logs "Cancelled" at t=50ms
 */