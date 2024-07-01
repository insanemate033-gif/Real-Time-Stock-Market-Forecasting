# Real Time Stock Market Forecasting

This repository contains an implementation of ensemble deep learning models to forecast or predict stock price. We used Alpha Vantage 
API to pull stock data(open,high,low,close,volume) and scraped news headlines from inshorts to perform sentiment analysis.

## Architecture
![](imgs/arch.PNG)


## Getting Started

It would be a better idea to create a conda environment and work in isolation 

- Create a virtual environment
```
conda create -n envname python=3.6.8 anaconda 
conda activate envname
```
Use ```conda deactivate``` to deactivate the environment
- Clone this repository
```
git clone --depth 1 https://github.com/insanemate033-gif/Real-Time-Stock-Market-Prediction-using-Ensemble-DL-and-Rainbow-DQN.git && cd Real-Time-Stock-Market-Prediction-using-Ensemble-DL-and-Rainbow-DQN
```
- Install the requirements
```
pip install -r requirements.txt
```
- Get an Alpha Vantage API key

To run ```animate.py``` you require a free [Alpha Vantage API Key](https://www.alphavantage.co/support/#api-key). 
Enter the key in ```key=''``` parameter inside the animate.py file 
``` 
ts = TimeSeries(key='',output_format='pandas')
```
- Run python script

To vizualize the forecast. Remember the data pulled by the API will not update the plot if the market is closed. 
```
python animate.py
```
To get heatmap visualization for correlation analysis on ^NSEI(Nifty50)
```
python heatmap.py
```

## Acknowledgements

- [@huseinzol05](https://github.com/huseinzol05/) for deep learning models
- [@sentdex](https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ) for plotting tutorials
- [Vader Sentiment](https://github.com/cjhutto/vaderSentiment)
- [Alpha Vantage API](https://www.alphavantage.co/) for stock data
- [Inshorts](inshorts.com) for news headlines

