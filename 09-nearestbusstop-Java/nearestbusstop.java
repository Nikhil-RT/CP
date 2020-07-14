// # Write the function nearestBusStop(street) that takes a 
// # non-negative int street number, and returns the nearest 
// # bus stop to the given street, where buses stop every 8th street, 
// # including street 0, and ties go to the lower street, 
// # so the nearest bus stop to 12th street is 8th street, 
// # and the nearest bus stop to 13 street is 16th street.

class nearestbusstop {
	public int fun_nearestbusstop(int street){
		// your code goes here
		if (street < 0) return -1;
		double result = street/8;
		if(result<1){
			result = 1;
		}
		return (int)Math.floor(result*8);

	}
	public static void main(String[] args) {
		nearestbusstop n = new nearestbusstop();
		System.out.println(n.fun_nearestbusstop(2));
		System.out.println(n.fun_nearestbusstop(13));
		System.out.println(n.fun_nearestbusstop(5));
	}
}