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
		
		return (Math.floorDiv(street, 8)*8);

	}
	public static void main(String[] args) {
		System.out.println(Math.floor(2.8));
	}
}