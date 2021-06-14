#Cullin Davis
#Chapter 1
import random
import statistics as st

#4
random.seed(0)
salaries = [round(random.random()*1000000, -3) for _ in range(100)]

#5
print("Question 5")
print(f'Mean w/o statistics module = {sum(salaries)/len(salaries)}')
print(f'Mean with statistics module = {st.mean(salaries)}')

def getMed(l):
    l.sort()
    llen = len(l)
    i = (llen)//2
    if llen % 2:
        return l[i]
    else:

        return (l[i-1]+l[i])/2

print(f'Median w/o statistics module = {getMed(salaries)}')
print(f'Median with statistics module = {st.median(salaries)}')

print(f'Mode w/o statistics moduel = {max(salaries, key = salaries.count)}')
print(f'Mode with statistics module = {st.mode(salaries)}')

def gets2(l):
    m = sum(l)/len(l)
    d = [(x-m)**2 for x in l]
    return sum(d)/(len(l)-1)
print(f'Variance w/o statistics module = {gets2(salaries)}')
print(f'Variance with statistics module = {st.variance(salaries)}')
print(f'Standard Deviation w/o statistics module = {gets2(salaries)**.5}')
print(f'Standard Deviation with statistics module = {st.stdev(salaries)}')
print('\nQuestion 6')
print('Range = {max(salaries)-min(salaries)}')
print('CV = {st.stdev(salaries)/st.mean(salaries)}')

def iqr(l):
    q = st.quantiles(l)
    iq = q[2]-q[1]
    return iq

print(f'IQR = {iqr(salaries)}')

def qcd(l):
    q = st.quantiles(l)
    cd = (q[2]-q[1])/(q[1]+q[2])
    return cd
print(f'QCD = {qcd(salaries)}')

def mms(l):
    r = max(l)-min(l)
    d = [(x-min(l))/r for x in l]
    return d
a7 = mms(salaries)

b7 = [(x-st.mean(salaries))/st.stdev(salaries) for x in salaries]

#print(a7)
#print(b7)
print("\nQuestion 8")
def cov(a, b):
    am = st.mean(a)
    bm = st.mean(b)
    s = 0
    for i,j in zip(a,b):
        x = i - am
        y = j - bm
        s += x*y/len(a)
    return s
print(cov(a7,b7))
print(f'Cov = {cov(a7, b7)}')
print(f'rho = {cov(a7, b7)/(st.stdev(a7)*st.stdev(b7))}')

