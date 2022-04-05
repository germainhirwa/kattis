var line;

while (line = readline()) {
    var nums = line.split(' ');
    var w = parseInt(nums[0]);
    var s = parseInt(nums[1]);
    var c = parseInt(nums[2]);
    var k = parseInt(nums[3]);
    if (s < k || w + c < k || (s == k && w + c <= 2*k) || (w + c == k && s <= 2*k))
        console.log("YES");
    else
        console.log("NO");
}