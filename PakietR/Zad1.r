library("readxl")

roln_data <- read_excel("PakietR/ROLN_3179.xlsx",sheet = "TABLICA")  

raw_data <- as.data.frame(lapply(roln_data[5:nrow(roln_data), 3:ncol(roln_data) ],as.numeric))
names(raw_data) <- c("2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018",
                    "2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018")
raw_data

control_data <- as.data.frame(lapply(roln_data[4:4, 3:ncol(roln_data) ],as.numeric))
names(control_data) <- c("2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018",
                        "2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018")
control_data

calculated_data <- as.data.frame(t( colSums(raw_data) ))
calculated_data

full_data=rbind(control_data,calculated_data)
house_data <- full_data[,1:13]
house_data$Źródło = c("Wiersz POLSKA","Suma pozostałych")
house_data <- house_data[, c(ncol(house_data), 1:(ncol(house_data)-1))]
house_data

land_data <- full_data[,14:ncol(full_data)]
land_data$Źródło = c("Wiersz POLSKA","Suma pozostałych")
land_data <- land_data[, c(ncol(land_data), 1:(ncol(land_data) - 1))]
land_data

house_diff <- house_data[1, -1] != house_data[2, -1]
house_diff <- as.data.frame(house_diff)
house_diff$Źródło = c("Wiers POLSKA niepoprawny")
house_diff <- house_diff[, c(ncol(house_diff), 1:(ncol(house_diff) - 1))]
house_diff

house_data <- rbind(house_data,house_diff)

land_diff <- land_data[1, -1] != land_data[2, -1]
land_diff <- as.data.frame(land_diff)
land_diff$Źródło = c("Wiers POLSKA niepoprawny")
land_diff <- land_diff[, c(ncol(land_diff), 1:(ncol(land_diff) - 1))]
land_diff

land_data <- rbind(land_data,land_diff)

columns <- c("Źródło", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018")
text_row <- data.frame(matrix(NA, nrow = 1, ncol = length(columns)))
names(text_row) <- columns
text_row$Źródło <- "Gospodarstwa"

house_data <- rbind(text_row,house_data)

text_row$Źródło <- "Użytki rolne"
land_data <- rbind(text_row,land_data)

merged_data <- rbind(house_data,land_data)
write.csv(merged_data,"PakietR/pol.csv",row.names = FALSE)

for (r in 1:nrow(raw_data)){
    for (c in 1:13 ){
        raw_data[r,c] <- raw_data[r,c+13]/raw_data[r,c]
    }

}

raw_data <- raw_data[,1:13]