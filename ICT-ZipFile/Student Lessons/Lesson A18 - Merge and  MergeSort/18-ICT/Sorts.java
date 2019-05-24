
import java.util.*;

/**
 *  Description of the Class
 *
 * @author     Your Name Here
 * @created    Month Day, Year
 */
public class Sorts
{
  private long steps;

  /**
   *  Description of Constructor
   *
   * @param  list  Description of Parameter
   */
  public Sorts()
  {
    steps = 0;
  }

  /**
   *  Description of the Method
   *
   * @param  list  reference to an array of integers to be sorted
   */
  public void bubbleSort(ArrayList <Comparable> list)
  { 
      for (int outer = 0; outer < list.size() - 1; outer++)
      {
        for (int inner = 0; inner < list.size()-outer-1; inner++)
        {
          if (list.get(inner).compareTo(list.get(inner + 1)) > 0)
          {
            //swap list[inner] & list[inner+1]
            Comparable temp = list.get(inner);
            list.set(inner, list.get(inner + 1));
            list.set(inner + 1, temp);
          }
        }
      }
  }

      
  /**
   *  Description of the Method
   *
   * @param  list  reference to an array of integers to be sorted
   */
  public void selectionSort(ArrayList <Comparable> list)
  {
      int min;
      Comparable temp;
        
      for (int outer = 0; outer < list.size() - 1; outer++)
      {
        min = outer;
        for (int inner = outer + 1; inner < list.size(); inner++)
        {
          if (list.get(inner).compareTo(list.get(min)) < 0)
          {
            min = inner;  // a new smallest item is found
          }
        }
        //swap list[outer] & list[min]
        temp = list.get(outer);
        list.set(outer, list.get(min));
        list.set(min, temp);
      }
    }

      

  /**
   *  Description of the Method
   *
   * @param  list  reference to an array of integers to be sorted
   */
  public void insertionSort(ArrayList <Comparable> list)
  {
        for (int outer = 1; outer < list.size(); outer++)
        {
            int position = outer;
            Comparable key = list.get(position);
            
            // Shift larger values to the right
            while (position > 0 && list.get(position - 1).compareTo(key) > 0)
            {
              list.set(position, list.get(position- 1));
              position--;
            }
            list.set(position,  key);
          }     
  }


 /**
   *  Takes in entire vector, but will merge the following sections
   *  together:  Left sublist from a[first]..a[mid], right sublist from
   *  a[mid+1]..a[last].  Precondition:  each sublist is already in
   *  ascending order
   *
   * @param  a      reference to an array of integers to be sorted
   * @param  first  starting index of range of values to be sorted
   * @param  mid    midpoint index of range of values to be sorted
   * @param  last   last index of range of values to be sorted
   */
  private void merge(ArrayList <Comparable> list, int first, int mid, int last)
  {
      
      // for you to code, n00bs! :p
    
  }

  /**
   *  Recursive mergesort of an array of integers
   *
   * @param  a      reference to an array of integers to be sorted
   * @param  first  starting index of range of values to be sorted
   * @param  last   ending index of range of values to be sorted
   */
  public void mergeSort(ArrayList <Comparable> list, int first, int last)
  {     
      if (first == last)
        return;
      else if (last - first == 1)
      {
         if (list.get(last).compareTo(list.get(first)) < 0)
         {
            Comparable temp = list.get(first);
            list.set(first, list.get(last));
            list.set(last, temp);
         }
      }
      else
      {
          int mid = (first + last)/2;
          mergeSort(list, first, mid);
          mergeSort(list, mid+1, last);
          merge(list, first, mid, last);
      }
   }

 
  /**
   *  Accessor method to return the current value of steps
   *
   */
  public long getStepCount()
  {
    return steps;
  }

  /**
   *  Modifier method to set or reset the step count. Usually called
   *  prior to invocation of a sort method.
   *
   * @param  stepCount   value assigned to steps
   */
  public void setStepCount(long stepCount)
  {
    steps = stepCount;
  }  
}
