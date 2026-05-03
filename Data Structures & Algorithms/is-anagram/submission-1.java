class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> l1 = new HashMap<>();
        HashMap<Character, Integer> l2 = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++) {
            //new char
            if (!l1.containsKey(s.charAt(i))) {
                l1.put(s.charAt(i), 1);
            } else { //repeated char
                l1.put(s.charAt(i), l1.get(s.charAt(i)) + 1);
            }
        }

        for (int j = 0; j < t.length(); j++) {
            //new char
            if (!l2.containsKey(t.charAt(j))) {
                l2.put(t.charAt(j), 1);
            } else { //repeated char
                l2.put(t.charAt(j), l2.get(t.charAt(j)) + 1);
            }
        }

        if (l1.equals(l2)) {
            return true;
        }
        return false;
    }
}
