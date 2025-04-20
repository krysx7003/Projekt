cars_data <- read.csv("PakietR/Cars93.csv")

mean_weight <- mean(as.numeric( cars_data$Weight ), na.rm=FALSE)

max_car <- cars_data[which.max(cars_data$Price), ]

mean_cylinders <- mean(as.numeric( cars_data$Cylinders ), na.rm=TRUE)

vans <- cars_data[cars_data$Type == "Van", ]
vans_from_us <- vans[vans$Origin == "non-USA",]

has_numbers <- grepl("[0-9]", cars_data$Model)
numeric_models <- cars_data[has_numbers, ]


toyota_cars <- cars_data[cars_data$Manufacturer == "Toyota",] 
widest_toyota <- max(toyota_cars$Width)

subaru_cars <- cars_data[cars_data$Manufacturer == "Subaru",] 
widest_subaru <- max(subaru_cars$Width)

cars_from_usa <- cars_data[cars_data$Origin == "USA",]
longer_than_s <- cars_from_usa[cars_from_usa$Width > widest_subaru,]
longer_than_st <- longer_than_s[longer_than_s$Width > widest_toyota,]
