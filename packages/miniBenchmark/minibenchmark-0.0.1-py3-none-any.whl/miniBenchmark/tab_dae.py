import numpy as np
import tensorflow
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def train_dae(df, batch_size=256,):
    """
    Train a Denoising Autoencoder on the provided DataFrame.

    Parameters:
    - df: pandas DataFrame with each row as an observation.
    - batch_size: int, size of the batch used during training.

    Returns:
    - autoencoder: trained Keras model.
    - encoder: encoder part of the Keras model.
    - scaler: MinMaxScaler object fitted to the df.
    """
    # Normalize the data
    scaler = MinMaxScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(df))#, columns=df.columns)

    # Set the fraction of the corruption process
    noise_factor = 0.5

    # Create noisy data
    X_train_noisy = df_scaled + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=df_scaled.shape)
    X_train_noisy = np.clip(X_train_noisy, 0., 1.)

    input_dim = df_scaled.shape[1]  # number of features

    # Define the encoder and decoder layers
    input_layer = Input(shape=(input_dim,))
    encoded = Dense(256, activation='relu')(input_layer)
    encoded = Dense(128, activation='relu')(input_layer)
    encoded = Dense(64, activation='relu')(encoded)

    decoded = Dense(128, activation='relu')(encoded)
    decoded = Dense(256, activation='relu')(encoded)
    decoded = Dense(input_dim, activation='sigmoid')(decoded)

    # Build the Model
    autoencoder = Model(input_layer, decoded)

    # Compile the model
    autoencoder.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')

    # Train the model
    autoencoder.fit(X_train_noisy, df_scaled,
                    epochs=30,
                    batch_size=batch_size,
                    shuffle=True,
                    validation_split=0.2)

    # Define an encoder model for encoding input data
    encoder = Model(input_layer, encoded)

    # Return the autoencoder, the encoder, and the scaler
    return autoencoder, encoder, scaler

# Example usage:
# Assuming df is your DataFrame

from .generate_data_tasks import generate_dataset
#ids, X, y = generate_dataset(M=2**18, n=2**8, task='regression', random_state=42)
#autoencoder, encoder, scaler = train_dae(X, batch_size=2**12)

def task_tab_dae(size = 10):

    ids, X, y = generate_dataset(M=2**(size+8), n=2**size, task='regression', random_state=42)
    autoencoder, encoder, scaler = train_dae(X, batch_size=2**11)


    
