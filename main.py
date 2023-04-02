# python3
import random

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def hash_funct(s):
    ans = 0
    prime = 10000002
    bucket_count = 10
    multiplier = random.randint(1, prime - 1)
    for t in reversed(str(s)):
        ans = (ans * multiplier + ord(t)) % prime
    return ans % bucket_count

def process_queries(queries):
    result = []
   
    buckets = [[] for _ in range(10)]
    for cur_query in queries:
        if cur_query.type == 'add':   
            numb = cur_query.number
            hashed = hash_funct(numb)
            bucket = buckets[hashed]
            for e in bucket:
                if cur_query.number == e.number:
                    e.name = cur_query.name
                    return  
                 
            buckets[hashed] = [cur_query] + bucket 
                
        elif cur_query.type == 'del':
            hashed = hash_funct(numb)
            bucket = buckets[hashed]
            for j in range(len(bucket)):
                if bucket[j].number == cur_query.number:
                    bucket.pop(j)
                    break
        else:
            response = 'not found'
            for s in buckets[hashed]:
                if cur_query.number == s.number:
                    response = s.name
                    break
            result.append(response)   
    return result
            
    

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

