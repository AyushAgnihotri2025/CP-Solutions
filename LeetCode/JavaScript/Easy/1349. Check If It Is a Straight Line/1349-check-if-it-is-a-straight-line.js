/**
 * @param {number[][]} coordinates
 * @return {boolean}
 */
 const isStraight = (x, y, z) => (y[1] - x[1]) * (z[0] - y[0]) === (y[0] - x[0]) * (z[1] - y[1]);
var checkStraightLine = function(coordinates) {
    for (let i = 1; i < coordinates.length - 1; i++) {
    if (!isStraight(coordinates[i - 1], coordinates[i], coordinates[i + 1]))
      return false;
  }
  return true;
};