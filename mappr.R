init <- function() {
  library(igraph)
  library(igraphdata)
  data(package = "igraphdata")
}

appr <- function(g, seed_index, alpha, tolerance) {
  len <- g.vcount()
  app_vector <- rep(0, len)
  
  r_vector <- rep(0, len)
  r_vector[seed_index] <- 0
  
  dw_vector <- g()
  while (r(v))
  dw <- 
  
}

export_to_gefi <- function(g) {
  library(rgexf)
  g.gexf <- igraph.to.gexf(g)
  
  f <- file("network.gexf")
  writeLines(g.gexf$graph, con = f)
  close(f)
}