# NextVertex() function is used to construct next leaves after a vertex 
# in the recursion tree
# Dong
# Bioinfo algorithms
a <- c(1,2,2)

k <- 4
L <- 4


a <- next.vertex(a,i,L,k)[[1]]
a
i <- length(a)


bypass(a,i,L,k)


next.vertex <- function(a,i,L,k){
  # Add one more digit if i<L
  if (i < L){
    a[i+1] <- 1
    return(list(a,i+1))
  } else {
    # This part is next.leaf() function to add one to last digit
    # However this part only add values to one digit and return which
    # digit
    for (j in L:1){
      if (a[j]<k){
        a[j] <- a[j]+1
        return(list(a,j))
      }
    }
  }
  return(list(a,0))
}


# This byppass function is used to skip the tree in the vertex ai
bypass <- function(a,i,L,k) {
  for (j in i:1) {
    if (a[j] < k) {
      a[j] <- a[j]+1
      return(list(a,j))
    }
  }
  return(list(a,0))
}