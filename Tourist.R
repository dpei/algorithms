# Manhattan tourist matrix in R is specified from vertical distance
# However in Python matrix is specificed from horizontal

h <- matrix(c(3,3,0,3,2,2,7,3,4,4,3,1), ncol = 3)
v <- matrix(c(1,4,4,0,6,4,2,5,5,4,2,2), ncol = 4)

row <- 4
col <- 4
manhattan.toursit(h,v,row,col)

manhattan.toursit <- function(h, v, row, col){
  MT <- matrix(rep(NA, row*col), ncol = col)
  MT[1,1] <- 0
  for (j in 2:row){
    MT[1,j] <- MT[1,j-1] + h[1,j-1]
  }
  for (i in 2:col){
    MT[i,1] <- MT[i-1,1] + v[i-1, 1]
  }
  for (i in 2:col){
    for (j in 2:row){
      MT[i,j] <- max(MT[i-1,j]+v[i-1,j], MT[i,j-1]+h[i,j-1])
    }
  }
  return(MT)
}

