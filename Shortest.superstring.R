# Find shortest superstring for a set of know strings.

# Function 1: find super string for two know strings. Return length 
# the biggest overlap
a <- "GGAGTTCGG"
b <- "TCGGT"

merge.two <- function(a, b) {
  max <- 0
  str <- NULL
  len1 <- nchar(a)
  len2 <- nchar(b)
  # a is in left
  for (i in 1:min(len1, len2)) {
    if (substr(a,(len1-i+1),len1) == substr(b,1,i)){
      if (max < i) {
        max <- i
        str <- paste(substr(a,1,(len1-i)),b,sep = "")
      }
    }
  }
  # a is in the right
  for (i in 1:min(len1, len2)) {
    if (substr(b,(len2-i+1),len2) == substr(a,1,i)){
      if (max < i) {
        max <- i
        str <- paste(substr(b,1,(len2-i)),a,sep = "")
      }
    }
  }
  return(c(max,str))
}

merge.two(a,b)

# Function two: Loop over all sets of strings and return result
A <- c("CATGC","CTAAGT","GCTA","TTCA","ATGCATC")
# Input is a vector, inside the vector contains all strings
shortest.superstring <- function(A) {
  lenA <- length(A)
  while(lenA > 1) {
    max <- 0
    # In each loop with i and j, Compare if there is overlap
    for (i in 1:(lenA-1)) {
      for (j in (i+1):lenA) {
        res <- as.integer(merge.two(A[i],A[j])[1])
        if(res > max) {
          max <- res
          l <- i
          r <- j
        }
      }
    }
    res.str <- merge.two(A[l],A[r])[2]
    # If we can find overlap, then left string become combined string
    # right side string become the last string 
    # then eliminate the last string and the vector is smaller.
    if (max == 0) {
      A[1] <- paste(A[1],A[lenA],sep = "")
    } else {
      A[l] <- res.str
      A[r] <- A[lenA]
    }
    lenA <- lenA - 1
  }
  return(A[1])
}

shortest.superstring(A)
B <- c("ATG","AGG", "TGC", "TCC", "GTC", "GGT", "GCA", "CAG")
shortest.superstring(B)
