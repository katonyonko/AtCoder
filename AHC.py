import io
import sys
import glob

#同じフォルダにtest_caseという名称でテストケースを置けば、test関数等が動く
path='/Users/katonyonko'
files = sorted(glob.glob(path+"/test_case/*"))

#以下が提出するコード
import time
import math
from random import randint, shuffle, uniform, choice, sample
from heapq import heappop, heappush
from collections import deque

def idx(i,j):
  return i*(i+1)//2+j

xxx=[(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (11, 0), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (12, 0), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11), (12, 12), (13, 0), (13, 1), (13, 2), (13, 3), (13, 4), (13, 5), (13, 6), (13, 7), (13, 8), (13, 9), (13, 10), (13, 11), (13, 12), (13, 13), (14, 0), (14, 1), (14, 2), (14, 3), (14, 4), (14, 5), (14, 6), (14, 7), (14, 8), (14, 9), (14, 10), (14, 11), (14, 12), (14, 13), (14, 14), (15, 0), (15, 1), (15, 2), (15, 3), (15, 4), (15, 5), (15, 6), (15, 7), (15, 8), (15, 9), (15, 10), (15, 11), (15, 12), (15, 13), (15, 14), (15, 15), (16, 0), (16, 1), (16, 2), (16, 3), (16, 4), (16, 5), (16, 6), (16, 7), (16, 8), (16, 9), (16, 10), (16, 11), (16, 12), (16, 13), (16, 14), (16, 15), (16, 16), (17, 0), (17, 1), (17, 2), (17, 3), (17, 4), (17, 5), (17, 6), (17, 7), (17, 8), (17, 9), (17, 10), (17, 11), (17, 12), (17, 13), (17, 14), (17, 15), (17, 16), (17, 17), (18, 0), (18, 1), (18, 2), (18, 3), (18, 4), (18, 5), (18, 6), (18, 7), (18, 8), (18, 9), (18, 10), (18, 11), (18, 12), (18, 13), (18, 14), (18, 15), (18, 16), (18, 17), (18, 18), (19, 0), (19, 1), (19, 2), (19, 3), (19, 4), (19, 5), (19, 6), (19, 7), (19, 8), (19, 9), (19, 10), (19, 11), (19, 12), (19, 13), (19, 14), (19, 15), (19, 16), (19, 17), (19, 18), (19, 19), (20, 0), (20, 1), (20, 2), (20, 3), (20, 4), (20, 5), (20, 6), (20, 7), (20, 8), (20, 9), (20, 10), (20, 11), (20, 12), (20, 13), (20, 14), (20, 15), (20, 16), (20, 17), (20, 18), (20, 19), (20, 20), (21, 0), (21, 1), (21, 2), (21, 3), (21, 4), (21, 5), (21, 6), (21, 7), (21, 8), (21, 9), (21, 10), (21, 11), (21, 12), (21, 13), (21, 14), (21, 15), (21, 16), (21, 17), (21, 18), (21, 19), (21, 20), (21, 21), (22, 0), (22, 1), (22, 2), (22, 3), (22, 4), (22, 5), (22, 6), (22, 7), (22, 8), (22, 9), (22, 10), (22, 11), (22, 12), (22, 13), (22, 14), (22, 15), (22, 16), (22, 17), (22, 18), (22, 19), (22, 20), (22, 21), (22, 22), (23, 0), (23, 1), (23, 2), (23, 3), (23, 4), (23, 5), (23, 6), (23, 7), (23, 8), (23, 9), (23, 10), (23, 11), (23, 12), (23, 13), (23, 14), (23, 15), (23, 16), (23, 17), (23, 18), (23, 19), (23, 20), (23, 21), (23, 22), (23, 23), (24, 0), (24, 1), (24, 2), (24, 3), (24, 4), (24, 5), (24, 6), (24, 7), (24, 8), (24, 9), (24, 10), (24, 11), (24, 12), (24, 13), (24, 14), (24, 15), (24, 16), (24, 17), (24, 18), (24, 19), (24, 20), (24, 21), (24, 22), (24, 23), (24, 24), (25, 0), (25, 1), (25, 2), (25, 3), (25, 4), (25, 5), (25, 6), (25, 7), (25, 8), (25, 9), (25, 10), (25, 11), (25, 12), (25, 13), (25, 14), (25, 15), (25, 16), (25, 17), (25, 18), (25, 19), (25, 20), (25, 21), (25, 22), (25, 23), (25, 24), (25, 25), (26, 0), (26, 1), (26, 2), (26, 3), (26, 4), (26, 5), (26, 6), (26, 7), (26, 8), (26, 9), (26, 10), (26, 11), (26, 12), (26, 13), (26, 14), (26, 15), (26, 16), (26, 17), (26, 18), (26, 19), (26, 20), (26, 21), (26, 22), (26, 23), (26, 24), (26, 25), (26, 26), (27, 0), (27, 1), (27, 2), (27, 3), (27, 4), (27, 5), (27, 6), (27, 7), (27, 8), (27, 9), (27, 10), (27, 11), (27, 12), (27, 13), (27, 14), (27, 15), (27, 16), (27, 17), (27, 18), (27, 19), (27, 20), (27, 21), (27, 22), (27, 23), (27, 24), (27, 25), (27, 26), (27, 27), (28, 0), (28, 1), (28, 2), (28, 3), (28, 4), (28, 5), (28, 6), (28, 7), (28, 8), (28, 9), (28, 10), (28, 11), (28, 12), (28, 13), (28, 14), (28, 15), (28, 16), (28, 17), (28, 18), (28, 19), (28, 20), (28, 21), (28, 22), (28, 23), (28, 24), (28, 25), (28, 26), (28, 27), (28, 28), (29, 0), (29, 1), (29, 2), (29, 3), (29, 4), (29, 5), (29, 6), (29, 7), (29, 8), (29, 9), (29, 10), (29, 11), (29, 12), (29, 13), (29, 14), (29, 15), (29, 16), (29, 17), (29, 18), (29, 19), (29, 20), (29, 21), (29, 22), (29, 23), (29, 24), (29, 25), (29, 26), (29, 27), (29, 28), (29, 29)]
def inv(i):
  return xxx[i]

