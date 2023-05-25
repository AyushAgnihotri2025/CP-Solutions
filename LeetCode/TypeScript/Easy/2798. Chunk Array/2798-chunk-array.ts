function chunk(arr: any[], size: number): any[][] {
  var chunkedArray = [];
  for (var i = 0; i < arr.length; i += size) {
    var chunk = arr.slice(i, Math.min(arr.length, i + size));
    chunkedArray.push(chunk);
  }
  return chunkedArray;
};