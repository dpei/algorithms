# Apr 25 2016

# input is a matrix

graph <- matrix(c(1,2,3,2,3,1),ncol = 2)
graph <- rbind(graph, cbind(graph[,2],graph[,1]))


frequency <- function(graph.in){
  my.list <- graph.in[,1]
  result <- rep(0,max(my.list))
  for (i in my.list){
    result[i] <- result[i] + 1
  }
  return(result)
}
  

find.node <- function(tour){
  for (i in tour){
    if (freq[i] != 0){
      return(i)
    }
  }
  return(-1)
}

# find any path the walks through the graph
# The infinity loop bug happened because a global 
# variable was used at the begining of loop so it 
# will never decreased into NULL
find.path <- function(graph.in, tour, next.s){
  for (i in nrow(graph.in)){
    if (graph.in[i,1] == next.s){
      current <- graph.in[i,]
      graph.in <- graph.in[-i,]
      if (is.vector(graph.in) == TRUE) {
        graph.in <- NULL
      } else {
        graph.in <- graph.in[!(graph.in[,1]==current[2] & graph.in[,2]==current[1]),]
      }
      tour <- c(tour, current[1])
      return(find.path(graph.in, tour, current[2]))
    }
  }
  tour <- c(tour, next.s)
  return(c(tour, graph.in))
}

# TODO: Calculate freq change into helper()
helper <- function(graph.in, tour, next.s){
  tour <- find.path(graph.in, tour, next.s)
  u <- find.node(tour)
  while (sum(freq) != 0) {
    sub <- find.path(c(), u)
    # attach a tour into current tour
    tour <- 
    u <- find.node(tour)
  }
  return(tour)
}