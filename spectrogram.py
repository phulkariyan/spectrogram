import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

def create_spectrogram(audio_file, output_file):
    # Load the audio file
    y, sr = librosa.load(audio_file)

    # Create the spectrogram
    D = librosa.stft(y)
    S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

    # Plot the spectrogram
    plt.figure(figsize=(12, 8))
    librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='hz')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram')

    # Save the spectrogram as an image file
    plt.savefig(output_file)
    plt.close()

    print(f"Spectrogram saved as {output_file}")

# Example usage
input_file = "path/to/your/audio/file.mp3"  # Replace with your audio file path
output_file = "spectrogram.png"  # Output image file name

create_spectrogram(input_file, output_file)
