/*********************************************
 * OPL 12.6.3.0 Model
 * Author: Admin
 * Creation Date: 01-04-2016 at 19:31:05
 version: 0.1 (Changelog attached, 16/04/01)
 *********************************************/

float budget=...;
int nEvents=...; //number of events
range rEvents=1..nEvents;
int nBets=...; //number of bets +1 (variable representing ID)
range rBets=1..nBets;
float ratesTable[rEvents][rBets]=...;

float x[rBets]=...;

float maxRisk=...; //defined by User OR 
float minGain=...; //defined by User 

 