class Solution {
    public int maxProfit(int[] prices) {
        int low = 0;
        int high = 0;
        int best = 0;
        for (int i = 0; i < prices.length; i++) {
            low = prices[i];
            for (int k = i+1; k < prices.length; k++) {
                high = prices[k];
                //
                if ((high-low) > best) {
                    best = high - low;
                }
            }
        }
        return best;
    }
}
