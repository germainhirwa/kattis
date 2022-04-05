STDIN.each_line do |line|
    nums = line.scan(/\d+/).map(&:to_i)
    w = nums[0]
    s = nums[1]
    c = nums[2]
    k = nums[3]
    if (s < k || w + c < k || (s == k && w + c <= 2*k) || (w + c == k && s <= 2*k))
        print "YES"
    else
        print "NO"
    end
end