
install.packages("keras")
library(keras)


## Establish the number of words to use as features
max_features = 10000

## Cut off text of review after # of max_len
max_len = 30

## Load it up!
imdb = dataset_imdb(num_words = max_features)

## split the set into training and test sets; list of integers (~50 Mb)
c(c(x_train, y_train), c(x_test, y_test)) %<-% imdb

x_train = pad_sequences(x_train, maxlen = max_len)
x_test = pad_sequences(x_test, maxlen = max_len)


model = keras_model_sequential() %>%
  layer_embedding(input_dim = 10000, output_dim = 8,
                  input_length = max_len) %>%
  layer_flatten() %>%
  layer_dense(units=1, activation = "sigmoid")


model %>% compile(
  optimizer = "rmsprop",
  loss = "binary_crossentropy",
  metrics = c("acc")
)

summary(model)

history = model %>% fit(
  x_train, y_train,
  epochs = 10,
  batch_size = 32,
  validation_split = 0.2
)
plot(history)


model2 =  keras_model_sequential() %>%
  layer_embedding(input_dim = 10000, output_dim = 8,
                  input_length = max_len) %>%
  layer_flatten() %>%
  layer_dense(units=1, activation = "sigmoid")
