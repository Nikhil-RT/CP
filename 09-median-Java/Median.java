// median(a) (10 pts)
// Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
// which is the value of the middle element, or the average of the two middle elements if there is no single middle 
// element. If the list is empty, return None.

public class Median {
	public int median(double[] list) {
		// Your code goes here
		int n = list.length;
		Double med;
		if (n%2 == 0) {
			double elements = list[n/2]+list[(n/2) - 1];
			med = ((double) elements)/2;
		}
		else {
			med = ((double) list[n/2]);
		}
		return med.intValue();
	}
}