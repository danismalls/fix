library(tidyr)
library(dplyr)
library(plotly)

install.packages("geohash")
library(geohash)
install.packages('flexdashboard')
library(flexdashboard)

setwd("~/repos/TF/fostasesta")


pricesdf = as.data.frame(read.csv('geohash_prices.csv', header = TRUE, sep=","))

pricesdf %>% summary()
head(pricesdf,200)

pricesdf$docbin = cut(pricesdf$doc_count,3,labels=c("low","medium","high"))



%>% 
  animation_button( 
    buttons = list(
      list(
        label = 'Play',
        method = 'animate',
        args = list( frame =~frame, fromcurrent = TRUE, mode = "immediate")
      ), 
      label='Pause', 
      method = 'animate', 
      args = list(duration = 0, redraw = FALSE, mode = 'immediate'))
  )


colnames(pricesdf)
head(pricesdf)

pricesdf %>% count()

p <- pricesdf %>%
  plot_ly(
    x = ~x,
    y = ~doc_count,
    frame = ~f,
    type = 'scatter',
    mode = 'markers',
    showlegend = F
  )

sub = pricesdf %>% filter(1:4)

sub = slice(pricesdf, 1:1000)

sub %>% mutate(DATE = as.Date(as.Date(date), "%b"))

mutate(as.Date(sub$date),format ="%B")

pricesdf$date_mon = as.Date(pricesdf$date, format = "%B")

as.Date(sub$date)

library(lubridate)
sub %>% mutate(date = ymd(date))

sub %>% count(lat,lon)

pricesdf %>% filter(date == '2018-04-01') %>% 
  plot_geo(
              lat=~ne_lat, 
              lon=~ne_lon,
              #color=~ceiling(avgRate),
              color=~ceiling(avgRate), 
              text=~doc_count, 
              #frame=~date, 
              showlegend=FALSE) %>% toWebGL()
p  



pricesdf %>% group_by(date) %>% tally(doc_count)


#Accumulate!
accumulate_by <- function(dat, var) {
  var <- lazyeval::f_eval(var, dat)
  lvls <- plotly:::getLevels(var)
  dats <- lapply(seq_along(lvls), function(x) {
    cbind(dat[var %in% lvls[seq(1, x)], ], frame = lvls[[x]])
  })
  dplyr::bind_rows(dats)
}

d <- pricesdf %>%
  group_by(date) %>%
  tally(avgRate)
 # accumulate_by(~date)


head(d)


p2 <- d %>%
  plot_ly(
    x = ~date, 
    y = ~n,
    #frame = ~date_mon, 
    type = 'bar',
    showlegend = F,
    showline = F,
    showticklabels = F,
    showgrid = F
 #   mode = 'lines'
    #line = list(simplyfy = F)
  ) %>% 
  layout(
    xaxis = list(
      title = "Date",
      zeroline = F
    )
  )

p



colnames(pricesdf)
colnames(dailypricedf)
head(dailypricedf)


pricesdf$numdocbin = cut(pricesdf$doc_count,3)
pricesdf$date_mon = factor(format(as.Date(pricesdf$date), "%B"), levels = month.name)
pricesdf$ratebin = cut(pricesdf$avgRate,4)

pricesdf = pricesdf %>% count(date,avgRate)

boulder_daily_precip_month <- boulder_daily_precip %>%
  group_by(month) %>%
  summarise(sum_daily = sum(avgRate))


p1 = pricesdf %>% 
  #format(as.Date(date),format ="%B") %>%
  plot_geo(locationmode = 'USA-states',
           lat=~ne_lat, 
           lon=~ne_lon,
           #size=~numdocbin,
           #size=~ceiling(avgRate),
           size =~as.numeric(ratebin),
           #color=~ratebin,
           alpha = 0.7,
           mode = 'markers',
           frame=~date, 
           showlegend=TRUE) %>%
  # add_markers(color = ~doc_count, frame = ~date_mon) %>%
  
  #colorbar(title = "Price Per Hour", tickprefix = '$') %>%
  layout(
    title = 'Time Lapse of Average Price per Service <br> January 2018 - October 2018',
    geo = list(scope = 'usa', 
               showland = T, 
               landcolor = toRGB("#080d12"),
               #plot_bgcolor = '#191A1A', paper_bgcolor = '#191A1A',
               #projection = list(type = 'conic conformal'), 
               projection = list(type = 'albers usa'),
               showlakes = TRUE,
               showcountries = TRUE,
               lakecolor = toRGB('white')
    )
  ) 

p1


p <- subplot(p1, p2, nrows = 2) %>%
  layout(title = "",
         xaxis = list(domain=list(x=c(0,0.5),y=c(0,0.5))),
         scene = list(domain=list(x=c(0.5,1),y=c(0,0.5))),
         xaxis2 = list(domain=list(x=c(0.5,1),y=c(0.5,1))),
         showlegend=FALSE,showlegend2=FALSE)
p
