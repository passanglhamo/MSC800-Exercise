def isfloat(n):
  """ 
  If string can be converted to floating number 
  returns that number, otherwise returns false
  """
  try:
    n=float(n)
    return n;
  except ValueError:
     return False;

def inputfloat(hint):
  """ 
  Prints hint and asks to enter number.
  Repeats until decimal number is entered.
  """
  ret = False
  while ret is False:
    ret = isfloat(input(hint))
    if ret is False:
      print("Please enter number")
  return ret 

class BMIcalculator:
  # removed the 'this' parameter
  def calculate(w,h):
    """
    Calculate and return bmi
    """
    return round(w/(h*h),2)

def main():
  print("Hello, let's calculate your BMI.");
  weight = float(input("Enter your weight in kilograms: "))
  height = float(input("Enter your height in meters: "))
  bmi=BMIcalculator.calculate(weight,height)
  print(f"Your BMI is: {bmi:.2f}")

if __name__ == "__main__":
    main()