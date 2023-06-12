type Fn = (...params: any) => any

function memoize(fn: Fn): Fn {
    const trie = new Map();
    return function (...params) {
        const node = { ref: trie };
        for (const param of params) {
            if (!node.ref.has(param)) node.ref.set(param, new Map());
            node.ref = node.ref.get(param);
        }
        if (node.ref.has('result')) return node.ref.get('result');
        const result = fn(...params);
        node.ref.set('result', result);
        return result;
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */