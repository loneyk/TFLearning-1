import tensorflow as tf
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

print(tf.__version__)
gpu_ok = tf.config.list_physical_devices('GPU')
print(gpu_ok)
print("GPUs: ", len(tf.config.experimental.list_physical_devices('GPU')))

# new test file


# test1111



