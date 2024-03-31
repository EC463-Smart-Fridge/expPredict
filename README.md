# Food Item Expiration Date Prediction

## Required files for implementation:
expPredictLambda.py, expirationPredictions.json

## formatData.py
Extracts and reformats food storage time data from foodkeeper.json, and saves to foodkeeperFormatted.json.

## expTimeCalc.py
Uses data from foodkeeperFormatted.py to calculate predicted expiration times for each food product type in the dataset. Predictions are stored in expirationPredictions.json.

## expPredict.py
Takes a food item name as input, matches the input to a food product type in expirationPredictions.json, and calculates and outputs a predicted expiration date for that food item.
