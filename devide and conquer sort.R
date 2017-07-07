# devide and conquer
# Merge sort

a <- c(1,3,4,5,6)
b <- c(2,2.4,3.2,3.3)

# combine two sorted vector into onw sorted vector
merge.two <- function(a,b){
  n1 <- length(a)
  n2 <- length(b)
  a[n1+1] <- Inf
  b[n2+1] <- Inf
  i <- 1
  j <- 1
  c <- NULL
  for (n in 1:(n1+n2)){
    if (a[i] < b[j]){
      c[n] <- a[i]
      i <- i + 1
    } else {
      c[n] <- b[j]
      j <- j + 1
    }
  }
  return(c)
}

c <- c(1, 2.4, 2, 3.2, 4, 3.3, 3, 6, 5)

merge.sort <- function(c) {
  n <- length(c)
  if (n == 1) {
    return(c)
  }
  left <- c[1: (n %/% 2)]
  right <- c[(n - n %/% 2+1):n]
  sort.left <- merge.sort(left)
  sort.right <- merge.sort(right)
  sorted <- merge(sort.left, sort.right)
  return(sorted)
}
c <- c(2,1)
merge.sort(c)
