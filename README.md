Audio Spike Detector in Python

This project analyzes audio files (WAV format) to identify and log potential audio spikes or drops in signal levels.

Features:

- Reads WAV files with specific characteristics: mono channel, 16-bit sample width, and 44100 Hz sample rate.
- Normalizes audio samples to a user-defined maximum value for consistent analysis.
- Identifies samples exceeding a user-defined threshold (both positive and negative).
- Identifies sudden drops in signal level between consecutive samples.
- Logs identified spikes and drops in separate text files for further review.
- Plots the normalized audio waveform visually.

Requirements:

    Python 3.x
    matplotlib library
    wave library

Usage:

    Clone the repository:

    git clone https://github.com/your-username/audio_spike_detector.git
    pip install matplotlib wave

Edit the script (main.py) to adjust:

    filename: Path to the WAV file you want to analyze.
    threshold: Positive threshold value for detecting spikes.
    nthreshold: Negative threshold value for detecting drops.

Run the script:

    python main.py

This will generate two log files:

    log_file_over.txt: Contains timestamps and values of samples exceeding the thresholds.
    log_file_drop.txt: Contains timestamps and values of sudden drops in signal level.

A plot of the normalized audio waveform will also be displayed.

Code Structure:

    main.py: Main script handling file I/O, normalization, analysis, logging, and plotting.
    file_manager.py: Functions for reading WAV data and converting it to usable samples.

License:

This project is licensed under a permissive license (to be determined). Please refer to the LICENSE file for details.

Contributing:

Feel free to contribute to this project by suggesting improvements, fixing bugs, or extending functionalities.
