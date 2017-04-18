from redis import Redis
from rq import Queue
from my_module import count_words_at_url, do_something_slow

#create a connection to redis and pass it to Queue.
q = Queue(connection=Redis())

result1 = q.enqueue(count_words_at_url, 'http://google.com')
result2 = q.enqueue(do_something_slow, 'foo bar')

