// # Write the function vowelCount(s), that takes a string s, 
// # and returns the number of vowels in s, ignoring case, 
// # so "A" and "a" are both vowels. The vowels are "a", "e", "i", "o", and "u". 
// # So, for example, ("Abc def!!! a? yzyzyz!") returns 3 (two a's and one e).


class vowelscount {
	int count = 0;
	public int fun_vowelscount(String s){
		// your code goes here	
		for (int i = 0; i< s.length(); i++) {
			if (s.charAt(i) =='a' || s.charAt(i) == 'e' || s.charAt(i) == 'i' || s.charAt(i) == 'o' || s.charAt(i) == 'u' || s.charAt(i) =='A' || s.charAt(i) =='E' || s.charAt(i) =='I' || s.charAt(i) =='O'|| s.charAt(i) =='U') {
				count++;
			}
		}
		return count-1;
	}
	
}