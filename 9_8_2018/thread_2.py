import threading, time

def test_one():
	print "I am test one,i wil take 5 second to coplete"
	time.sleep(5)
	print "test one completed"

def test_two():
	print "I am test two,i wil take 5 second to coplete"
	time.sleep(5)
	print "test two completed"

#thread creation..
a = threading.Thread(target=test_one)
b = threading.Thread(target=test_two)

#run the thread..
st_time = time.time()
a.start()
b.start()
a.join()
b.join()
end_time = time.time()
print end_time - st_time
print "threads completed"


