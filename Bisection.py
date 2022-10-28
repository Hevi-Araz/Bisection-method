from calendar import c

def Bisection_method(func , a , b , error_accept):
    
# " this function solves for an unknown root of a non linear function given the function, # the initial root boundaries,and an acceptable level of error  " 
#"parameters:
# -----------------------
# :param func: the user defined function, which needs to be entered as a string
# :param a: the initial lower root boundary.
# :param b: the initial upper root boundary.
# :param error_accept: the users acceptable level of error.
# 
# returns:
# -------------------------
# :return: the root boundaries and the error at the final itaration. "

 def f(x):
  f=eval(func)
  return f

 error = abs(b-a)

 while error > error_accept:
    c=(b+a)/2

    if f(a)*f(b)>=0:
      print("No root or multiple roots present , therefore, the bisection method will not work")
      quit()

    elif f(c)*f(a)< 0:
      b=c
      error = abs(b-a)

    elif f(c)*f(b)< 0:
      a=c
      error = abs(b-a)

    else:
      print("something went wrong")
      quit()

 print(f"the error is {error}")
 print(f"the lower boundary,a,is {a} and the upper boundary,b, is {b}")

#to call our function description 
# print (bisection_method.__doc__)

Bisection_method("(4*x **3) + 3*x -3", -1,5,0.07)


