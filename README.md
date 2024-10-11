# Simplex method for maximization

### Input:

n // number of constraints
c_1 c_2 ... c_m // coefficients of objective function
c_1_1 c_1_2 ... c_1_m // coefficients of constraint function
c_2_1 c_2_2 ... c_2_m // coefficients of constraint function
.
.
.
c_n_1 c_n_2 ... c_n_m // coefficients of constraint function
b_1 b_2 ... b_n // Right-Hand side numbers
epsilon // approximation accuracy

### Output:

[x_1, x_2, ... x_m] // A vector of decision variables
maxval // maximum value of the objective function

or

The string "The method is not applacable!"

## Examples:

### Input:

```
2
3 2
1 1
2 1
4 5
0.001
```

### Output:

```
[1.0, 3.0]
9.0
```

### Input:

```
3
1 2 3 4
1 4 7 10
3 6 8 10
4 9 14 15
30 44 53
0.001
```

### Output:

```
[3.2, 0, 0, 2.6799999999999997]
13.92
```

### Input:

```
3
1 2 3 4
1 4 7 10
3 6 8 10
4 9 14 15
30 44 53
1
```

### Output:

```
[0, 0, 0, 3.0]
12.0
```

### Input:

```
1
1 3
-1 0
9
0.001
```

### Output:

```
The method is not applacable!
```

### Input:

```
1
1 3
1 6
-9
0.001
```

### Output:

```
The method is not applacable!
```
