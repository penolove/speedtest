# speedtest

( one speed trial for X_start per 10 min)
keep the process running for a full day or futher
```
./speedtest.sh >> X_star.txt
```

( one speed trial for xareast per 10 min)
keep the process running for a full day or futher
```
./speedtest.sh >> xareast.txt
```
and edit parse_speed_record.py _____main__
for your file_name wanted to compare


```
python parse_speed_record.py
```
will produce three imgs for  UP_speed, Down_speed, Ping 

![picture](ping(ms).png)
![picture](up_speed(Mbps).png)
![picture](down_speed(Mbps).png)
