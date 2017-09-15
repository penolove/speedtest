while true;
do
    date '+%Y-%m-%d %H:%M:%S';
    pyspeedtest;
    #pyspeedtest -s 210.200.212.249;
    sleep 600;
done
