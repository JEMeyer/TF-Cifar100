The setup for this whole project took me several days to get working but with pip3 you should be good to go.
Since I used TensorFlow this will be unable to run on Loki. You will need to move this code to a system that has Python3 and pip3 installed, as well as TensorFlow already installed.

The only extra libraries I ended up using in addtion to TensorFlow was matplotlib.

To run the network as it is configured now (both label bytes and very deep) simply run:

> python3 cifar100_train.py

If you get any missing packages, install them using pip3. The error message will tell you what packages you are missing.
The network will output as it is learning, as as long as you have a folder in your pwd called 'output_data', the text file of all the data points will be output there with the current UTC ticks as the name.
My code should automatically download the CIFAR dataset if it is not already available locally. This will only need to be done for the first run and won't re-download for any subsequent runs.

Once the network runs, you can create a graph using my custom python script 'visualize_data.py'.

visualize_data usage:
> python3 visualize_data.py INPUT TITLE OUTPUT

an example of this using data I have uploaded to loki would be:
> python3 visualize_data.py "output_data/Multi 30 Hidden.txt" "Deep Run (30 Hidden/Both Labels)" "Multi 30 Hidden.png"

That will read in output_data/Multi 30 Hidden.txt for the data points, createa  graph with a heading of "Deep Run (30 Hidden/Both Labels)" and will output that to a png file in the pwd called 'Multi 30 Hidden'