# Flask_Application - TensorFlow Serving with Docker
In this project, we will deploy a Pre-trained TensorFlow model with the help of TensorFlow Serving with Docker, and we will also create a visual web interface using Flask web framework which will serve to get predictions from the served TensorFlow model and help end-users to consume through API calls. 

The model is entirely based on the official Tensorflow Regression tutorial notebook available here: https://www.tensorflow.org/tutorials/keras/regression.
This model predicts the fuel efficiency of late -1970s and early 1980s automobiles. The model is based on Tensorflow and stored in the Tensorflow
[SavedModel format](https://github.com/bouknify/Flask_Application/tree/main/dnn/1).
The input features used for this model are attributes of the cars. The output of the model is a single float value.

## Installation Instructions

Prerequisite: Please install [docker](https://docs.docker.com/get-docker/)

1. Pull down the source code from this Git repository:

```sh
$ git clone https://github.com/bouknify/Flask_Application.git
$ cd Flask_Application
```

2. Create and start containers:

If you inspect docker-compose.yml you can see that:

    a. The Tensorflow Serving image is obtained from its public docker hub store (image: tensorflow/serving:2.4.0).

    b. The dnn_service image is defined by the Dockerfile. It's the Containerised Python Web Application (Flask Framework).

And now we can simply run both services together with:  
```sh
$ docker-compose up
```
3. Navigate to 'http://localhost:5000' to view the web interface! and start the predictions...

![Test Image 4](https://github.com/bouknify/Flask_Application/blob/main/static/images/index.PNG)

## Testing

PyTest is a testing framework that allows us to write test codes using python. It helps to write tests from unit tests to functional tests.

To run all the tests:

```sh
$ python -m pytest -v
```

