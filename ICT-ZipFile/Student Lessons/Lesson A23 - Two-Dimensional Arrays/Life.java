import java.util.*;
import java.io.*;

public class Life
{
    // specs say matrix to be 20 x 20.  If you'd like, you can make it 22 x 22 
    // and ignore row/col 0 and 21.  This will allow you to not have to test the 
    // condition of going out of bounds when you're counting neighbors.
    // You can make the matrix to store ints or Strings    
    private String[][] myMatrix;
    
    // initialize matrix (fill with " " if make String matrix)
    // call loadFile
    public Life(String fileName)
    {
        
        
    }
    
    // loads file and updates matrix so that matrix[r][c] is alive if (r,c) 
    // is present in file
    private void loadFile(String fileName)
    {
        try
        {
            Scanner file = new Scanner(new File(fileName));
            int numEntries = file.nextInt();
            for (int i = 0; i < numEntries; i++)
            {
                int row = file.nextInt();
                int col = file.nextInt();
                myMatrix[row][col] = "*"; // = 1 if int matrix
            }
        }
        catch (IOException error)
        {
            System.out.println (error.getMessage());
        }            
    }
    
    // updates the matrix based on the number of neighbors around each cell.
    // make a copy matrix
    // count nbrs around each cell in copy (separate method)
    // 0,1, or 4+ nbrs --> death to myMatrix[r][c]
    // 3 nbrs --> life to myMatrix[r][c]   
    public void nextGeneration()
    {
        
    }
    
    // counts and returns number of living organisms around max[r][c]   
    private int countNeighbors(String[][] max, int row, int col)
    {
        return 0;
    }
    
    // counts and returns total # of living organisms in myMatrix
    public int countLiving()
    {
        return 0;
    }
    
    // counts and returns # of living organisms in row
    public int countRow(int row)
    {
        return 0;
    }        
    
     // counts and returns # of living organisms in col
    public int countCol(int col)
    {
       return 0;
    }
    
    // displays contents of myMatrix ( "*" if alive, " " if dead)
    // include row # and col # (make a table)
    public void output()
    {
        
    }
}