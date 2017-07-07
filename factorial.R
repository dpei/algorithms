factorial <- function(n){
  if (n == 1){
    return(1)
  } else {
    atta <- n+factorial(n-1)
    return(atta)
  }
}

factorial(6)


multiply <- function(n,m){
  if (m == 0){
    return(0)
  } else if (m > 0) {
    return(n + multiply(n,m-1))
  } else if (m < 0) {
    return(-n + multiply(n,m+1))
  }
}

multiply(-2,-5)



fabocci <- function(n){
  if(n==1){
    return(1)
  } else {
    return(n*fabocci(n-1))
  }
}

fabocci(100)
is.infinite(Inf)


# inefficient in calculating all possible branches when M is too big
recursive.change <- function(M,c){
  best.num <- Inf
  if (M == 0) {
    return(0)
  } 
  for (i in 1:length(c)){
    if (M >= c[i]) {
      num.coin <- recursive.change(M-c[i],c)
      if ((num.coin+1) < best.num){
        best.num <- num.coin+1
      }
    }
  }
  return(best.num)
}

system.time(recursive.change(30,c(1,2,5)))


# Attempt the superficially harder task of doing this for each omount of money m from 0 to M
# this algorithm will be more efficient, notice when i == 0 is a new situation compared with 
# Python
DPChange <- function(M, c){
  best.num <- rep(NA, M)
  for (m in 1:M) {
    best.num[m] <- Inf
    for (i in 1:length(c)){
      if (m > c[i]) {
        if (best.num[m-c[i]]+1<best.num[m]){
          best.num[m] <- best.num[m-c[i]]+1
        }
      } else if (m ==c[i]){
        best.num[m] <- 1
      }
    }
  }
  return(best.num[M])
}

system.time(DPChange(63,c(1,5,10,25)))


# same efficiency in R with recursive change function
recDC <- function(c, M, known){
  min <- M
  if (M %in% c){
    known[M] <- 1
    return(1)
  } else if (known[M] > 0){
    return(known[M])
  } else {
    for (i in 1:length(c)){
      if (M >= c[i]) {
        num.coin <- 1 + recDC(c, (M-c[i]), known)
        if (num.coin < min){
          min <- num.coin
          known[M] <- min
        }
      }
    }
  }
  return(min)
}


system.time(recDC(c(1,2,5),30,rep(0,30)))