score=0
class Ahc:

  def __init__(self,b):
    self.start=time.perf_counter()
    self.TL=1.7
    self.b=b
    self.bi=[None]*465
    for i in range(465): self.bi[self.b[i]]=i
    self.ansK=0
    self.ans=[]

  def score(self, K):
    return 100000-5*K

  def simple_score(self, K, ans):
    b=self.b.copy()
    for i in range(K):
      x,y,xd,yd=ans[i]
      b[idx(x,y)],b[idx(xd,yd)]=b[idx(xd,yd)],b[idx(x,y)]
    E=0
    for i in range(29):
      for j in range(i+1):
        if b[idx(i,j)]>b[idx(i+1,j)]:E+=1
        if b[idx(i,j)]>b[idx(i+1,j+1)]:E+=1
    if E==0: return 100000-5*K
    else: return 50000-50*E

  def big_ball(self,i,j):
    if j==0: return i-1,j
    elif j==i: return i-1,j-1
    else:
      if self.bc[idx(i-1,j-1)]>self.bc[idx(i-1,j)]: return i-1,j-1
      else: return i-1,j
  
  def small_ball(self,i,j):
    if self.bc[idx(i+1,j)]<self.bc[idx(i+1,j+1)]: return i+1,j
    else: return i+1,j+1

  def init_ans(self):
    self.bc=self.b.copy()
    self.bic=self.bi.copy()
    for i in range(465):
      nowi,nowj=inv(self.bic[i])
      while nowi>0:
        ei,ej=self.big_ball(nowi,nowj)
        if self.bc[idx(ei,ej)]<self.bc[idx(nowi,nowj)]: break
        self.bc[idx(nowi,nowj)],self.bc[idx(ei,ej)]=self.bc[idx(ei,ej)],self.bc[idx(nowi,nowj)]
        self.bic[i],self.bic[self.bc[idx(nowi,nowj)]]=self.bic[self.bc[idx(nowi,nowj)]],self.bic[i]
        self.ansK+=1
        self.ans.append((nowi,nowj,ei,ej))
        nowi,nowj=ei,ej

  def init_ans2(self):
    self.bc=self.b.copy()
    self.bic=self.bi.copy()
    self.ansKc=0
    self.ansc=[]
    for i in reversed(range(465)):
      nowi,nowj=inv(self.bic[i])
      while nowi<29:
        ei,ej=self.small_ball(nowi,nowj)
        if self.bc[idx(ei,ej)]>self.bc[idx(nowi,nowj)]: break
        self.bc[idx(nowi,nowj)],self.bc[idx(ei,ej)]=self.bc[idx(ei,ej)],self.bc[idx(nowi,nowj)]
        self.bic[i],self.bic[self.bc[idx(nowi,nowj)]]=self.bic[self.bc[idx(nowi,nowj)]],self.bic[i]
        self.ansKc+=1
        self.ansc.append((nowi,nowj,ei,ej))
        nowi,nowj=ei,ej
    if self.ansKc<self.ansK:
      self.ansK=self.ansKc
      self.ans=self.ansc

  def stoc_ans(self):
    self.bc=self.b.copy()
    self.bic=self.bi.copy()
    self.ansKc=0
    self.ansc=[]
    for i in range(465):
      nowi,nowj=inv(self.bic[i])
      while nowi>0:
        if self.ansKc<int(self.ansK*0.75): ei,ej=self.big_ball(nowi,nowj)
        elif nowj==0: ei,ej=nowi-1,0
        elif nowj==nowi: ei,ej=nowi-1,nowj-1
        elif self.bc[idx(nowi-1,nowj-1)]<self.bc[idx(nowi,nowj)]<self.bc[idx(nowi-1,nowj)]: ei,ej=nowi-1,nowj
        elif self.bc[idx(nowi-1,nowj)]<self.bc[idx(nowi,nowj)]<self.bc[idx(nowi-1,nowj-1)]: ei,ej=nowi-1,nowj-1
        else:
          a,b=self.bc[idx(nowi-1,nowj-1)],self.bc[idx(nowi-1,nowj)]
          x=uniform(0,1)
          if x<a/(a+b): ei,ej=nowi-1,nowj-1
          else: ei,ej=nowi-1,nowj
        if self.bc[idx(ei,ej)]<self.bc[idx(nowi,nowj)]: break
        self.bc[idx(nowi,nowj)],self.bc[idx(ei,ej)]=self.bc[idx(ei,ej)],self.bc[idx(nowi,nowj)]
        self.bic[i],self.bic[self.bc[idx(nowi,nowj)]]=self.bic[self.bc[idx(nowi,nowj)]],self.bic[i]
        self.ansKc+=1
        self.ansc.append((nowi,nowj,ei,ej))
        nowi,nowj=ei,ej
    if self.ansKc<self.ansK:
      self.ansK=self.ansKc
      self.ans=self.ansc

  def solve(self):
    self.init_ans()
    while time.perf_counter()- self.start<self.TL:
      self.stoc_ans()

def main(i):
  global score
  if i>=0:
    writefile = open(path+'/test_case/output/'+str(i).zfill(4)+'output.txt', 'w')
    with open(files[i]) as f:
      lines = f.read().split('\n')
    sys.stdin = io.StringIO('\n'.join(lines))
  b=[]
  for j in range(30):
    x=list(map(int,input().split()))
    b+=x
  C=Ahc(b)
  C.solve()
  if i==-1:
    print(C.ansK)
    for i in range(C.ansK):
      print(*C.ans[i])
  else:
    writefile.write(str(C.ansK)+"\n")
    for i in range(C.ansK):
      writefile.write(' '.join([str(C.ans[i][j]) for j in range(4)])+"\n")
    score+=C.simple_score(C.ansK,C.ans)
    # print(C.simple_score(C.ansK,C.ans))

def test(s,g):
  for i in range(s,g):
    main(i)
  print(score*1.5)

if __name__ == "__main__":
  #現在のスコア 13421715
  flg=1
  if flg==0: main(-1)
  elif flg==1: test(0,100)