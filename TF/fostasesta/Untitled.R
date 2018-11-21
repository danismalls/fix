library(tidyr)
library(plotly)

setwd("~/Downloads")

pricesdf = as.data.frame(read.csv('geohash_prices.csv', header = TRUE, sep=","))
