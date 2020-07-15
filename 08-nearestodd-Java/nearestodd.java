// # Write the function nearestOdd(n) that takes an double n, 
// # and returns as an int value the nearest odd number to n. 
// # In the case of a tie, return the smaller odd value. 
// # Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the double 13.0.

class nearestodd {
	public int fun_nearestodd(double n){
		// your code goes here
		
		if (n%2 == 0) {
			return (int)(n)-1;
		}
		else{
			return (int)(2*((int)(n/2.0))+1);
		}
		
	}
}



