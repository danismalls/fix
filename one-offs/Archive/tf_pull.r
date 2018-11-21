library(elasticsearchr)
install.packages("elastic")
library(elastic)
library(dplyr)
library(tidyr)

connect(es_host = "tellfinder-elasticsearch.uncharted.software", es_port = 9200, es_transport_schema  = "http")


query1='{
"size" : 0,
            "query" : {
            "bool" : {
            "filter" : [
            
            {
              "term" : {"feature.site_name":"backpage"}
            },
              {
              "range" : {
              "locality.dateBegin" : {
              "gte" : "2017-04-07",
              "lte" : "2018-07-18"
              }
              }  
              }
              ]
            }
            },
            "aggs" : {
            "postsbyday" : {
            "date_histogram" : {
            "field" : "locality.dateBegin",
            "interval" : "1d"
            }
            }}}'


query = '{
  "size" : 0,
      "query" : {
      "bool" : {
      "filter" : [ {
        "term" : {
        "feature.keywords.classifier" : "young"
        }
        }]
}
},
"aggs" : {
"locations" : {
"terms": {
"field" : "locality.label",
"size" : 10
}
}
}
}'


query = '{
  "size": "0",
      "aggs" : {
        "sources": {
          "terms": {
            "field":"feature.site_name",
              "size": 1
}
}
}
}'

fir = Search(index = "mx_ht_documents_2_sift_6.1", size=10000, body = query1, asdf = TRUE)$hits$hits
fir$`_source.feature.site_name`[[16]]


df = bind_rows(fir)


count(index = "mx_ht_documents_2_sift_6.1")

# Get all results - one approach is to use a while loop
res <- Search(index = "mx_ht_documents_2_sift_6.1", body=query1, scroll="5m")
out <- list()
hits <- 1
while(hits != 0){
  res <- scroll(scroll_id = res$`_scroll_id`)
  hits <- length(res$hits$hits)
  if(hits > 0)
    out <- c(out, res$hits$hits)
}
length(out)
out[[1]]

df %>% 
    filter(_source.feature.scrapedtime >= input$dates[1], _source.feature.scrapedtime <= input$dates[2]) %>%
    count(type) %>% 
    arrange(desc(n)) %>%
    select("Action Type" = type, "Freq" = n) %>%
    head(20) 

attach(df)
detach(df)

df$`_source.feature.scrapedtime`= as.Date(df$`_source.feature.scrapedtime`)
df %>% count(`_source.feature.scrapedtime`[[3]]) 
