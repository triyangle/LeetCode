public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] nums2=nums.clone();
    	Arrays.sort(nums);
    	int le=0;
    	int ri=nums.length-1;
    	int n1=0,n2=0;
    	while(le<ri){
    		if(nums[le]+nums[ri]==target){
    			n1=nums[le];
    			n2=nums[ri];
    			break;
    		}
    		else if(nums[le]+nums[ri]>target){
    			ri--;
    		}
    		else
    			le++;
    	}
    	int fi1=0;
    	int fi2=0;
    	for(int i=0;i<nums.length;i++){
    		if(nums2[i]==n1){
    			fi1=i;
    			break;
    		}	
    	}
    	for(int j=nums.length-1;j>=0;j--){
    		if(nums2[j]==n2){
    			fi2=j;
    			break;
    		}	
    	}
    	return new int[]{fi1,fi2};
    }
}
