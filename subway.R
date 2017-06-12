library(ggplot2)
library(scales)

subway <- read.delim('subway.txt',header=TRUE)

ggplot(subway, aes(x=factor(DATE), y=as.integer(PASSENGERS))) + geom_bar(position="dodge", stat="identity",aes(fill=factor(STATION)))
ggplot(data = subway, aes(x = factor(DATE), y = as.integer(PASSENGERS), fill = factor(STATION))) + geom_bar(stat="identity") + scale_y_continuous(labels = comma)
