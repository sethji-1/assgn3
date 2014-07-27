import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    diction={}
    person_a=record[0]
    person_b=record[1]
    if person_a in diction:
        diction[person_a].append(person_b)
    else:
        diction[person_a]=[person_b]
    for key in diction:
        mr.emit_intermediate(key,diction[key])
      
def reducer(key, list_of_values):
    total=len(list_of_values)
    mr.emit((key,total))
    
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)    
                    
    
    