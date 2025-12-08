# F1 Qatar 2025 GP Prediction — Performance Modeling Using Weighted Z-Scores

This project predicts driver performance for the 2025 Qatar Grand Prix using a weighted performance index based on z-score. It uses historical data(qualifying, race pace, sprint results, Qatar-track performance) to rank the drivers.

---
## Main Insights

Additional data could help with developing this model into an ML-based prediction model.

This z-score calculation only accounts for previous races and the drivers without previous qatar track data, naturally, rank lower.

Model can be improved further with supplemental data to compare how z-score estimation does against an ML-based model. 

---
## Tools  
Python • pandas • fastf1 API • Jupyter

---
## Notebooks

data1.ipynb — Data Cleaning

model.ipynb — Z-score calculations

---
## Results

According to the model, the strongest projected performers are:
1. Lando Norris
2. Max Verstappen
3. Lewis Hamilton
4. Oscar Piastri
5. George Russell

---
## Results after Qatar 25 GP 
Qatar 2025 GP ended with top 3 being:
 1. Piastri
 2. Verstappen
 3. Sainz (not in my list of top 3)
However, at the Abu Dhabi GP, the following week, the top 3 was as follows:
 1. Verstappen
 2. Piastri
 3. Norris, where he won the title

--
## Evaluation
Looking at the results of the overall season, I could argue that the z-score was not so far off, since this seasons top 3 were in my predicted top 5 list. Regardless of Norris not ranking in top 3 during the Qatar GP, the final 3 of this season had a place in my ranking list. Hamilton and Russell also were not far down the actual rankings of this season, where Russell ranked 4th and Hamilton 6th in the championship.  

This is not to say my z-score ran as expected since this was an estimation for the Qatar GP and not the whole season. If the Qatar GP went accordingly with my estimated ranking list, the Abu Dhabi GP wouldn't have taken place. 

---
## Author  
**Inci Ozdemir**  
