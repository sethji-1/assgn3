import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    key=(record[0],record[1])
    value=record
    mr.emit(key,value)
     
    
def reducer(key, list_of_values):
    if key[0]
    
    
    
    
    
    
    
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)        