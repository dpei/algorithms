# Introduction of bioinforamtics algorithms
# Dong

# a is the original value, each digit is in scala of an array
a <- c(1,1,2,1)
# k represent total how many possible values in one digit 
k <- 4
#
L <- length(a)
# call this function to add one to the number a time until it exhausted 
# all possible numbers in the array
next.leaf(a,L,k)

next.leaf <- function(a,L,k) {
  for (i in L:1){
    if (a[i] < k) {
      a[i] <- a[i] + 1 
      return(a)
    } else {
      a[i] <- 1
    }
  }
  return(a)
}

all.leaves <- function(L,k) {
  a <- c(1,1,1,1)
  while (1==1) {
    print(a)
    a <- next.leaf(a,L,k)
    if (all(a == c(1,1,1,1)))
      break
  }
}
all.leaves(L,k)
