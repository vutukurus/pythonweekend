import threading, time

def test_one():
	print "I am test one,i wil take 5 second to coplete"
	time.sleep(5)
	print "test one completed"

def test_two():
	print "I am test two,i wil take 5 second to coplete"
	time.sleep(5)
	print "test two completed"

st_time = time.time()
test_one()
test_two()
end_time = time.time()
print end_time - st_time