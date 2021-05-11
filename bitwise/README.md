# Bitwise operations:

When we have a number we can use its bits version to improve our algorithms and have faster and shorter codes

## Erase the lowest set bit

x & (x - 1) => Allows erased the last bit inside x

```
if x = 00101100
then x - 1 = 00101011

then x & (x-1) = 00101100 & 00101011 = 00101000

Where:

=>  00101100
  & 00101011
_____________
    00101000
```

As we can see above when we apply the x & (x -1) operation we are changing the last bit with 1 to 0 value.

## Get the last significant bit

x & ~(x - 1) => Allows get the lowest bit in x

```
if x = 00101100
then x - 1 = 00101011
so ~(x - 1) = 11010100

then x & ~(x-1) = 00101100 & 11010100 = 00000100

Where:

=>  00101100
  & 11010100
_____________
    00000100
```

## Extract the k-th bit

(x >> k) & 1 => extracts the k-th bit from x

```
if x = 00101100 and k = 3
then x >> k = 00000101
so (x >> k) & 1= 00000101 & 1 = 1

Where:

=>  00000101
  & 00000001
_____________
    00000001
```

## Flip bit k-th

**x ^ ( 1 << k-1)** => flip the k-th bit

```
if x = 01001001 and k = 6
then 1 << (6 - 1) = 100000
so x ^ ( 1 << (k-1))= 01001001 ^ 100000

Where:

=>  01001001
xor 00100000
_____________
    01101001
```

**Other useful operations**:

- x | ( 1 << k-1) => Turn on the k-th bit
- x & ~( 1 << (k-1)) => Turn off the k-th bit
