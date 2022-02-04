# Song Identification Via Voice 
▪	Used **Python** to write an application that identifies songs from recorded audio via a user-defined database. <br />
▪	Allowed users to easily add songs to a SQL database and used the PyAudio package and wave module to record input voice. <br />
▪	Adopted the Discrete Fourier Transformation to transform time domain signals into frequency domain signals, grouped the resultant signals into 40 chunks per second, and, 
for frequency intervals 30-40Hz, 40-80Hz, 80-120Hz and 120-180Hz respectively, identified the frequency with the highest magnitude within each interval and for each chunk. <br />
▪	Played the matched song from the database having the longest consecutively matched signal length with the search audio by going through all the possible start times from the target songs. <br />
