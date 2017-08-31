def time_convert(time):
    t = tuple((str(time).split(':')))
    hh = t[0]
    mm = t[1]
    return t

def time_diff(time_in, time_out):
    t0 = time_convert(time_in)
    t1 = time_convert(time_out)
    hours = str(int(t1[0]) - int(t0[0]))
    minutes = str(int(t1[1]) - int(t0[1]))
    return (hours+":"+minutes)

def clock_in(worker_dict, name, time_in):
    info_list = worker_dict.get(name)
    info_list[0] = time_in
    worker_dict[name] = info_list

def clock_out(worker_dict, name, time_out):
    info_list = worker_dict.get(name)
    info_list[1] = time_out
    info_list[2] = time_diff(info_list[0], info_list[1])
    worker_dict[name] = info_list

def main():
    workers = {"George Spelvin": [0,0,0], "Jane Doe": [0,0,0], "John Smith": [0,0,0]}
    print(workers.get("George Spelvin"))   # should print [0,0,0]
    clock_in(workers, "George Spelvin", "08:00")
    clock_out(workers, "George Spelvin", "17:00")
    print(workers.get("George Spelvin"))   # should print [8, 17, 9]

if __name__ == "__main__":
    main()
