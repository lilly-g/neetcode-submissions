class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> s = new HashSet<Integer>();
        for (int n : nums) {
            if (!s.contains(n)) {
                s.add(n);
            } else {
                return true;
            }
        }
        return false;
    }
}