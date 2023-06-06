### EKAK ihale data temizleme

library(tidyverse)

df <- ilanSozlesme1001

summary(df)

df$price <- str_replace(df$price, "TRY" , "")

df$price <- as.numeric(gsub(",", ".", gsub("\\.", "", df$price)))
#df$date_signed <- as.Date(df$date_signed)

sum(df$price)/1000000000

df <- arrange(df, desc(price))
sum(df$price[1:10])/1000000000

top10_share = sum(df$price[1:10])/ sum(df$price)
## 64%
top100_share = sum(df$price[1:100])/ sum(df$price)
# 94.9 %

df_buyer  <- df %>% group_by(buyer) %>% summarise(total_contract = sum(price)) %>% arrange(desc(total_contract))
df_seller  <- df %>% group_by(seller) %>% summarise(total_contract = sum(price)) %>% arrange(desc(total_contract))
top10_sellerShare <- sum(df_seller$total_contract[1:10])/ sum(df_seller$total_contract)

