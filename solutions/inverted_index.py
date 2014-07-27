import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    #document_id and text both are string
    value=record[0]
    key=record[1]
    words=key.split()
    for w in words:
        mr.emit_intermediate(w,value)
        
           
def reducer(key, list_of_values):
    #key is words and list_of_values is doc_id's 
    lst=[]
    for v in list_of_values:
        if v not in lst:
            lst.append(v)
    mr.emit((key,lst))    
    
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)

    
        