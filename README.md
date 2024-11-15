# Vítor Mussa Tavares Gomes' master research data pipeline

This repo contains the data pipeline for my master research project.
It is made of two main components:
- reddit-tracer: a Python app for tracing the history of a subreddit.
- eda: Jupyter notebooks for exploratory data analysis with NLP.

# reddit-tracer

This is a simple Python app for tracing the history of the subreddit.
It uses the [Pushshift API](http://pushshift.io/) to get a subreddit comments for the specified time period.

## Usage
For the data collection, you must set the following environment variables:
- `SUBREDDIT_NAME`: the name of the subreddit you want to trace.
- `TRACER_START_TIME`: the start time of the trace in iso format.
- `TRACER_END_TIME`: the end time of the trace in iso format.

Then you need to run the app main module:

```bash
python main.py
```

The app will create a `data` folder with the collected data.
To concatenate the data into a single file, you can run the following command:

```bash
python concatenation.py
```
 
# eda

This folder contains Jupyter notebooks for exploratory data analysis with NLP.
The `models.ipynb` notebook contains the code for training the models used in the research.
The `vis.ipynb` notebook contains the code for the visualizations used in the research.
To reproduce the results, you should download the trained models from the Zenodo repository and place them in the `models` folder. You can access the models [here](https://zenodo.org/records/14104692).

The `eda/models` folder structure should be like this:
```
models
--- lda_10t
------ lda_10t.gensim
------ lda_10t.gensim.expElogbeta.npy
------ lda_10t.gensim.id2word
------ lda_10t.gensim.state
--- lda_100t
------ lda_100t.gensim
------ lda_100t.gensim.expElogbeta.npy
------ lda_100t.gensim.id2word
------ lda_100t.gensim.state
--- corpus.mm
--- corpus.mm.index
--- dictionary.gensim
```
