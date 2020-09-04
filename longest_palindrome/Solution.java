class Solution {
    String reversed = "";
    String original = "";
    int l = 0;
    
    public String longestPalindrome(String s) {
        this.reversed = reverseString(s);
        this.l = this.reversed.length();
        
        for(int windowSize=s.length(); windowSize > 0; windowSize--){
            int from = 0;
            while(from + windowSize <= this.l){
                int to = from + windowSize;
                String subs = s.substring(from, to);
                if(isPalindrome(subs, from, to)){
                    return subs;
                }
                from++;
            }
            
        }
        
        return s;
    }
    
    public boolean isPalindrome(String s, int from, int to){
        String r = this.reversed.substring(this.l-to, this.l-from);
        return s.equals(r);
    }
    
    public String reverseString(String s){
        String reversed="";
        for(char c: s.toCharArray()){
            reversed = c+reversed;
        }
        return reversed;
    }
}