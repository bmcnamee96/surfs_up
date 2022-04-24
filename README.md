# Surfs Up Challenge
### Overview
The purpose of this challenge was to use sqlalchemy to filter a sqlite database for temperature and precipitation. By using sqlalchemy we can quickly and concisely search and filter the db for what we need.  In this challenge, we filtered for the month of June and then the month of December.

## Analysis
### Results
1) The mean temp for June is almost 4 degrees higher than December.
2) The minimum temp for December is 8 degrees lower than June.
3) The maximum temp for December is only 2 degrees lower than June.

The differences between the two months (June and December) are not that different.

### Summary
In order to learn more about the two months, we should look at the other table in the database.
Some good queries would be:
- dec_prcp = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date) == 12).all()
- june_prcp = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date) == 6).all()

After running these queries we can see that December is a more rainy month than June.

- session.query(Measurement.station, func.avg(Measurement.tobs)).filter(extract('month', Measurement.date) == 12).\
    group_by(Measurement.station).order_by(func.avg(Measurement.tobs).desc()).all()
- session.query(Measurement.station, func.avg(Measurement.tobs)).filter(extract('month', Measurement.date) == 6).\
    group_by(Measurement.station).order_by(func.avg(Measurement.tobs).desc()).all()
    
These queries show the station that has the highest average temperature for each month. After running these queries we can see that the station of USC00514830 is the hottest for the month of December and the station of USC00519397 is the hottest for the month of June.
