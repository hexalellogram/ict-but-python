public class CheckingAccount
{
  private double myBalance;
  private int myAccountNumber;

  public CheckingAccount()
  {
    myBalance = 0.0;
    myAccountNumber = 0;
  }

  public CheckingAccount(double initialBalance, int acctNum)
  {
    myBalance = initialBalance;
    myAccountNumber = acctNum;
   }

  public double getBalance()
  {
    return myBalance;
  }

  public void deposit(double amount)
  {    	
 	    myBalance += amount;
  }

  public void withdraw( double amount )
  {
    myBalance -= amount;
  }
}

-----------------------

// in driver

prompt for deposit amount
store that amount (call the var dep)  // dep = -500

try
{
	money.deposit(dep);
}
catch (IllegalArgumentException error)
{
	SOP( error.getMessage());
}
