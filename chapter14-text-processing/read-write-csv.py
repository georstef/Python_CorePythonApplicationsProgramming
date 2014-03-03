import csv

DATA = (
    (1, 'John', 'Mercedes A-CLASS'),
    (2, 'George', 'RF600, VFR800'),
    (3, 'Fotis', 'Seat'),
    )



if __name__=='__main__':
    print('--- write CSV ---')
    f = open('read-write-csv.csv', 'w')
    writer = csv.writer(f, lineterminator='\n')
    #for record in DATA: 
    #    writer.writerow(record) # one record at a time
    writer.writerows(DATA) # all records at once writer.writerows(iterable)
    f.close()
    print('done')

    print('--- read CSV ---')
    f = open('read-write-csv.csv', 'r')
    reader = csv.reader(f)
    for aa, name, vehicles in reader:
        print('A/A:', aa, ' NAME:', name, 'VEHICLES:', vehicles)
    f.close()

    
