# Operators
Python language supports several types of operators. In this section, we will focus on few of them.
Operators are used to perform operations on variables and values.
### Python divides the operators in the following groups:
- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators
## Assignment Operators
Assignment operators are used to assign values to variables. Let us take = as an example. 

```Python
Operator	Example	  Same As	
=	         x = 5	  x = 5	
+=	         x += 3	  x = x + 3	
-=	         x -= 3	  x = x - 3	
*=	         x *= 3	  x = x * 3	
/=	         x /= 3	  x = x / 3	
%=	         x %= 3	  x = x % 3	
//=	         x //= 3  x = x // 3	
**=	         x **= 3  x = x ** 3	
&=	         x &= 3	  x = x & 3	
|=	         x |= 3	  x = x | 3	
^=	         x ^= 3	  x = x ^ 3	
>>=	         x >>= 3  x = x >> 3	
<<=	         x <<= 3  x = x << 
```
## Arithmetic Operators:
- Addition(+): a + b
- Subtraction(-): a - b
- Multiplication(*): a * b
- Division(/): a / b
- Modulus(%): a % b
- Floor division(//): a // b
- Exponentiation(**): a ** b

## Comparison Operators

```python
# Operator	Name	               Example	
    ==	    Equal	                x == y	
    !=	Not equal	                x != y	
    >	Greater than	            x > y	
    <	Less than	                x < y	
   >=	Greater than or equal to	x >= y	
   <=	Less than or equal to	    x <= y
```

## Logical Operators
```python
#Operator	Description	                               Example	
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
```

## Identity Operators
```python
#Operator	Description	                                        Example	
is 	Returns True if both variables are the same object	         x is y	
is not	Returns True if both variables are not the same object	x is not y
```

## Membership Operators
```python
#Operator	Description	                                                                      Example	
in 	Returns True if a sequence with the specified value is present in the object	           x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y
```

## Bitwise Operators
```python
#Operator	Name	Description	                               Example	
& 	        AND	Sets each bit to 1 if both bits are 1	        x & y	
|	        OR	Sets each bit to 1 if one of two bits is 1	    x | y	
^	       XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
~	      NOT	Inverts all the bits	                          ~x	
<<	     Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
```


```python

#Operator	Description	
()	        Parentheses	
**	        Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	    Addition and subtraction	
<<  >>	    Bitwise left and right shifts	
&	        Bitwise AND	
^	        Bitwise XOR	
|	        Bitwise OR	
==  !=  >  
>=  <  <=  
is  is not  
in  not in  Comparisons, identity, and membership operators	
not	        Logical NOT	
and	        AND	
or	        OR
```