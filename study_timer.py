import time, random, winsound
s = 60
p = 0
m = 14
t = 0
ran_quote = ["It all starts with an assumption.(After Basis) (Inductive Step)",
 "It all ends with a conclusion. (Inductive Step)",
 "The rule of inference behind mathematical induction can be expressed in predicate logic as:\n (P(1)^∀k(P(k)->P(k+1))) -> ∀nP(n)",
 "Step 1: For All... Fixed integer! (Mathematical Induction)"
,"Mathematical induction is used to prove a statement true for an (countably) infinite number of cases."
,"Remember to factor out dy/dx after taking the derivative."
,"To find two points where a curve crosses the x-axis, solve for x first. "
 ,"65xy = 65x AND 65y."
 ,"During the basis step, we want to specify variables like P(n)"]


print("Start learning! Don't give up for at least one minute.")
r = len(ran_quote)
print("[Random Tip]\n "+ran_quote[random.randint(0, (r-1))]+"\n")
while s >= 0:
	if (s > 0):
		s -= 1
		p += 1
		if (p%15) == 0  and (p!=60) and (t != 0):
			print(f"Time spent: "+str(t)+":"+str(p))
	elif (s >= 0) and (m > 0):
		s += 60
		p -= 60
		m -= 1
		t += 1
		print(f""+str(t)+" minute(s) have passed.")
	else:
		s -= 1
		print("*"*32)
		print("*Time's up! Look up the answer.*")
		print("*"*32)
		print("*Time's up! Look up the answer.*")
		print("*"*32)
		print("*Time's up! Look up the answer.*")
		print("*"*32)
		# The following code will sound an alarm. If it's annoying, change it.
		winsound.Beep(440,750)
		time.sleep(1)
		winsound.Beep(440,1000)
	time.sleep(1)
