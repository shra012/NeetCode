import java.util.*;
import java.util.stream.Collectors;

public class StringEncodeAndDecode {
    public static void main(String[] args) {
        List<String> original = List.of("Hello", "World!");
        String encoded = encode(original);
        List<String> decoded = decode(encoded);

        System.out.println("Original: " + original);
        System.out.println("Encoded: " + encoded);
        System.out.println("Decoded: " + decoded);
    }    
    public static String encode(List<String> str) {
        if (str == null || str.isEmpty()){
            return "";
        }
        return str.stream().map(st -> st.length() + "#" + st).collect(Collectors.joining());
    }
    public static List<String> decode(String str) {
        List<String> result = new ArrayList<>();
        if (str == null || str.isEmpty()){
            return result;
        }
        int i = 0;
        while(i < str.length()){
            int j = i;
            while(str.charAt(j) != '#'){
                j++;
            }
            int len = Integer.parseInt(str.substring(i, j));
            result.add(str.substring(j+1, j+1+len));
            i = j+1+len;
        }
        return result;
    }

}
