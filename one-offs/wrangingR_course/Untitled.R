install.packages("dslabs")
install.packages("readr")
library(dslabs)
library(readr)

getwd()

setwd()

system.file("extdata", package="dslabs")
list.files(getwd())

filename <-"murders.csv"
path <- system.file("extdata", package = "dslabs")
file.copy(file.path(path, filename), getwd())


#to view first few lines of a file
read_lines("murders.csv", n_max = 3)

#tibble vs. dataframe
read.csv # dataframe
read_csv # tibble

#to avoid setting characters to factors, set stringsAsFactors = FALSE

#url downloads
url = "http://blahblah blah"
#temporary downloads
#create temp file
tmp_filename = tempfile()
#save file to temp filename
download.file(url, tmp_filename)



dat = read_csv(tmp_filename)
file.remove(tmp_filename)