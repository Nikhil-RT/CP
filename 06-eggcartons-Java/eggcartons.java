// # Write the function eggCartons(eggs) that takes 
// # a non-negative integer number of eggs, and returns 
// # the smallest integer number of cartons required to hold 
// # that many eggs, where a carton may hold up to 12 eggs

class eggcartons {
	public int fun_eggcartons(int eggs){
		int carton = 12;
		if (eggs%carton == 0) {
			return eggs/carton;
		}
		else if(eggs%carton == 1){
			return (eggs/carton )+1;
		}
		else{
			return 1;
		}
	}
	public static void main(String[] args) {
		
	}
}