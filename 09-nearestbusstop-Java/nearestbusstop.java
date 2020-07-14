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
		double result = (double)street/8;
		return (int)(Math.round(result) * 8);

	}
	public static void main(String[] args) {
		nearestbusstop n = new nearestbusstop();
		//8,16,8
		System.out.println(n.fun_nearestbusstop(12));
		System.out.println(n.fun_nearestbusstop(13));
		System.out.println(n.fun_nearestbusstop(5));

		//0,8,0,16
		System.out.println(n.fun_nearestbusstop(4));
		System.out.println(n.fun_nearestbusstop(8));
		System.out.println(n.fun_nearestbusstop(0));
		System.out.println(n.fun_nearestbusstop(16));
	}
}