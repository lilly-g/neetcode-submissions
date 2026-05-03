class Solution {
    public int maxProfit(int[] prices) {
        //initialize 2 pointers
        int l = 0;
        int r = 1;
        int max = 0;

        while (r < prices.length) {
            //check if (l-r) is a better profit
            if (prices[l] < prices[r]) {
                max = Math.max(max, prices[r]-prices[l]);
            } else {
                //this means r is a better buying point
                //so just skip to checking from here
                l = r;
            }
            r++;
        }
        return max;
    }
}
