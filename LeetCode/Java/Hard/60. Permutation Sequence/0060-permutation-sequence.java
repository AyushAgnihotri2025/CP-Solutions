class Solution {
    public String getPermutation(int n, int k) {
        List<Integer> lr = new ArrayList<>();
        int sum=1;
        for(int i=1;i<=n;i++) {lr.add(i);sum*=i;}
        StringBuilder sb = new StringBuilder();
        while(lr.size()!=0&&n>0)
        {
            sum/=n--;
            if(k%sum==0){sb.append(lr.remove(k/(sum)-1)); for(int i=lr.size()-1;i>=0;i--) sb.append(lr.get(i)); return sb.toString();}
            sb.append(lr.remove(k/(sum)));
            k=k%sum;
        }
        return sb.toString();
    }
}