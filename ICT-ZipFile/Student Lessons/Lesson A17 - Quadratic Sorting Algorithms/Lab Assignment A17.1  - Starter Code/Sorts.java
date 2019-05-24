
import java.util.*;

public class Sorts
{
    private long mySteps;   // disregard this for now
    
    public Sorts()
    {
        mySteps = 0;    // disregard this for now
    }

    
    public void bubbleSort(ArrayList <Comparable> list)
    {
        
        // implement this method
    }

    /**
     *  Description of the Method
     *
     * @param  list  reference to an array of integers to be sorted
     */
    public void selectionSort(ArrayList <Comparable> list)
    {
       // implement this method
        
    }

    /**
     *  Description of the Method
     *
     * @param  list  reference to an array of integers to be sorted
     */
    public void insertionSort(ArrayList <Comparable> list)
    {
       // implement this method
    }

    //  Recursively divides a list in half, over and over. When the
    //  sublist has one or two values, stop subdividing.
    public void mergeSort(ArrayList <Comparable> a, int first, int last)
    {
        // we'll do this next week!
    }

    // creates a copy of ArrayList list called temp, and uses temp’s values to properly merge(sort) list
    // from first to last 
    public void merge(ArrayList<Comparable> list, int first, int mid, int last)
    {
        // implement this method
    }

    public void quickSort (ArrayList <Comparable> list, int first, int last)
    {
        // god method
    }

    /**
     *  Accessor method to return the current value of steps
     *
     */
    public long getStepCount()
    {
        return mySteps;
    }

    /**
     *  Modifier method to set or reset the step count. Usually called
     *  prior to invocation of a sort method.
     *
     * @param  stepCount   value assigned to steps
     */
    public void setStepCount(long stepCount)
    {
        mySteps = stepCount;
    }   
}
