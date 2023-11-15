from .generate_data_tasks import generate_wave

import numpy as np
import matplotlib.pyplot as plt

def compute_fft_psd(wave, sampling_rate, plot=False):
    """
    Compute the FFT and Power Spectral Density (PSD) from a sampled wave.
    
    Parameters:
    - wave (numpy array): The sampled wave data.
    - sampling_rate (float): The sampling rate of the wave (samples per second).
    - plot (bool): If True, plot the time-domain signal and the frequency-domain signal.
    
    Returns:
    - results (dict): A dictionary containing the time vector ('time'), frequency vector ('fft_freq'), 
                      FFT values ('fft_vals'), and PSD values ('psd_vals').
    """
    # Time vector
    duration = len(wave) / sampling_rate
    time = np.linspace(0, duration, len(wave), endpoint=False)
    
    # Compute the FFT
    fft_vals = np.fft.fft(wave)
    fft_freq = np.fft.fftfreq(len(fft_vals), 1/sampling_rate)

    # Compute the Power Spectral Density (PSD)
    psd_vals = np.abs(fft_vals) ** 2

    # Only keep the positive half of the spectrum (and frequencies)
    half_len = len(psd_vals) // 2
    fft_freq = fft_freq[:half_len]
    psd_vals = psd_vals[:half_len]

    # If plot is True, create the plots
    if plot:
        plt.figure(figsize=(12, 6))

        # Plot the time domain signal
        plt.subplot(2, 1, 1)
        plt.plot(time, wave)
        plt.title("Time Domain Signal")
        plt.xlabel("Time (seconds)")
        plt.ylabel("Amplitude")

        # Plot the PSD
        plt.subplot(2, 1, 2)
        plt.stem(fft_freq, psd_vals, linefmt='b', markerfmt=" ", basefmt="-b")
        plt.title("Frequency Domain Signal - Power Spectral Density")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Power")
        plt.tight_layout()
        plt.show()

    # Package results in a dictionary
    results = {
        'time': time,
        'fft_freq': fft_freq,
        'fft_vals': fft_vals[:half_len],  # Return only the positive frequencies
        'psd_vals': psd_vals,
    }
    
    return results

# Example usage:
# Assuming 'wave' is your sampled wave data array and 'sampling_rate' is your sampling rate

#wave = generate_wave(r=1, n=30, intervals = int(1e8))
#sampling_rate = 100
#import time
#t0=time.time()
#fft_psd_results = compute_fft_psd(wave, sampling_rate, plot=False)
#print(time.time() - t0)


def task_fft(intervals=1e8):
    wave = generate_wave(r=1, n=30, intervals = intervals)
    sampling_rate = 100
    fft_psd_results = compute_fft_psd(wave, sampling_rate, plot=False)
    return None




def generate_2d_wave(size, r, n_terms):
    """
    Generates a 2D wave pattern as a sum of sine waves.
    
    Parameters:
    - size (int): The size of the 2D grid (size x size).
    - r (float): The base amplitude factor for the sine terms.
    - n_terms (int): The number of terms in the wave sum.

    Returns:
    - wave (numpy.ndarray): The generated 2D wave pattern.
    """
    # Create a 2D grid of points
    x = np.linspace(0, 2 * np.pi, size)
    y = np.linspace(0, 2 * np.pi, size)
    X, Y = np.meshgrid(x, y)

    # Initialize the wave
    wave = np.zeros((size, size))

    # Add sine terms to the wave
    for n in range(1, n_terms + 1):
        wave += (r ** n) * np.sin(n * np.pi * (X * Y))

    return wave

def fft_2d_and_power_spectral(wave, plot=False):
    """
    Computes the 2D Fast Fourier Transform (FFT) and Power Spectral Density (PSD)
    of a 2D wave pattern and optionally plots the results.
    
    Parameters:
    - wave (numpy.ndarray): The 2D wave pattern.
    - plot (bool): If True, plot the wave and its power spectral density.

    Returns:
    - fft_2d (numpy.ndarray): The FFT of the 2D wave pattern.
    - psd (numpy.ndarray): The power spectral density of the 2D wave pattern.
    """
    # Compute the 2D FFT
    fft_2d = np.fft.fft2(wave)

    # Shift the zero frequency component to the center of the spectrum
    fft_shifted = np.fft.fftshift(fft_2d)

    # Compute the Power Spectral Density (PSD)
    psd = np.abs(fft_shifted) ** 2

    if plot:
        # Plot the original wave
        plt.figure(figsize=(10, 4))

        plt.subplot(1, 2, 1)
        plt.imshow(wave, extent=(0, 2 * np.pi, 0, 2 * np.pi), cmap='viridis')
        plt.colorbar()
        plt.title('Original 2D wave')

        # Plot the power spectral density
        plt.subplot(1, 2, 2)
        plt.imshow(np.log(psd), extent=(0, 2 * np.pi, 0, 2 * np.pi), cmap='viridis')
        plt.colorbar()
        plt.title('Power Spectral Density of the 2D wave')
        plt.tight_layout()
        plt.show()

    return fft_2d, psd

# Generate a 2D wave pattern
#size = 2**12
#r = 0.9
#n_terms = 5
#wave = generate_2d_wave(size, r, n_terms)

# Compute the FFT and Power Spectral Density, with plotting
#fft_2d, psd = fft_2d_and_power_spectral(wave, plot=False)

def task_fft_2d(size=2**12):
    r = 0.9
    n_terms = 5
    wave = generate_2d_wave(size, r, n_terms)

    # Compute the FFT and Power Spectral Density, with plotting
    fft_2d, psd = fft_2d_and_power_spectral(wave, plot=False)
    return None

