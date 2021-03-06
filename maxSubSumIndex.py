# -*- coding: cp1254 -*-
from time import time
import random
def maxSubSum1(a):
    seqStart = 0
    seqEnd = -1
    maxSum = 0;
    for i in range(0, len(a)):
        for j in range(i, len(a)):
            thisSum = 0
            for k in range(i,j+1):
                thisSum = thisSum + a[k]
                if(thisSum > maxSum):
                    maxSum = thisSum
                    seqStart = i
                    seqEnd = j
    return {'y0':maxSum, 'y1':seqStart ,'y2':seqEnd }
    

def maxSubSum2(a):
    seqStart = 0
    seqEnd = -1
    maxSum = 0;
    for i in range(0, len(a)):
        thisSum = 0
        for j in range(i, len(a)):
            thisSum = thisSum + a[j]
            if(thisSum > maxSum):
                maxSum = thisSum
                seqStart = i
                seqEnd = j
    return {'y0':maxSum, 'y1':seqStart ,'y2':seqEnd }

def maxSubSum4(a):
    seqStart = 0
    seqEnd = -1
    maxSum = 0;
    thisSum = 0
    i = 0
    for j in range(0, len(a)):
        thisSum = thisSum + a[j]
        if(thisSum > maxSum):
            maxSum = thisSum
            seqStart = i
            seqEnd = j
        elif(thisSum < 0):
            i = j + 1
            thisSum = 0
    return {'y0':maxSum, 'y1':seqStart ,'y2':seqEnd }

