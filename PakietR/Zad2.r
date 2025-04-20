library("readxl")

roln_data <- read_excel("PakietR/ROLN_3179.xlsx",sheet = "OPIS")  

roln_data <- roln_data[,2:2]

words <- c()
for (r in 1:nrow(roln_data)){
    new_words <- strsplit(as.character( roln_data[r,1] )," ")[[1]]
    words <- c(words,new_words)
}

unique_words <- as.data.frame( words[!duplicated(words) & !duplicated(words, fromLast = TRUE)] )
names(unique_words) <- c("słowa")

write.csv(unique_words,"PakietR/słowa.csv",row.names = FALSE)