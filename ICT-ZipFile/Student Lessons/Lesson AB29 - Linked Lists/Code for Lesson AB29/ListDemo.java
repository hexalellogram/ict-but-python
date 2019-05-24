/**
 *  Demonstrates the use of the SinglyLinkedList class.
 *
 * @author     G. Peck
 * @created    May 12, 2002
 */
public class ListDemo{
  SinglyLinkedList myList;

  public ListDemo(){
    myList = new SinglyLinkedList();
  }

  /**
   *  Creates a SinglyLinkedList of 5 Integer nodes
   */
  public void createList(){
    for (int k = 1; k < 21; k++){
      myList.addLast(new Integer(k));
    }
  }

  /**
   *  Display the first element of the list
   */
  public void displayFirst(){
    System.out.println("First Element: " + myList.getFirst());
  }
  public void displayLast(){
    System.out.println("Last Element: " + myList.getLast());
  }

  /**
   *  Print the contents of myList
   */
  public void print(){
    myList.printList();
    System.out.println();
  }
  public void getNodes()
  {
      System.out.println("Number of List Nodes: "+myList.size()); 
  }
}
