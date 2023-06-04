var TimeLimitedCache = function() {
    this.data = {};
    this.active = 0;
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const prevActive = !!this.data[key]?.isActive;
    prevActive ? clearTimeout(this.data[key].timeoutId) : this.active++;
    const timeoutId = setTimeout(() => {
        this.active--;
        this.data[key].isActive = false;
    },duration);
    this.data[key] = {
        isActive: true,
        value,
        timeoutId
    }
    return prevActive;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    return this.data[key]?.isActive ? this.data[key].value : -1;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return this.active;
};

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */