from tensorflow.keras import backend as K

def dice_coefficient(y_true, y_pred):
    eps = 1e-6
    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    intersection = K.sum(y_true_f * y_pred_f)
    return (2. * intersection) / (K.sum(y_true_f * y_true_f) + K.sum(y_pred_f * y_pred_f) + eps) #eps pour éviter la division par 0 

def get_output_size_image(new_model):
    n = len(new_model.layers)-1
    for i in range(n,0,-1):
        A = list(new_model.layers[i].output.shape)
        if len(A)==4:
            _, IMG_HEIGHT, IMG_WIDTH,IMG_CHANNELS = A
            return IMG_HEIGHT, IMG_WIDTH # 4 argument pour une image

