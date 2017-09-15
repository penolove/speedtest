from itertools import groupby
from dateutil.parser import parse
import matplotlib.pyplot as plt
import numpy as np

def is_date(string):
    try: 
        parse(string)
        return True
    except ValueError:
        return False

def where(t):
    return [i for i, x in enumerate(t) if x]

def parse_tuples(parts):
    hour=parse(parts[0]).hour
    ping=int(parts[2].replace("Ping: ","").replace(" ms",""))
    down_v=float(parts[3].replace("Download speed: ","").replace(" Mbps",""))
    up_v=float(parts[4].replace("Upload speed: ","").replace(" Mbps",""))
    return (hour,ping,down_v,up_v)



def list_mean(x):
    if(len(x)!=0):
        return int(sum(x)/float(len(x)))
    
def reduce_records(all_records):
    all_records_reduced=[]
    for hour, g1 in groupby(sorted(all_records), lambda t: t[0]):
        g1=[i for i in g1]
        ping=[i[1] for i in g1]
        down_v=[i[2] for i in g1]
        up_v=[i[3] for i in g1]
        all_records_reduced.append((hour,list_mean(ping),list_mean(down_v),list_mean(up_v)))
    return all_records_reduced

def parse_wrapper(file_name="T_start.txt"):
    text_file = open(file_name, "r")
    lines = text_file.readlines()
    target =[is_date(i.replace('\n','')) for i in lines]
    t = where(target)
    t_success = where([x-y==5 for x,y in zip(t[1:],t)])
    target_success =[t[i] for i in t_success]
    all_records=[parse_tuples(lines[i:i+5]) for i in target_success]
    return reduce_records(all_records)

def save_img(all_comapny_records, color, index=2, title='foo'):
    for records_reduced, color_ in zip(all_comapny_records, color):
        x_list = np.array([i[0] for i in records_reduced])
        y_list = np.array([i[index] for i in records_reduced])
        plt.axhline(y=np.mean(y_list), linestyle='dashed', color=color_)
        plt.plot(x_list, y_list, color=color_)
    plt.ylabel(title, fontsize=16)
    plt.xlabel('day_hour', fontsize=16)

    plt.savefig(title+'.png')
    plt.clf()


if __name__ == "__main__":
    all_company_records = []
    company = ["X_star.txt","Xyphone.txt","Xareast.txt"]
    color_list = ["#9467bd","#ff7f0e","r"] #puple , orange,red
    for cp in company:
        reduced_records = parse_wrapper(file_name=cp)
        all_company_records.append(reduced_records)
    save_img(all_company_records, color_list, index=1, title='ping(ms)')
    save_img(all_company_records, color_list, index=2, title='down_speed(Mbps)')
    save_img(all_company_records, color_list, index=3, title='up_speed(Mbps)')
