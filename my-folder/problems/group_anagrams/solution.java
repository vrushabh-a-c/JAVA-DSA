class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if(strs==null || strs.length==0)
            return new ArrayList<>();
        
        Map<String,List<String>> map = new HashMap<>();
        for(String s: strs)
        {
            char[] char_array = s.toCharArray();
            Arrays.sort(char_array);
            String str = new String(char_array);
            
            if(map.containsKey(str)){
                map.get(str).add(s);
            }
            else{
                map.put(str,new ArrayList<>());
                map.get(str).add(s);
            }
        }
        return new ArrayList<>(map.values());
    }
}