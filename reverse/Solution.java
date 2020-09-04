class Solution {
    public int reverse(int x) {
        String numberInString = String.valueOf(x);
        
        String reversed = reverseString(numberInString);
        String numberWithSign = resolveSign(reversed);
            
        Long result = Long.parseLong(numberWithSign);
        if(result > Integer.MAX_VALUE || result < Integer.MIN_VALUE) return 0;
        return result.intValue();
    }
    
    
    public String resolveSign(String stringNumber){
        String numberWithSign = stringNumber;
        if(stringNumber.charAt(stringNumber.length()-1)=='-') {
            numberWithSign = "-"+stringNumber.substring(0, stringNumber.length()-1);
        }
        return numberWithSign;
    }
    
    
    public String reverseString(String stringToReverse){
        char[] charArray = stringToReverse.toCharArray();
        String reversed = "";
        for(char character : charArray){
            reversed = character+reversed;
        }
        return reversed;
    }
}