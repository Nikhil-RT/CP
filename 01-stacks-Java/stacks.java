// import jdk.internal.org.objectweb.asm.tree.analysis.Value;

// """Add a couple methods to our LinkedList class,
// and use that to implement a Stack.
// You have 4 functions below to fill in:
// insert_first, delete_first, push, and pop.
// Think about this while you're implementing:
// why is it easier to add an "insert_first"
// function than just use "append"?"""
import org.junit.Test;
import static org.junit.Assert.assertEquals;

import java.beans.Transient;
class Element{
	int value;
	Element next;
	public Element(int value){
		this.value = value;
		this.next = null;
	}
}

class LinkedList{
	Element head;
	public LinkedList(Element head){
		this.head = head;
	}

	public void append(Element new_element){
		Element current = this.head;
        if (this.head != null) {
            while(current.next != null){
                current = current.next;
            }
            current.next = new_element;
        }
        else{
            this.head = new_element;
        }
	}

	public void insert_first(Element new_element){
		 // "Insert new element as the head of the LinkedList"
		// new_element = new Element(value);
		if (head == null){
			head = new_element;
		}
		Element current = new_element;
		head = current.next;
		current = head;

	}

	public Element delete_first(){
		// return this.head;
	   // "Delete the first (head) element in the LinkedList as return it"
	   if (head == null) {
		   return head;
	   }
	   Element current = head;
	   head = head.next;
	   current.next = null;
	   return current;
	}
}


public class stacks{
	LinkedList ll;
	public stacks(Element top){
		ll = new LinkedList(top);
	}

	public void push(Element e){
		// "Push (add) a new element onto the top of the stack"
		ll.insert_first(e);
	}

	public Element pop(){
		ll.delete_first();
		return new Element(5);
	}
	public static void main(String[] args) {
		Element e1 = new Element(1);
      	Element e2 = new Element(2);
		Element e3 = new Element(3);
		stacks stack = new stacks(e1);
		stack.push(e2);
		stack.push(e3);
		System.out.println(stack);
		assertEquals("1.", 3, stack.pop().value);
		assertEquals("2.", 2, stack.pop().value);
		assertEquals("3.", 1, stack.pop().value);
		assertEquals("4.", null, stack.pop());
	}

}
