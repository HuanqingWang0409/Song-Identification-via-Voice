# Song Identification Via Voice 
▪	Used **Python** to write an application from scratch which can identify songs from recorded audio via a user-defined database. <br />
▪	Allowed users to easily add songs to the **SQL** database and used the PyAudio package to record input voice.<br />
▪	Adopted the **Discrete Fourier Transformation** to transform time domain signals into frequency domain signals, grouped the resultant signals into 40 chunks per second, and identified the frequency with the highest signal magnitude for each chunk.<br />
▪	Plays the song from the database having the longest matched signal length with the search audio by going through all the possible start times from the songs. <br />

