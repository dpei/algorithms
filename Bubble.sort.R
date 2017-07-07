# bubble sort

bubble.sort <- function(vec){
  for (passnum in (length(vector)-1):1) {
    for (i in 1:passnum){
      if (vec[i] > vec[i+1]){
        temp <- vec[i+1]
        vec[i+1] <- vec[i]
        vec[i] <- temp
      }
    }
  }
  return (vec)
}

vec <- c(54,26,93,17,77,31,44,55,20)
bubble.sort(vec)