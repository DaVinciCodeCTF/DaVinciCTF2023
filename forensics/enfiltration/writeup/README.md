# Enfiltration writeup

This challenge is about matching audio's enf with power grid data.

In audio metadata, you can see that the audio was recorded in 2019.

You can retrieve National frequency data in England in 2019 from https://www.nationalgrideso.com/industry-information/balancing-services/frequency-response-services/historic-frequency-data

You can use this script to extract enf data from audio : https://github.com/deerajnagothu/pyenf_extraction

You then have to write a script (cf wu.py) that matches enf data to national grid data, to find out the date where the audio was recorded

Note : Since there are differences between the real enf data and the ones retrieved by any script (due to fft approximations), the method to calculate the distance between 2 points should not rely on standard deviation summing.
