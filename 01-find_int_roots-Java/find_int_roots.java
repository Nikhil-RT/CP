import java.util.Arrays;

// # Write the function bonusFindIntRoots(a,b,c) that takes 
// # the int coefficients a, b, c of a quadratic equation of this form:
// #      y = ax2 + bx + c
// # You are guaranteed the function has 2 real roots, and in fact that 
// # the roots are all integers. Your function should return these 2 int roots as a list
// # in increasing order. How does a function return multiple values? Like so:
// # return root1, root2


class find_int_roots {
	public int[] fun_find_int_roots(int a, int b, int c){
		// your code goes here
		
		int[] arr = {a,b,c};
		double root1 = -b-((Math.sqrt(Math.pow(b, 2)-4*a*c)/2*a));
		double root2 = -b+((Math.sqrt(Math.pow(b, 2)-4*a*c)/2*a));
		
		int root[] = {(int)root1,(int)root2};
		Arrays.sort(root);
		return root;
			
	}
}