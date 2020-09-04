class Solution {
    public int maxArea(int[] height) {
        int maxArea = 0;
        int leftPointer = 0;
        int rightPointer = height.length;
        int highestLeftLine = 0;
        int highestRightLine = 0;
        while( leftPointer > rightPointer){
            leftHeight = height[leftPointer];
            rigthHeight = height[rightPointer];
            
            if(leftHeight > highestLeftLine){
                leftPointer++;
                highestLeftLine = leftHeight
            }
            
            rightPointer--;
        }
        
        for(int i=0; i < height.length; i++){
            for(int j=i+1; j < height.length; j++){
                int max_h = Math.min(height[i],height[j]);
                int area = max_h*(j-i);
                max_area = Math.max(area, max_area);
            }
        }
        return max_area;
    }
}