class recursion {
	public int get_fib(int value){
		// return -1;
		if(value == 0) {
			return 0;
		}
		else if( value == 1){
			return 1;
		}
		else {
			return (get_fib(value - 2)+ get_fib(value-1));
		}
	}
	public static void main(String[] args) {
		
	}
}