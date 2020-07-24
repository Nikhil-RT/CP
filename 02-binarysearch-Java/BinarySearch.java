class BinarySearch {
	public int binary_search(int[] arr, int value){
        // Your code goes here
        int min = 0;
        int max = arr.length-1;
        while (min <= max) {
                int mid = min + (max - min)/2;
                if (value < arr[mid]) {
                        max = mid - 1;
                }
                else if (value > arr[mid]) {
                        min = mid + 1;
                }
                else {return mid;}
        }
        return -1;
	}
}