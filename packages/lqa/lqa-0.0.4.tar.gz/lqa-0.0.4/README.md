# Local Quadratic Approximation (LQA)
In deep learning tasks, the learning rate determines the update step size in each iteration, which plays a critical role in gradient-based optimization. However, the determination of the appropriate learning rate in practice typically replies on subjective judgement. In this work, we propose a novel optimization method based on local quadratic approximation (LQA). In each update step, given the gradient direction, we locally approximate the loss function by a standard quadratic function of the learning rate. Then, we propose an approximation step to obtain a nearly optimal learning rate in a computationally efficient way. The proposed LQA method has three important features. First, the learning rate is automatically determined in each update step. Second, it is dynamically adjusted according to the current loss function value and the parameter estimates. Third, with the gradient direction fixed, the proposed method leads to nearly the greatest reduction in terms of the loss function. Extensive experiments have been conducted to prove the strengths of the proposed LQA method. The detailed description of the LQA method can be found at https://arxiv.org/abs/2004.03260.

## How to use LQA
### 1. Import the package
```
import lqa
```

### 2. Initialize a LQA worker and train your model. 

The following example shows the necessary parameters: 

* model: your model (based on tensorflow.keras)

* epochs: the number of epochs

* train: training dataset (e.g., [X0, Y0], or a data generator)

* test: testing (or validation) dataset (e.g., [X1, Y1], or a data generator)

* loss: loss function

```
bestmodel = lqa.gd(model, epochs=10, train=[X0,X1], test=[Y0,Y1]], loss='sparse_categorical_crossentropy')
```

### 3. Get the tuned model from the worker.

The tuned model and training records are organized as attributes of the LQA worker.
```
# tuned model
bestmodel.model

# training records, including:
# history[train_loss] - loss on the training dataset
# history[train_acc] - accuracy on the training dataset
# history[test_loss] - loss on the testing dataset
# history[test_acc] - accuracy on the testing dataset
bestmodel.history
```