if __name__ == '__main__':
    #10 elemanlý dizi zamanlarý
    a = [4, -3, 5, -2, -1, 2, 6, -2, 7, 10]
    t0 = time()
    maxSum = maxSubSum1(a)
    t1 = time()
    print 'maxSum1 = %d' % maxSum['y0']
    print 'maxSum1 seqStart = %d' % maxSum['y1']
    print 'maxSum1 seqEnd = %d' % maxSum['y2']
    print 'maxSubSum1 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum2(a)
    t1 = time()
    print 'maxSum2 = %d' % maxSum['y0']
    print 'maxSum2 seqStart = %d' % maxSum['y1']
    print 'maxSum2 seqEnd = %d' % maxSum['y2']
    print 'maxSubSum2 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum4(a)
    t1 = time()
    print 'maxSum4 = %d' % maxSum['y0']
    print 'maxSum4 seqStart = %d' % maxSum['y1']
    print 'maxSum4 seqEnd = %d' % maxSum['y2']
    print 'maxSubSum4 zaman = %f' %(t1-t0)

    a = []
    #50 elemanlý dizi zamanlarý
    for i in range(50):
        x = int(random.uniform(-10, 10))
        a.append(x)
    t0 = time()
    maxSum = maxSubSum1(a)
    t1 = time()
    print 'maxSum1 = %d' % maxSum['y0']
    print 'maxSum1 seqStart = %d' % maxSum['y1']
    print 'maxSum1 seqEnd = %d' % maxSum['y2']
    print 'maxSubSum1 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum2(a)
    t1 = time()
    print 'maxSum2 = %d' % maxSum['y0']
    print 'maxSum2 seqStart = %d' % maxSum['y1']
    print 'maxSum2 seqEnd = %d' % maxSum['y2']
    print 'maxSubSum2 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum4(a)
    t1 = time()
    print 'maxSum4 = %d' % maxSum['y0']
    print 'maxSum4 seqStart = %d' % maxSum['y1']
    print 'maxSum4 seqEnd = %d' % maxSum['y2']
    print 'maxSubSum4 zaman = %f' %(t1-t0)
    a = []
    #100 elemanlý dizi oluþturalým
    for i in range(100):
        x = int(random.uniform(-10, 10))
        a.append(x)
    t0 = time()
    maxSum = maxSubSum1(a)
    t1 = time()
    print 'maxSum1 = %d' % maxSum['y0']
    print 'maxSum1 seqStart = %d' % maxSum['y1']
    print 'maxSum1 seqEnd = %d' % maxSum['y2']
    print 'maxSubSum1 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum2(a)
    t1 = time()
    print 'maxSum2 = %d' % maxSum['y0']
    print 'maxSum2 seqStart = %d' % maxSum['y1']
    print 'maxSum2 seqEnd = %d' % maxSum['y2']
    print 'maxSubSum2 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum4(a)
    t1 = time()
    print 'maxSum4 = %d' % maxSum['y0']
    print 'maxSum4 seqStart = %d' % maxSum['y1']
    print 'maxSum4 seqEnd = %d' % maxSum['y2']
    print 'maxSubSum4 zaman = %f' %(t1-t0)
    a = []
    #500 elemanlý dizi oluþturalým
    for i in range(500):
        x = int(random.uniform(-10, 10))
        a.append(x)
    t0 = time()
    maxSum = maxSubSum1(a)
    t1 = time()
    print 'maxSum1 = %d' % maxSum['y0']
    print 'maxSum1 seqStart = %d' % maxSum['y1']
    print 'maxSum1 seqEnd = %d' % maxSum['y2']
    print 'maxSubSum1 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum2(a)
    t1 = time()
    print 'maxSum2 = %d' % maxSum['y0']
    print 'maxSum2 seqStart = %d' % maxSum['y1']
    print 'maxSum2 seqEnd = %d' % maxSum['y2']
    print 'maxSubSum2 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum4(a)
    t1 = time()
    print 'maxSum4 = %d' % maxSum['y0']
    print 'maxSum4 seqStart = %d' % maxSum['y1']
    print 'maxSum4 seqEnd = %d' % maxSum['y2']
    print 'maxSubSum4 zaman = %f' %(t1-t0)
        
    a = []
    #1000 elemanlý dizi oluþturalým
    for i in range(1000):
        x = int(random.uniform(-10, 10))
        a.append(x)
    t0 = time()
    maxSum = maxSubSum1(a)
    t1 = time()
    print 'maxSum1 = %d' % maxSum['y0']
    print 'maxSum1 seqStart = %d' % maxSum['y1']
    print 'maxSum1 seqEnd = %d' % maxSum['y2']
    print 'maxSubSum1 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum2(a)
    t1 = time()
    print 'maxSum2 = %d' % maxSum['y0']
    print 'maxSum2 seqStart = %d' % maxSum['y1']
    print 'maxSum2 seqEnd = %d' % maxSum['y2']
    print 'maxSubSum2 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum4(a)
    t1 = time()
    print 'maxSum4 = %d' % maxSum['y0']
    print 'maxSum4 seqStart = %d' % maxSum['y1']
    print 'maxSum4 seqEnd = %d' % maxSum['y2']
    print 'maxSubSum4 zaman = %f' %(t1-t0)
    

    a = []
    #10000 elemanlý dizi oluþturalým
    for i in range(10000):
        x = int(random.uniform(-10, 10))
        a.append(x)
    t0 = time()
    maxSum = maxSubSum1(a)
    t1 = time()
    print 'maxSum1 = %d' % maxSum['y0']
    print 'maxSum1 seqStart = %d' % maxSum['y1']
    print 'maxSum1 seqEnd = %d' % maxSum['y2']
    print 'maxSubSum1 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum2(a)
    t1 = time()
    print 'maxSum2 = %d' % maxSum['y0']
    print 'maxSum2 seqStart = %d' % maxSum['y1']
    print 'maxSum2 seqEnd = %d' % maxSum['y2']
    print 'maxSubSum2 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum4(a)
    t1 = time()
    print 'maxSum4 = %d' % maxSum['y0']
    print 'maxSum4 seqStart = %d' % maxSum['y1']
    print 'maxSum4 seqEnd = %d' % maxSum['y2']
    print 'maxSubSum4 zaman = %f' %(t1-t0)

    a = []
    #100000 elemanlý dizi oluþturalým
    for i in range(100000):
        x = int(random.uniform(-10, 10))
        a.append(x)
    t0 = time()
    maxSum = maxSubSum1(a)
    t1 = time()
    print 'maxSum1 = %d' % maxSum['y0']
    print 'maxSum1 seqStart = %d' % maxSum['y1']
    print 'maxSum1 seqEnd = %d' % maxSum['y2']
    print 'maxSubSum1 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum2(a)
    t1 = time()
    print 'maxSum2 = %d' % maxSum['y0']
    print 'maxSum2 seqStart = %d' % maxSum['y1']
    print 'maxSum2 seqEnd = %d' % maxSum['y2']
    print 'maxSubSum2 zaman = %f' %(t1-t0)
    t0 = time()
    maxSum = maxSubSum4(a)
    t1 = time()
    print 'maxSum4 = %d' % maxSum['y0']
    print 'maxSum4 seqStart = %d' % maxSum['y1']
    print 'maxSum4 seqEnd = %d' % maxSum['y2']
    print 'maxSubSum4 zaman = %f' %(t1-t0)
