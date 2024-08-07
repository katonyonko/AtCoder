git config --global user.email katonyonko@yahoo.co.jp
git config --global user.name "katonyonko"

#再帰関数を書くとき
import sys
sys.setrecursionlimit(10**6)

#n以下の素数を列挙(10**6くらいまでは高速に動く)
import math
def Eratosthenes(n):
  prime=[]
  furui=list(range(2,n+1))
  while furui[0]<math.sqrt(n):
    prime.append(furui[0])
    furui=[i for i in furui if i%furui[0]!=0]
  return prime+furui

#素因数分解はここからコピーするのが多分速い
def gcd(a, b):
  while b: a, b = b, a % b
  return a
def lcm(a, b):
  return a // gcd(a, b) * b
def isPrimeMR(n):
  d = n - 1
  d = d // (d & -d)
  L = [2, 7, 61] if n < 1<<32 else [2, 3, 5, 7, 11, 13, 17] if n < 1<<48 else [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
  for a in L:
    t = d
    y = pow(a, t, n)
    if y == 1: continue
    while y != n - 1:
      y = y * y % n
      if y == 1 or t == n - 1: return 0
      t <<= 1
  return 1
def findFactorRho(n):
  m = 1 << n.bit_length() // 8
  for c in range(1, 99):
      f = lambda x: (x * x + c) % n
      y, r, q, g = 2, 1, 1, 1
      while g == 1:
          x = y
          for i in range(r):
              y = f(y)
          k = 0
          while k < r and g == 1:
              ys = y
              for i in range(min(m, r - k)):
                  y = f(y)
                  q = q * abs(x - y) % n
              g = gcd(q, n)
              k += m
          r <<= 1
      if g == n:
          g = 1
          while g == 1:
              ys = f(ys)
              g = gcd(abs(x - ys), n)
      if g < n:
          if isPrimeMR(g): return g
          elif isPrimeMR(n // g): return n // g
          return findFactorRho(g)
def primeFactor(n):
  i = 2
  ret = {}
  rhoFlg = 0
  while i * i <= n:
      k = 0
      while n % i == 0:
          n //= i
          k += 1
      if k: ret[i] = k
      i += i % 2 + (3 if i % 3 == 1 else 1)
      if i == 101 and n >= 2 ** 20:
          while n > 1:
              if isPrimeMR(n):
                  ret[n], n = 1, 1
              else:
                  rhoFlg = 1
                  j = findFactorRho(n)
                  k = 0
                  while n % j == 0:
                      n //= j
                      k += 1
                  ret[j] = k
  if n > 1: ret[n] = 1
  if rhoFlg: ret = {x: ret[x] for x in sorted(ret)}
  return ret
def divisors(N):
  pf = primeFactor(N)
  ret = [1]
  for p in pf:
      ret_prev = ret
      ret = []
      for i in range(pf[p]+1):
          for r in ret_prev:
              ret.append(r * (p ** i))
  return sorted(ret)
  
#numpyの高速化
from numba import njit
@njit(cache=True)

#累積和
A=np.array([1,2,3,4,5])
np.cumsum(A) #[1,3,6,10]
np.sum(A)-np.cumsum(np.append(0, A[:len(A)-1])) #逆累積和[15, 14, 12,  9,  5]

#複数行の読み込み
import sys
s = sys.stdin.readlines()

#dequeueの方が若干早いらしい
from collections import deque
dq = deque()
# 後ろへデータを挿入
dq.append(データ)
# 前へデータを挿入
dq.appendleft(データ)
# 後ろのデータの取り出し
dq.pop()
# 前のデータを取り出し
dq.popleft()
# dequeが空になるまで繰り返し
while dq:

#bit の性質a + b − (a xor b) = 2 × (a and b)
#bit全探索をやる場合はitertools.product()を使いましょう
import itertools
import pprint
l1 = ['a', 'b', 'c']
l2 = ['X', 'Y', 'Z']
p = itertools.product(l1, l2)
for v in p:
  print(v)
p2 = itertools.product(l1, repeat=2) #こんな指定もできる

#Union Find
import sys
sys.setrecursionlimit(10**6)
class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * n
  def find(self, x):
    if self.parents[x] < 0:
      return x
    else:
      self.parents[x] = self.find(self.parents[x])
      return self.parents[x]
  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if x == y:
      return
    if self.parents[x] > self.parents[y]:
       x, y = y, x
    self.parents[x] += self.parents[y]
    self.parents[y] = x
  def size(self, x):
    return -self.parents[self.find(x)]
  def same(self, x, y):
    return self.find(x) == self.find(y)
  def members(self, x):
    root = self.find(x)
    return [i for i in range(self.n) if self.find(i) == root]
  def roots(self):
    return [i for i, x in enumerate(self.parents) if x < 0]
  def group_count(self):
    return len(self.roots())
  def all_group_members(self):
    return {r: self.members(r) for r in self.roots()}
  def __str__(self):
    return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

#Segment Tree
class SegTree:
    X_unit = 1 << 30
    X_f = min
 
    def __init__(self, N):
        self.N = N
        self.X = [self.X_unit] * (N + N)
 
    def build(self, seq):
        for i, x in enumerate(seq, self.N):
            self.X[i] = x
        for i in range(self.N - 1, 0, -1):
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])
 
    def set_val(self, i, x):
        i += self.N
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])
 
    def fold(self, L, R):
        L += self.N
        R += self.N
        vL = self.X_unit
        vR = self.X_unit
        while L < R:
            if L & 1:
                vL = self.X_f(vL, self.X[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.X_f(self.X[R], vR)
            L >>= 1
            R >>= 1
        return self.X_f(vL, vR)

    def get_val(self,idx):
        return self.X[idx+self.N]

#遅延セグ木 0-indexed、演算はmaxの例を書いているが、変更する場合はunitとclassmethodの部分を変える
#モノイドAがモノイドXに右作用する
#https://maspypy.com/segment-tree-%e3%81%ae%e3%81%8a%e5%8b%89%e5%bc%b72 1-indexedと書かれているが、以下のコードは0-indexed
class LazySegTree:
    X_unit = 0
    A_unit = 0

    #作用を受ける側のモノイドの演算
    @classmethod
    def X_f(cls, x, y):
        return max(x,y)

    #作用素の演算
    @classmethod
    def A_f(cls, x, y):
        return max(x,y)

    #作用素の積が積の作用素になるように定義する
    @classmethod
    def operate(cls, x, a):
        return max(x,a)

    def __init__(self, N):
        self.N = N
        self.X = [self.X_unit] * (N + N)
        self.A = [self.A_unit] * (N + N)

    def build(self, seq):
        for i, x in enumerate(seq, self.N):
            self.X[i] = x
        for i in range(self.N - 1, 0, -1):
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def _eval_at(self, i):
        return self.operate(self.X[i], self.A[i])

    def _propagate_at(self, i):
        self.X[i] = self._eval_at(i)
        self.A[i << 1] = self.A_f(self.A[i << 1], self.A[i])
        self.A[i << 1 | 1] = self.A_f(self.A[i << 1 | 1], self.A[i])
        self.A[i] = self.A_unit

    def _propagate_above(self, i):
        H = i.bit_length() - 1
        for h in range(H, 0, -1):
            self._propagate_at(i >> h)

    def _recalc_above(self, i):
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self._eval_at(i << 1), self._eval_at(i << 1 | 1))

    #i番目の値をxに変更する
    def set_val(self, i, x):
        i += self.N
        self._propagate_above(i)
        self.X[i] = x
        self.A[i] = self.A_unit
        self._recalc_above(i)

    #LからR-1までの値の積を取る
    def fold(self, L, R):
        L += self.N
        R += self.N
        self._propagate_above(L // (L & -L))
        self._propagate_above(R // (R & -R) - 1)
        vL = self.X_unit
        vR = self.X_unit
        while L < R:
            if L & 1:
                vL = self.X_f(vL, self._eval_at(L))
                L += 1
            if R & 1:
                R -= 1
                vR = self.X_f(self._eval_at(R), vR)
            L >>= 1
            R >>= 1
        return self.X_f(vL, vR)

    #LからR-1までの値にxを作用させる
    def operate_range(self, L, R, x):
        L += self.N
        R += self.N
        L0 = L // (L & -L)
        R0 = R // (R & -R) - 1
        self._propagate_above(L0)
        self._propagate_above(R0)
        while L < R:
            if L & 1:
                self.A[L] = self.A_f(self.A[L], x)
                L += 1
            if R & 1:
                R -= 1
                self.A[R] = self.A_f(self.A[R], x)
            L >>= 1
            R >>= 1
        self._recalc_above(L0)
        self._recalc_above(R0)

#累積和
import itertools
list(itertools.accumulate(l))

#BIT(Binary Indexed Tree, Fenwick Treeとも, 添え字が0から始まる形で管理していることに注意)
class BIT:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n
    def add(self, p, x):
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p
    #合計にはrを含まない
    def sum(self, l, r):
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)
    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s
    #pの位置をxという値にセット
    def set(self, p, x):
        self.add(p, -self.sum(p, p+1) + x)

#Dijkstra
from heapq import heappop,heappush
def Dijkstra(G,s):
  done=[False]*len(G)
  inf=10**20
  C=[inf]*len(G)
  C[s]=0
  h=[]
  heappush(h,(0,s))
  while h:
    x,y=heappop(h)
    if done[y]:
      continue
    done[y]=True
    for v in G[y]:
      if C[v[1]]>C[y]+v[0]:
        C[v[1]]=C[y]+v[0]
        heappush(h,(C[v[1]],v[1]))
  return C

#Warshall-Floyd
# cost[i][j]: 頂点v_iから頂点v_jへ到達するための辺コストの和
def WF(cost):
    for k in range(len(cost)):
        for i in range(len(cost)):
            for j in range(len(cost)):
                if cost[i][k]!=INF and cost[k][j]!=INF:
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    return cost

#オイラーツアー(https://maspypy.com/euler-tour-%E3%81%AE%E3%81%8A%E5%8B%89%E5%BC%B7#toc4)
def EulerTour(G, s):
    depth=[-1]*len(G)
    depth[s]=0
    done = [0]*len(G)
    Q = [~s, s] # 根をスタックに追加
    parent=[-1]*len(G)
    ET = []
    left,right=[-1]*len(G),[-1]*len(G)
    while Q:
        i = Q.pop()
        if i >= 0: # 行きがけの処理
            done[i] = 1
            ET.append(i)
            for a in G[i][::-1]:
                if done[a]: continue
                depth[a]=depth[i]+1
                parent[a]=i
                Q.append(~a) # 帰りがけの処理をスタックに追加
                Q.append(a) # 行きがけの処理をスタックに追加
        else: # 帰りがけの処理
            ET.append(i)
    for i in range(len(G)*2):
      if ET[i]>=0 and left[ET[i]]==-1: left[ET[i]]=i
      if ET[~i]<0 and right[~ET[~i]]==-1: right[~ET[~i]]=len(G)*2-i-1
    return ET, left, right, depth, parent #(right-left+1)//2がその頂点を含む部分木の大きさ

#LCA(最小共通祖先)
class LCA_Tree:
    def __init__(self, G, s):
        self.G=G
        self.s=s

        def EulerTour(G, s):
            depth=[-1]*len(G)
            depth[s]=0
            done = [0]*len(G)
            Q = [~s, s] # 根をスタックに追加
            parent=[-1]*len(G)
            ET = []
            left=[-1]*len(G)
            while Q:
                i = Q.pop()
                if i >= 0: # 行きがけの処理
                    done[i] = 1
                    if left[i]==-1: left[i]=len(ET)
                    ET.append(i)
                    for a in G[i][::-1]:
                        if done[a]: continue
                        depth[a]=depth[i]+1
                        parent[a]=i
                        Q.append(~a) # 帰りがけの処理をスタックに追加
                        Q.append(a) # 行きがけの処理をスタックに追加
                else: # 帰りがけの処理
                    ET.append(parent[~i])
            return ET[:-1], left, depth, parent
        self.S,self.F,self.depth,self.parent=EulerTour(self.G,0)
        self.INF = (len(self.G), None)
        self.M = 2*len(self.G)
        self.M0 = 2**(self.M-1).bit_length()
        self.data = [self.INF]*(2*self.M0)
        for i, v in enumerate(self.S):
            self.data[self.M0-1+i] = (self.depth[v], i)
        for i in range(self.M0-2, -1, -1):
            self.data[i] = min(self.data[2*i+1], self.data[2*i+2])

    #LCAの計算 (generatorで最小値を求める)
    def LCA(self, u, v):
        def _query(a, b):
            yield self.INF
            a += self.M0; b += self.M0
            while a < b:
                if b & 1:
                    b -= 1
                    yield self.data[b-1]
                if a & 1:
                    yield self.data[a-1]
                    a += 1
                a >>= 1; b >>= 1
        fu = self.F[u]; fv = self.F[v]
        if fu > fv:
            fu, fv = fv, fu
        return self.S[min(_query(fu, fv+1))[1]]

#強連結成分分解
#labels:強連結成分のラベル番号, lb_cnt:全強連結成分数, build:graphから強連結成分分解を実行, construct:強連結成分によるDAGと各成分の頂点リストのリストをこの順に抽出
class SCC:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.rev_graph = [[] for _ in range(n)]
        self.labels = [-1] * n
        self.lb_cnt = 0

    def add_edge(self, v, nxt_v):
        self.graph[v].append(nxt_v)
        self.rev_graph[nxt_v].append(v)

    def build(self):
        self.post_order = []
        self.used = [False] * self.n
        for v in range(self.n):
            if not self.used[v]:
                self._dfs(v)
        for v in reversed(self.post_order):
            if self.labels[v] == -1:
                self._rev_dfs(v)
                self.lb_cnt += 1

    def _dfs(self, v):
        stack = [v, 0]
        while stack:
            v, idx = stack[-2:]
            if not idx and self.used[v]:
                stack.pop()
                stack.pop()
            else:
                self.used[v] = True
                if idx < len(self.graph[v]):
                    stack[-1] += 1
                    stack.append(self.graph[v][idx])
                    stack.append(0)
                else:
                    stack.pop()
                    self.post_order.append(stack.pop())

    def _rev_dfs(self, v):
        stack = [v]
        self.labels[v] = self.lb_cnt
        while stack:
            v = stack.pop()
            for nxt_v in self.rev_graph[v]:
                if self.labels[nxt_v] != -1:
                    continue
                stack.append(nxt_v)
                self.labels[nxt_v] = self.lb_cnt

    def construct(self):
        self.dag = [[] for i in range(self.lb_cnt)]
        self.groups = [[] for i in range(self.lb_cnt)]
        for v, lb in enumerate(self.labels):
            for nxt_v in self.graph[v]:
                nxt_lb = self.labels[nxt_v]
                if lb == nxt_lb:
                    continue
                self.dag[lb].append(nxt_lb)
            self.groups[lb].append(v)
        return self.dag, self.groups

#popcount
def Popcount(n):
    c = (n & 0x5555555555555555) + ((n>>1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c>>2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c>>4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c>>8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c>>16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c>>32) & 0x00000000ffffffff)
    return c

#拡張ユークリッド ax+by=gcd(a,b)となるようなx,yを求める。同時にgcdも求める
#aとbが互いに素な時、xはmod bにおいてのaの逆元
def ExtGCD(a, b):
    if b:
        g, y, x = ExtGCD(b, a % b)
        y -= (a // b)*x
        return g, x, y
    return a, 1, 0

#mが素数と限らない場合にmod.mに置けるaの逆元（aとmが互いに素であることが必要十分条件）を求める関数
def Inv(a,m):
    return ExtGCD(a,m)[1]%m

#0から100万までの逆元を全て求める方法
MAX = 10**6+10
MOD = 998244353
inv = [0]*MAX
inv[1] = 1
 
for i in range(2, MAX):
    inv[i] = MOD-inv[MOD%i]*(MOD//i)%MOD

# 中国剰余定理。以下を満たすxを求める
# x≡b1 (mod.m1)
# x≡b2 (mod.m2)
import math
def Ch_Rem(b1,b2,m1,m2):
    g,p,q=ExtGCD(m1,m2)
    d=math.gcd(m1,m2)
    lcm=m1*m2//d
    return (b1+m1//d*(b2-b1)*p)%lcm

# 円同士の交点 円1: 中心(x1,y1) 半径r1 と 円2: 中心(x2,y2) 半径r2 の2つの円の交点
def CirclesCrossPoints(x1, y1, r1, x2, y2, r2):
    eps=10**(-6)
    r=((x1-x2)**2+(y1-y2)**2)**.5
    if r<eps or r+eps>r1+r2 or r1+eps>r+r2 or r2+eps>r+r1:
        return ()
    else:
        rr0 = (x2 - x1)**2 + (y2 - y1)**2
        xd = x2 - x1
        yd = y2 - y1
        rr1 = r1**2; rr2 = r2**2
        cv = (rr0 + rr1 - rr2)
        sv = (4*rr0*rr1 - cv**2)**.5
        return (
            (x1 + (cv*xd - sv*yd)/(2.*rr0), y1 + (cv*yd + sv*xd)/(2.*rr0)),
            (x1 + (cv*xd + sv*yd)/(2.*rr0), y1 + (cv*yd - sv*xd)/(2.*rr0)),
        )

# 頂点から円への接点 中心 (x1,y1) 半径 r1 に対する、点 (x2,y2) から引いた接線がなす接点
def circle_tangent_points(x1, y1, r1, x2, y2):
    dd = (x1 - x2)**2 + (y1 - y2)**2
    r2 = (dd - r1**2)**.5
    return circles_cross_points(x1, y1, r1, x2, y2, r2)

#円の外心を求める
def Gaishin(x1,y1,x2,y2,x3,y3):
    eps=10**(-6)
    if abs((x2-x1)*(y3-y2)-(x3-x2)*(y2-y1))<eps:
      return (max(x1,x2,x3)-min(x1,x2,x3))/2, (max(y1,y2,y3)-min(y1,y2,y3))/2, 0
    py = ((x3 - x1) * (x1**2 + y1**2 - x2**2 - y2**2) - (x2 - x1) * (x1**2 + y1**2 - x3**2- y3**2)) / (2 * (x3 - x1)*(y1 - y2) - 2 * (x2 - x1) * (y1 - y3))
    if x2 == x1:
        px = (2 * (y1 - y3) * py - x1**2 - y1**2 + x3**2 + y3**2) / (2 * (x3 - x1))
    else:
        px = (2 * (y1 - y2) * py - x1**2 - y1**2 + x2**2 + y2**2) / (2 * (x2 - x1))
    r = ((px - x1)**2+(py - y1)**2)**.5
    return px,py,r

#高速フーリエ変換による畳み込み 詳しくはmaspyさんのページhttps://maspypy.com/%E6%95%B0%E5%AD%A6%E3%83%BBnumpy-%E9%AB%98%E9%80%9F%E3%83%95%E3%83%BC%E3%83%AA%E3%82%A8%E5%A4%89%E6%8F%9Bfft%E3%81%AB%E3%82%88%E3%82%8B%E7%95%B3%E3%81%BF%E8%BE%BC%E3%81%BF
# (1 + 2x + 3x^2)(4 + 5x + 6x^2) = 4 + 13x + 28x^2 + 27x^3 + 18x^4
# f = np.array([1, 2, 3], np.int64)
# g = np.array([4, 5, 6], np.int64)
# h = convolve(f, g)
#print(h)[ 4 13 28 27 18]
def Convolve(f, g):
  fft_len = 1
  while 2 * fft_len < len(f) + len(g) - 1:
      fft_len *= 2
  fft_len *= 2
  Ff = np.fft.rfft(f, fft_len)
  Fg = np.fft.rfft(g, fft_len)
  Fh = Ff * Fg
  h = np.fft.irfft(Fh, fft_len)
  h = np.rint(h).astype(np.int64)
  return h[:len(f) + len(g) - 1]

#平衡二分木 nは追加する要素の数字が2**n以下になるような数字として設定。それなりに大きくても構築はO(1)なので遅くはならない。
class BalancingTree:
    def __init__(self, n):
        self.N = n
        self.root = self.node(1<<n, 1<<n)

    def append(self, v):# v を追加（その時点で v はない前提）
        v += 1
        nd = self.root
        while True:
            if v == nd.value:
                # v がすでに存在する場合に何か処理が必要ならここに書く
                return 0
            else:
                mi, ma = min(v, nd.value), max(v, nd.value)
                if mi < nd.pivot:
                    nd.value = ma
                    if nd.left:
                        nd = nd.left
                        v = mi
                    else:
                        p = nd.pivot
                        nd.left = self.node(mi, p - (p&-p)//2)
                        break
                else:
                    nd.value = mi
                    if nd.right:
                        nd = nd.right
                        v = ma
                    else:
                        p = nd.pivot
                        nd.right = self.node(ma, p + (p&-p)//2)
                        break

    def leftmost(self, nd):
        if nd.left: return self.leftmost(nd.left)
        return nd

    def rightmost(self, nd):
        if nd.right: return self.rightmost(nd.right)
        return nd

    def find_l(self, v): # vより真に小さいやつの中での最大値（なければ-1）
        v += 1
        nd = self.root
        prev = 0
        if nd.value < v: prev = nd.value
        while True:
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                prev = nd.value
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    def find_r(self, v): # vより真に大きいやつの中での最小値（なければRoot）
        v += 1
        nd = self.root
        prev = 0
        if nd.value > v: prev = nd.value
        while True:
            if v < nd.value:
                prev = nd.value
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    @property
    def max(self):
        return self.find_l((1<<self.N)-1)

    @property
    def min(self):
        return self.find_r(-1)

    def delete(self, v, nd = None, prev = None): # 値がvのノードがあれば削除（なければ何もしない）
        v += 1
        if not nd: nd = self.root
        if not prev: prev = nd
        while v != nd.value:
            prev = nd
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    #####
                    return
            else:
                if nd.right:
                    nd = nd.right
                else:
                    #####
                    return
        if (not nd.left) and (not nd.right):
            if not prev.left:
                prev.right = None
            elif not prev.right:
                prev.left = None
            else:
                if nd.pivot == prev.left.pivot:
                    prev.left = None
                else:
                    prev.right = None

        elif nd.right:
            # print("type A", v)
            nd.value = self.leftmost(nd.right).value
            self.delete(nd.value - 1, nd.right, nd)    
        else:
            # print("type B", v)
            nd.value = self.rightmost(nd.left).value
            self.delete(nd.value - 1, nd.left, nd)

    def __contains__(self, v: int) -> bool:
        return self.find_r(v - 1) == v

    class node:
        def __init__(self, v, p):
            self.value = v
            self.pivot = p
            self.left = None
            self.right = None

    def debug(self):
        def debug_info(nd_):
            return (nd_.value - 1, nd_.pivot - 1, nd_.left.value - 1 if nd_.left else -1, nd_.right.value - 1 if nd_.right else -1)

        def debug_node(nd):
            re = []
            if nd.left:
                re += debug_node(nd.left)
            if nd.value: re.append(debug_info(nd))
            if nd.right:
                re += debug_node(nd.right)
            return re
        print("Debug - root =", self.root.value - 1, debug_node(self.root)[:50])

    def debug_list(self):
        def debug_node(nd):
            re = []
            if nd.left:
                re += debug_node(nd.left)
            if nd.value: re.append(nd.value - 1)
            if nd.right:
                re += debug_node(nd.right)
            return re
        return debug_node(self.root)[:-1]

#LIS(最長増加部分列の長さと具体的な最長増加部分列を求める)
from bisect import bisect_left
def LIS(A: list):
    L = [A[0]]
    ID=[0]*len(A)
    for i in range(1,len(A)):
        if A[i] > L[-1]:
            L.append(A[i])
            ID[i]=len(L)-1
        else:
            tmp=bisect_left(L, A[i])
            L[tmp] = A[i]
            ID[i]=tmp
    L2=[]
    L3=[]
    m=len(L)-1
    for i in range(len(A)-1,-1,-1):
        if ID[i]==m:
            L2.append(A[i])
            L3.append(i)
            m-=1
    return len(L), L2[::-1], L3[::-1] #それぞれ最長増加部分列の長さ、復元した部分列、そのインデックス

#WLIS(広義の最長増加部分列の長さと具体的な広義最長増加部分列を求める)
from bisect import bisect_right
def WLIS(A: list):
    L = [A[0]]
    ID=[0]*len(A)
    for i in range(1,len(A)):
      if A[i] >= L[-1]:
        L.append(A[i])
        ID[i]=len(L)-1
      else:
        tmp=bisect_right(L, A[i])
        L[tmp] = A[i]
        ID[i]=tmp
    L2=[]
    L3=[]
    m=len(L)-1
    for i in range(len(A)-1,-1,-1):
      if ID[i]==m:
        L2.append(A[i])
        L3.append(i)
        m-=1
    return len(L), L2[::-1], L3[::-1]

#Kruskal法 max_vに頂点数,edgesに辺(重み、結んでいる２つの頂点（順不同）で入れる)
class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * n
  def find(self, x):
    if self.parents[x] < 0:
      return x
    else:
      self.parents[x] = self.find(self.parents[x])
      return self.parents[x]
  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if x == y:
      return
    if self.parents[x] > self.parents[y]:
       x, y = y, x
    self.parents[x] += self.parents[y]
    self.parents[y] = x
  def size(self, x):
    return -self.parents[self.find(x)]
  def same(self, x, y):
    return self.find(x) == self.find(y)
  def members(self, x):
    root = self.find(x)
    return [i for i in range(self.n) if self.find(i) == root]
  def roots(self):
    return [i for i, x in enumerate(self.parents) if x < 0]
  def group_count(self):
    return len(self.roots())
  def all_group_members(self):
    return {r: self.members(r) for r in self.roots()}
  def __str__(self):
    return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
def Kruskal(G):
  edges=set()
  for i in range(len(G)):
    for j in range(len(G[i])):
      c,k=G[i][j]
      l,m=min(i,k),max(i,k)
      edges.add((c,l,m))
  edges=list(edges)
  edges.sort()
  uf = UnionFind(len(G))
  mst = [] #最小全域木の辺すべて
  weight=0 #最小全域木の重さ
  for edge in edges:
    if not uf.same(edge[1], edge[2]):
      uf.union(edge[1], edge[2])
      mst.append(edge)
      weight+=edge[0]
  return mst,weight

#Prim法
from heapq import heappop,heappush
def Prim(G):
  N=len(G)
  m=set()
  m.add(0)
  mst = [] #最小全域木の辺すべて
  weight=0 #最小全域木の重さ
  h=[]
  for c,v in G[0]:
    if v not in m:
      heappush(h,(c,0,v))
  while len(h)>0:
    c,u,v=heappop(h)
    if v not in m:
      mst.append((c,u,v))
      weight+=c
      m.add(v)
      for c2,v2 in G[v]:
        if v2 not in m:
          heappush(h,(c2,v,v2))
  return mst,weight

#DFS
def dfs(G,r=0):
    used=[False]*len(G)
    parent=[-1]*len(G)
    st=[]
    st.append(r)
    while st:
        x=st.pop()
        if used[x]==True:
            continue
        used[x]=True
        for v in G[x]:
            if v==parent[x]:
                continue
            parent[v]=x
            st.append(v)
    return parent

#BFS
from collections import deque
def bfs(G,s):
  inf=10**30
  D=[inf]*len(G)
  D[s]=0
  dq=deque()
  dq.append(s)
  while dq:
    x=dq.popleft()
    for y in G[x]:
      if D[y]>D[x]+1:
        D[y]=D[x]+1
        dq.append(y)
  return D

# 重心分解
def cent_decomp(G,i):
  D,parent,used=bfs(G,i)
  size={key:1 for key in used}
  stack=[(i,0)]
  while stack:
    x,d=stack.pop()
    if d==0:
      for v in G[x]:
        if D[v]>D[x]:
          stack.append((v,1))
          stack.append((v,0))
    else:
      size[parent[x]]+=size[x]
  res=[]
  for i in used:
    tmp=0
    if len(used)-size[i]>len(used)//2: tmp=1
    for v in G[i]:
      if D[v]>D[i] and size[v]>len(used)//2: tmp=1
    if tmp==0: res.append(i)
  return res

#01BFS Gは隣接頂点リストで、(隣接頂点,重み(0or1))が入っている
from collections import deque
def bfs01(G,s):
  inf=10**20
  dist = [inf]*len(G)
  dist[s] = 0
  que = deque()
  que.append(s)
  while que:
    i = que.popleft()
    for j, c in G[i]:
        d = dist[i] + c
        if d < dist[j]:
            dist[j] = d
            if c == 1:
                que.append(j)
            else:
                que.appendleft(j)
  return dist

# 複数の区間が与えられた時の和集合(Xは区間のリストのリスト⇨例えばX=[[1,3],[10,12],[2,8]]なら[[1,8],[10,12]]が返る。1以上3以下か10以上12以下か2以上8以下の区間は1以上8以下か10以上12以下として表せる)
def Union(X):
    tmp=[]
    ans=[]
    for l,r in X:
        tmp.append([l,1])
        tmp.append([r+1,-1])
    tmp.sort()
    i=0
    l=tmp[0][0]
    flag=tmp[0][1]
    while i<len(tmp):
        if i<len(tmp)-1:
            while i<len(tmp)-1 and tmp[i+1][0]==tmp[i][0]:
                flag+=tmp[i+1][1]
                i+=1
        if i<len(tmp):
            if flag==0:
                ans.append([l,tmp[i][0]-1])
                if i<len(tmp)-1:
                    l=tmp[i+1][0]
            if i<len(tmp)-1:
                flag+=tmp[i+1][1]
        i+=1
    size=0
    for x,y in ans:
        size+=y-x+1
    return ans,size

#Combination
F=[1]
for i in range(N):
    F.append(F[-1]*(i+1)%mod)
I=[pow(F[-1],mod-2,mod)]
for i in range(N):
    I.append(I[-1]*(N-i)%mod)
I=I[::-1]

#Combination(modが素数ではなく、Nが小さくて全部求めておけば良いとき)
#C[id(m,n)]でmCnが得られる
def id(m,n):
  return m*(m+1)//2+n
C=[1]
for i in range(N):
  C.append(1)
  for j in range(i):
    C.append((C[i*(i+1)//2+j]+C[i*(i+1)//2+j+1])%M)
  C.append(1)

#lucasの定理により任意の整数Mに対しmod Mで二項係数を求めるクラス
#BC=BinomiaCoeeficien(M)で定義した後BC(n,k)がnCkを返すようになる。
class BinomialCoefficient:
    def __init__(self, mod):
        self.mod = mod
        self.prime = self.prime_factorize(mod)
        self.facs = []
        self.invs = []
        self.pows = []
        self.factinvs = []
        for p, c in self.prime:
            pc = pow(p, c)
            fac = [1] * pc
            inv = [1] * pc
            for i in range(1, pc):
                k = i
                if(i % p == 0):
                    k = 1
                fac[i] = fac[i - 1] * k % pc
            inv[-1] = fac[-1]
            for i in range(1, pc)[::-1]:
                k = i
                if(i % p == 0):
                    k = 1
                inv[i - 1] = inv[i] * k % pc
            self.facs.append(fac)
            self.invs.append(inv)
            pw = [1]
            while(pw[-1] * p != pc):
                pw.append(pw[-1] * p)
            self.pows.append(pw)

    def prime_factorize(self, n):
        prime = []
        f = 2
        while(f * f <= n):
            if(n % f == 0):
                n //= f
                cnt = 1
                while(n % f == 0):
                    n //= f
                    cnt += 1
                prime.append((f, cnt))
            f += 1
        if(n != 1):
            prime.append((n, 1))
        return prime

    def crt(self, rm):
        r0 = 0
        m0 = 1
        for a, b in rm:
            r1 = a % b
            m1 = b
            if(m0 < m1):
                r0, r1, m0, m1 = r1, r0, m1, m0
            if(m0 % m1 == 0):
                if(r0 % m1 != r1):
                    return 0, 0
                continue
            g, im = self.inv_gcd(m0, m1)
            u1 = m1 // g
            if((r1 - r0) % g):
                return 0, 0
            x = (r1 - r0) // g * im % u1
            r0 += x * m0
            m0 *= u1
            if(r0 < 0):
                r0 += m0
        return r0, m0

    def inv_gcd(self, n, m):
        n %= m
        if(n == 0):
            return m, 0
        s, t, m0, m1 = m, n, 0, 1
        while(t):
            u = s // t
            s -= t * u
            m0 -= m1 * u
            m0, m1, s, t = m1, m0, t, s
        if(m0 < 0):
            m0 += m // s
        return s, m0

    def inv_mod(self, n, m):
        g, im = self.inv_gcd(n, m)
        return im

    def calc_e(self, n, k, r, p):
        e = 0
        while(n):
            n //= p
            e += n
        while(k):
            k //= p
            e -= k
        while(r):
            r //= p
            e -= r
        return e

    def lucas(self, n, k, p, c, i):
        pw = self.pows[i]
        fac = self.facs[i]
        inv = self.invs[i]
        r = n - k
        pc = pow(p, c)
        e = self.calc_e(n, k, r, p)
        if(e >= len(pw)):
            return 0
        ret = pw[e]
        if((p != 2 or c < 3) and (self.calc_e(n // pw[-1], k // pw[-1], r // pw[-1], p) & 1)):
            ret *= -1
        while(n):
            ret *= fac[n % pc] * inv[k % pc] * inv[r % pc] % pc
            ret %= pc
            n //= p
            k //= p
            r //= p
        return ret

    def __call__(self, n, k):
        if(k < 0 or k > n):
            return 0
        if(k == 0 or k == n):
            return 1
        rm = [(self.lucas(n, k, p, c, i), pow(p, c)) for i, (p, c) in enumerate(self.prime)]
        ret, _ = self.crt(rm)
        return ret

#行列掃き出し法(Aはリスト、Nは桁数（Aのサイズではない）で、Aの要素を2進数表示したときに上の桁から掃き出しでまとめていく関数)
#A=[2,3]であれば、2進表示で10, 11だが、10は残して2の位の1が被っている11については10とxorを取って01に変更する。
def elimination(A,N=60):
  res=[]
  for i in reversed(range(N)):
    f=0
    for j in range(len(A)):
      if (A[j]>>i)&1==1:
        if f==0:
          x=A[j]
          t=j
          f=1
        else:
          A[j]^=x
    if f==1:
      res.append(x)
      A.pop(t)
    else:
      res.append(0)
  return res

#z algorithm
def z_algorithm(s):
    N = len(s)
    Z_alg = [0]*N

    Z_alg[0] = N
    i = 1
    j = 0
    while i < N:
        while i+j < N and s[j] == s[i+j]:
            j += 1
        Z_alg[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i+k < N and k + Z_alg[k]<j:
            Z_alg[i+k] = Z_alg[k]
            k += 1
        i += k
        j -= k
    return Z_alg

#10進数をn進数にする関数→リスト形式で、左から１の位、１０の位、という順番で数字が入る。
def Base_10_to_n(X, n):
  res=[]
  d=1
  while pow(n,d)<=X: d+=1
  for i in range(d):
    res.append(X//pow(n,d-1-i))
    X%=pow(n,d-1-i)
  return res[::-1]

#Topological Sort DAGでない入力でも良いが、その場合は-1が出力される Gは行先を入れたグラフ
from heapq import heappop,heappush
def TopologicalSort(G):
  G2=[set() for _ in range(len(G))]
  for i in range(len(G)):
    for v in G[i]:
      G2[v].add(i)
  res=[]
  h=[]
  for i in range(len(G)):
    if len(G2[i])==0:
      heappush(h,i)
  while len(h):
    x=heappop(h)
    res.append(x)
    for y in G[x]:
      G2[y].remove(x)
      if len(G2[y])==0:
        heappush(h,y)
  if len(res)==len(G):
    return res
  else:
    return -1

#サイクルの検出(Topological SortしてDAGじゃなかった場合、rから始まるサイクルを構成できる)
def dfs(G,r=0):
    used=[False]*len(G) #行きがけ
    finished=[False]*len(G) #帰りがけ
    parent=[-1]*len(G)
    st=[]
    st.append([r,1])
    st.append([r,0])
    cycle=[]
    while st:
        x,y=st.pop()
        if y==0:
            cycle.append(x)
            used[x]=True
            for v in G[x]:
                if used[v]==True and finished[v]==False:
                    return 0,cycle #サイクルありの場合
                parent[v]=x
                st.append([v,1])
                st.append([v,0])
        else:
            cycle.pop()
            finished[x]=True
    return None

#multiset
import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List
T = TypeVar('T')
class SortedMultiset(Generic[T]):
  BUCKET_RATIO = 50
  REBUILD_RATIO = 170
 
  def _build(self, a=None) -> None:
      "Evenly divide `a` into buckets."
      if a is None: a = list(self)
      size = self.size = len(a)
      bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
      self.a = [a[size * i // bucket_size : size * (i + 1) // bucket_size] for i in range(bucket_size)]
 
  def __init__(self, a: Iterable[T] = []) -> None:
      "Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"
      a = list(a)
      if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
          a = sorted(a)
      self._build(a)
 
  def __iter__(self) -> Iterator[T]:
      for i in self.a:
          for j in i: yield j
 
  def __reversed__(self) -> Iterator[T]:
      for i in reversed(self.a):
          for j in reversed(i): yield j
 
  def __len__(self) -> int:
      return self.size
 
  def __repr__(self) -> str:
      return "SortedMultiset" + str(self.a)
 
  def __str__(self) -> str:
      s = str(list(self))
      return "{" + s[1 : len(s) - 1] + "}"
 
  def _find_bucket(self, x: T) -> List[T]:
      "Find the bucket which should contain x. self must not be empty."
      for a in self.a:
          if x <= a[-1]: return a
      return a
 
  def __contains__(self, x: T) -> bool:
      if self.size == 0: return False
      a = self._find_bucket(x)
      i = bisect_left(a, x)
      return i != len(a) and a[i] == x
 
  def count(self, x: T) -> int:
      "Count the number of x."
      return self.index_right(x) - self.index(x)
 
  def add(self, x: T) -> None:
      "Add an element. / O(√N)"
      if self.size == 0:
          self.a = [[x]]
          self.size = 1
          return
      a = self._find_bucket(x)
      insort(a, x)
      self.size += 1
      if len(a) > len(self.a) * self.REBUILD_RATIO:
          self._build()
 
  def discard(self, x: T) -> bool:
      "Remove an element and return True if removed. / O(√N)"
      if self.size == 0: return False
      a = self._find_bucket(x)
      i = bisect_left(a, x)
      if i == len(a) or a[i] != x: return False
      a.pop(i)
      self.size -= 1
      if len(a) == 0: self._build()
      return True
 
  def lt(self, x: T) -> Union[T, None]:
      "Find the largest element < x, or None if it doesn't exist."
      for a in reversed(self.a):
          if a[0] < x:
              return a[bisect_left(a, x) - 1]
 
  def le(self, x: T) -> Union[T, None]:
      "Find the largest element <= x, or None if it doesn't exist."
      for a in reversed(self.a):
          if a[0] <= x:
              return a[bisect_right(a, x) - 1]
 
  def gt(self, x: T) -> Union[T, None]:
      "Find the smallest element > x, or None if it doesn't exist."
      for a in self.a:
          if a[-1] > x:
              return a[bisect_right(a, x)]
 
  def ge(self, x: T) -> Union[T, None]:
      "Find the smallest element >= x, or None if it doesn't exist."
      for a in self.a:
          if a[-1] >= x:
              return a[bisect_left(a, x)]
 
  def __getitem__(self, x: int) -> T:
      "Return the x-th element, or IndexError if it doesn't exist."
      if x < 0: x += self.size
      if x < 0: raise IndexError
      for a in self.a:
          if x < len(a): return a[x]
          x -= len(a)
      raise IndexError
 
  def index(self, x: T) -> int:
      "Count the number of elements < x."
      ans = 0
      for a in self.a:
          if a[-1] >= x:
              return ans + bisect_left(a, x)
          ans += len(a)
      return ans
 
  def index_right(self, x: T) -> int:
      "Count the number of elements <= x."
      ans = 0
      for a in self.a:
          if a[-1] > x:
              return ans + bisect_right(a, x)
          ans += len(a)
      return ans

#BellmanFord
def BellmanFord(G,s=0):
    inf=10**20
    D=[inf]*len(G)
    D[s]=0
    for i in range(len(G)-1):
      for j in range(len(G)):
        for c,v in G[j]:
          if D[j]+c<D[v]:
            D[v]=D[j]+c
    cycle=[0]*len(G)
    for j in range(len(G)):
      for c,v in G[j]:
        if D[j]+c<D[v]: cycle[v]=1
    for i in range(len(G)-1):
      for j in range(len(G)):
        if cycle[j]==1:
          for c,v in G[j]:
            cycle[v]=1
    for i in range(len(G)):
      if cycle[i]==1: D[i]='-inf'
    return D

# Ford-Fulkerson algorithm 計算量は最悪でO(F|E|) Fは最大フロー
class FordFulkerson:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]
 
    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)
 
    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)
 
    def dfs(self, v, t, f):
        if v == t:
            return f
        used = self.used
        used[v] = 1
        for e in self.G[v]:
            w, cap, rev = e
            if cap and not used[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0
 
    def flow(self, s, t):
        flow = 0
        f = INF = 10**9 + 7
        N = self.N 
        while f:
            self.used = [0]*N
            f = self.dfs(s, t, INF)
            flow += f
        return flow

# Dinic's algorithm 計算量V^2E
from collections import deque
class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None]*self.N
        deq = deque([s])
        level[s] = 0
        G = self.G
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10**9 + 7
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow

# 全方位木DP　参考提出コードhttps://atcoder.jp/contests/abc222/submissions/33273074
from collections import deque
#0を根として、Pに各頂点の親を格納。
P = [-1] * N
Q = deque([0])
R = []
while Q:
  i = deque.popleft(Q)
  R.append(i)
  for a in G[i]:
    if a != P[i]:
      P[a] = i
      G[a].remove(i)
      deque.append(Q, a)
##### Settings
unit = xxxx
merge = lambda a, b: xxxxxx
## ↓ この2つは必ず対称的にする（じゃないとバグる）
adj_bu = lambda a, i, p: xxxxx
adj_td = lambda a, i, p: xxxxx
#####
adj_fin = lambda a, i: xxxxx
#####
ME = [unit] * N #子からの情報を集約した値
ans = [0] * N #親に伝搬する値
TD = [unit] * N #累積値を格納しておくリスト
#葉から値を集約して通常の木DPをやる部分
for i in R[1:][::-1]:
    p = P[i]
    ans[i] = adj_bu(ME[i], i, p)
    ME[p] = merge(ME[p], ans[i])
ans[R[0]] = adj_fin(ME[R[0]], R[0])
#親からの情報と子からの情報を統合して全方位木DPをやる部分
for i in R:
    ac = TD[i]
    for j in G[i]:
        TD[j] = ac #前から累積していった値をTDに格納
        ac = merge(ac, ans[j]) #acを前から累積した値に更新
    ac = unit #一度リセットして、後ろから累積していった値をacに入れる
    for j in G[i][::-1]:
        TD[j] = adj_td(merge(TD[j], ac), j, i) #TD[j]を親方向から伝搬させる値に更新（前から累積したTD[j]と後ろからの累積値acをマージ）
        ac = merge(ac, ans[j]) #acを後ろから累積した値に更新
        ans[j] = adj_fin(merge(ME[j], TD[j]), j) #親方向からの伝搬値TD[j]と子方向からの伝搬値ME[j]で最終的な答えans[j]を更新
print(*ans, sep = "\n")

#分割数列挙 for x in partition_of_int(N):print(x)
def part_int_sub(n, k, a):
  if n == 0: yield a
  elif n == 1: yield a + [1]
  elif k == 1: yield a + [1] * n
  else:
    if n >= k:
      yield from part_int_sub(n-k, k, a+[k])
    yield from part_int_sub(n, k-1, a)

def partition_of_int(n):
  yield from part_int_sub(n, n, [])

#設定した比較関数でソート
from functools import cmp_to_key
def cmp(a, b):
    if a == b: return 0
    return -1 if a < b else 1
def cmpstr(a, b):
    return cmp(str(a), str(b))
xs = [4, 90, -9, 12, 42]
xs.sort(key=cmp_to_key(cmpstr))

from collections import Counter

# SA-IS (O(nlogn))
# s: 文字列
def sais(s):
    uniq = list(set(s))
    uniq.sort()
    return sais_rec(list(map({e: i+1 for i, e in enumerate(uniq)}.__getitem__, s)), len(uniq))
def sais_rec(lst, num):
    L = len(lst)
    if L < 2:
        return lst + [0]
    lst = lst + [0]
    L += 1
    res = [-1] * L
    t = [1] * L
    for i in range(L-2, -1, -1):
        t[i] = 1 if (lst[i] < lst[i+1] or (lst[i] == lst[i+1] and t[i+1])) else 0
    isLMS = [t[i-1] < t[i] for i in range(L)]
    LMS = [i for i in range(1, L) if t[i-1] < t[i]]
    LMSn = len(LMS)

    count = Counter(lst)
    tmp = 0
    cstart = [0]*(num+1)
    cend = [0]*(num+1)
    for key in range(num+1):
        cstart[key] = tmp
        cend[key] = tmp = tmp + count[key]

    cc_it = [iter(range(e-1, s-1, -1)) for s, e in zip(cstart, cend)]
    for e in reversed(LMS):
        res[next(cc_it[lst[e]])] = e

    cs_it = [iter(range(s, e)) for s, e in zip(cstart, cend)]
    ce_it = [iter(range(e-1, s-1, -1)) for s, e in zip(cstart, cend)]
    for e in res:
        if e > 0 and not t[e-1]:
            res[next(cs_it[lst[e-1]])] = e-1
    for e in reversed(res):
        if e > 0 and t[e-1]:
            res[next(ce_it[lst[e-1]])] = e-1

    name = 0; prev = -1
    pLMS = {}
    for e in res:
        if isLMS[e]:
            if prev == -1 or lst[e] != lst[prev]:
                name += 1; prev = e
            else:
                for i in range(1, L):
                    if lst[e+i] != lst[prev+i]:
                        name += 1; prev = e
                        break
                    if isLMS[e+i] or isLMS[prev+i]:
                        break
            pLMS[e] = name-1

    if name < LMSn:
        sublst = [pLMS[e] for e in LMS if e < L-1]
        ret = sais_rec(sublst, name-1)

        LMS = list(map(LMS.__getitem__, reversed(ret)))
    else:
        LMS = [e for e in reversed(res) if isLMS[e]]

    res = [-1] * L

    cc_it = [iter(range(e-1, s-1, -1)) for s, e in zip(cstart, cend)]
    for e in LMS:
        res[next(cc_it[lst[e]])] = e

    cs_it = [iter(range(s, e)) for s, e in zip(cstart, cend)]
    ce_it = [iter(range(e-1, s-1, -1)) for s, e in zip(cstart, cend)]

    for e in res:
        if e > 0 and not t[e-1]:
            res[next(cs_it[lst[e-1]])] = e-1
    for e in reversed(res):
        if e > 0 and t[e-1]:
            res[next(ce_it[lst[e-1]])] = e-1
    return res

# Longest Common Prefix
# (文字列s, 文字列長n, Suffix Array)を引数として与える
def LCP(s, n, sa):
    lcp = [-1]*(n+1)
    rank = [0]*(n+1)
    for i in range(n+1): rank[sa[i]] = i

    h = 0
    lcp[0] = 0
    for i in range(n):
        j = sa[rank[i] - 1]
        if h > 0: h -= 1
        while j+h < n and i+h < n and s[j+h]==s[i+h]:
            h += 1
        lcp[rank[i] - 1] = h
    return lcp

#スライド最小値
from collections import deque
def sliding_window(A,L):
  """
  A: 列のi番目の要素
  L: 最小値を調べる長さ
  """
  ans = []
  que = deque()
  for i, a in enumerate(A):
    while que and a <= que[-1][1]:
      que.pop()
    que.append((i, a))
    ans.append(que[0][1])
    if que and que[0][0] <= i+1-L:
      que.popleft()
  return ans[L-1:]

#行列累乗
class MatMul:
  def __init__(self, N, mod):
    self.N = N
    self.mod = mod
  def idx(self,i,j): return i*self.N+j
  def mult(self,A,B):
    res=[]
    for i in range(self.N):
      for j in range(self.N):
        res.append(sum([A[self.idx(i,k)]*B[self.idx(k,j)]%self.mod for k in range(self.N)])%self.mod)
    return res
  def pow_mat(self,A,n):
    tmp=[A]
    m=n
    while m>1:
      tmp.append(self.mult(tmp[-1],tmp[-1]))
      m//=2
    res=[0]*self.N**2
    for i in range(self.N):
      res[self.idx(i,i)]=1
    for i in range(len(tmp)):
      if (n>>i)&1==1:
        res=self.mult(res,tmp[i])
    return res
  def mat_vec(self,A,v):
    res=[0]*self.N
    for i in range(self.N):
      res[i]=sum([A[self.idx(i,j)]*v[j]%self.mod for j in range(self.N)])%self.mod
    return res
  
#Binary Trie
#この実装のmin_xorは一般的なTrieの変数とは異なるが、こういうこともできるという例（Trieに入っている２数のXORの最小値を求めている）
#その他実装が足りないので、必要に応じて追加する（https://kazuma8128.hatenablog.com/entry/2018/05/06/022654）
class BinaryTrie:
    class node:
        def __init__(self,val):
            self.left = None
            self.right = None
            self.cnt = 0
            self.min_xor = 1<<30
            self.val = val
 
    def __init__(self):
        self.B = 30
        self.root = self.node(1<<self.B)
        
 
    def append(self,val):
        pos = self.root
        stack = []
        for b in range(self.B)[::-1]:
            stack.append(pos) 
            if val>>b & 1:
                if pos.right is None:
                    pos.right = self.node(val)
                pos = pos.right
            else:
                if pos.left is None:
                    pos.left = self.node(val)
                pos = pos.left
 
        pos.cnt = 1
        pos.val = val
        pos.min_xor = 1<<self.B
        for pos in stack[::-1]:
            pos.cnt = 0
            if pos.left and pos.left.cnt:
                pos.cnt += pos.left.cnt
                pos.min_xor = min(pos.min_xor,pos.left.min_xor)
                pos.val = pos.left.val
            if pos.right and pos.right.cnt:
                pos.cnt += pos.right.cnt
                pos.min_xor = min(pos.min_xor,pos.right.min_xor)
                pos.val = pos.right.val
            if pos.left and pos.right and pos.left.cnt and pos.right.cnt:
                pos.min_xor = min(pos.min_xor,pos.left.val ^ pos.right.val)
    
    def remove(self,val):
        #print("remove",val)
        pos = self.root
        stack = []
        for b in range(self.B)[::-1]:
            stack.append(pos)
            if val>>b & 1:
                pos = pos.right
            else:
                pos = pos.left
        
        pos.cnt = 0
        pos.val = -1
        pos.min_xor = 1<<self.B
        for pos in stack[::-1]:
            pos.cnt = 0
            pos.min_xor = 1<<30
            if pos.left and pos.left.cnt:
                pos.cnt += pos.left.cnt
                pos.min_xor = min(pos.min_xor,pos.left.min_xor)
                pos.val = pos.left.val
            if pos.right and pos.right.cnt:
                pos.cnt += pos.right.cnt
                pos.min_xor = min(pos.min_xor,pos.right.min_xor)
                pos.val = pos.right.val
            if pos.left and pos.right and pos.left.cnt and pos.right.cnt:
                pos.min_xor = min(pos.min_xor,pos.left.val ^ pos.right.val)
            if pos.cnt == 0:
                pos.val = -1

def cartesian_tree(a, cmp=lambda x,y: x < y):
    n = len(a)
    parent = [-1] * n
    for i in range(1,n):
        p = i-1  # parent of i
        l = -1  # left child of i
        while p != -1 and cmp(a[i], a[p]):
            pp = parent[p]  # parent of parent of i
            if l != -1:
                parent[l] = p
            parent[p] = i
            l = p
            p = pp
        parent[i] = p
    return parent

#Merge Sort Tree
#参考：https://tjkendev.github.io/procon-library/python/range_query/merge-sort-tree.html
#data2関連を消せばカウントしかできなくなるが少し高速になる
from itertools import accumulate
from bisect import bisect_right
from heapq import merge
class MergeSortTree:
  def __init__(self, A):
    self.N = len(A)
    self.N0 = 2**(self.N-1).bit_length()
    self.data = [None]*(2*self.N0)
    self.data2 = [None]*(2*self.N0)
    for i, a in enumerate(A):
      self.data[self.N0-1+i] = [a]
      self.data2[self.N0-1+i] = [0, a]
    for i in range(self.N, self.N0):
      self.data[self.N0-1+i] = []
      self.data2[self.N0-1+i] = [0]
    for i in range(self.N0-2, -1, -1):
      *self.data[i], = merge(self.data[2*i+1], self.data[2*i+2])
      self.data2[i] = [0]+list(accumulate(self.data[i]))

  # count elements A_i s.t. A_i <= k for i in [l, r)
  def count_query(self,l, r, k):
      L = l + self.N0; R = r + self.N0
      s = 0
      while L < R:
        if R & 1:
          R -= 1
          s += bisect_right(self.data[R-1], k)
        if L & 1:
          s += bisect_right(self.data[L-1], k)
          L += 1
        L >>= 1; R >>= 1
      return s
  
  # sum of elements A_i s.t. A_i <= k for i in [l, r)
  def sum_query(self,l, r, k):
      L = l + self.N0; R = r + self.N0
      s = 0
      while L < R:
        if R & 1:
          R -= 1
          s += self.data2[R-1][bisect_right(self.data[R-1], k)]
        if L & 1:
          s += self.data2[L-1][bisect_right(self.data[L-1], k)]
          L += 1
        L >>= 1; R >>= 1
      return s

#2SAT
#https://github.com/shakayami/ACL-for-python/wiki/two-sat
def two_sat(n,clause):
    answer=[0]*n
    edges=[]
    N=2*n
    for s in clause:
        i,f,j,g=s
        edges.append((2*i+(0 if f else 1),2*j+(1 if g else 0)))
        edges.append((2*j+(0 if g else 1),2*i+(1 if f else 0)))
    M=len(edges)
    start=[0]*(N+1)
    elist=[0]*M
    for e in edges:
        start[e[0]+1]+=1
    for i in range(1,N+1):
        start[i]+=start[i-1]
    counter=start[:]
    for e in edges:
        elist[counter[e[0]]]=e[1]
        counter[e[0]]+=1
    visited=[]
    low=[0]*N
    Ord=[-1]*N
    ids=[0]*N
    NG=[0,0]
    def dfs(v):
        stack=[(v,-1,0),(v,-1,1)]
        while stack:
            v,bef,t=stack.pop()
            if t:
                if bef!=-1 and Ord[v]!=-1:
                    low[bef]=min(low[bef],Ord[v])
                    stack.pop()
                    continue
                low[v]=NG[0]
                Ord[v]=NG[0]
                NG[0]+=1
                visited.append(v)
                for i in range(start[v],start[v+1]):
                    to=elist[i]
                    if Ord[to]==-1:
                        stack.append((to,v,0))
                        stack.append((to,v,1))
                    else:
                        low[v]=min(low[v],Ord[to])
            else:
                if low[v]==Ord[v]:
                    while(True):
                        u=visited.pop()
                        Ord[u]=N
                        ids[u]=NG[1]
                        if u==v:
                            break
                    NG[1]+=1
                low[bef]=min(low[bef],low[v])
    for i in range(N):
        if Ord[i]==-1:
            dfs(i)
    for i in range(N):
        ids[i]=NG[1]-1-ids[i]
    for i in range(n):
        if ids[2*i]==ids[2*i+1]:
            return None
        answer[i]=(ids[2*i]<ids[2*i+1])
    return answer

#LowLink
# https://kntychance.hatenablog.jp/entry/2022/09/16/161858
# https://github.com/prd-xxx/gorichan_kyopro_library/tree/main/lowlink
class LowLink:
    def __init__(self,n,es):
        self.n = n
        self.es = es
        self.visited = [0] * n
        self.order = [0] * n
        self.low = [0] * n
        self.count = 0
        self.articulation_points = set()
        self.bridges = []
        self.dfs_parent = [-1] * n
        self.dfs_child = [[] for _ in range(n)]
        self.is_dfs_root = [0] * n
    def _dfs(self,rt):
        self.is_dfs_root[rt] = 1
        stack = [(-1,rt,0)]
        while stack:
            p,c,dir = stack.pop()
            if dir==0:
                if self.visited[c]: continue
                self.visited[c] = 1
                self.low[c] = self.order[c] = self.count
                self.count += 1
                if c != rt:
                    self.dfs_parent[c] = p
                    self.dfs_child[p].append(c)
                for to in self.es[c][::-1]:
                    if self.visited[to]:
                        if to != p:
                            self.low[c] = min(self.low[c], self.order[to])
                        continue
                    stack.append((c,to,1))
                    stack.append((c,to,0))
            else:
                if self.dfs_parent[c] != p: continue
                if c != self.dfs_parent[p]:
                    self.low[p] = min(self.low[p], self.low[c])
                if p != rt and self.order[p] <= self.low[c]:
                    self.articulation_points.add(p)
                if self.order[p] < self.low[c]:
                    self.bridges.append((p,c)) 
        if len(self.dfs_child[rt]) >= 2:
            self.articulation_points.add(rt)
    def build(self):
        self.component_num = 0
        for i in range(self.n):
            if self.visited[i]: continue
            self._dfs(i)
            self.component_num += 1

# 重心分解
class Centroid_decomposition:
    def __init__(self, N: int, G: list[int]):
        #頂点数N, 隣接リストGを渡す。重心分解を行う
        #order[c]: 重心分解後の部分木における、重心cのDFS到達順
        #          重心cの部分木は、orderが重心cよりも「大きい」BFSで移動可能な頂点
        #depth[c]: 重心分解後の部分木における、重心cの深さ
        #belong[c]: 重心分解後の部分木における、重心cの親となる重心(根の場合、-1)
        #           belong[c]を再帰的にたどることで、頂点iが属する重心を列挙できる
        self.N = N
        self.logN = N.bit_length()
        self.order = order = [-1] * N
        self.depth = depth = [-1] * N
        self.belong = belong = [-1] * N

        #部分木の大きさを前計算
        stack, size = [(0, -1)], [1] * N
        for now, back in stack:
            for nxt in G[now]:
                if nxt != back:
                    stack.append((nxt, now))
        while stack:
            now, back = stack.pop()
            if back != -1:
                size[back] += size[now]

        #重心分解を実行
        stack = [(0, -1, 0)]
        for c in range(N):
            now, back, d = stack.pop()

            #1. 重心を探す
            while True:
                for nxt in G[now]:
                    if order[nxt] == -1 and size[nxt] * 2 > size[now]:
                        size[now], size[nxt], now = size[now] - size[nxt], size[now], nxt
                        break
                else:  #forループが完走 = 頂点nowが重心の場合
                    break
            
            #2. 採番
            order[now], depth[now], belong[now] = c, d, back

            #3. 重心に隣接する頂点を再帰的に重心分解
            if size[now] > 1:
                for nxt in G[now]:
                    if order[nxt] == -1:
                        stack.append((nxt, now, d + 1))


    #頂点u, vをどちらも含む、最も小さい部分木の重心を返す
    def find(self, u: int, v: int):
        du, dv = self.depth[u], self.depth[v]
        for du in range(du - 1, dv - 1, -1):
            u = self.belong[u]
        for dv in range(dv - 1, du - 1, -1):
            v = self.belong[v]
        while u != v:
            u, v = self.belong[u], self.belong[v]
        return u

    #頂点vが属する重心木を、サイズの昇順に列挙する
    def get(self, v: int):
        vertices = []
        for d in range(self.depth[v], -1, -1):
            vertices.append(v)
            v = self.belong[v]
        return vertices

class AuxiliaryTree:
    def __init__(self, n, edge, root=0):
        self.n = n
        self.edge = edge
        self.eular = [-1] * (2 * n - 1)
        self.first = [-1] * n
        self.depth = [-1] * n
        self.lgs = [0] * (2 * n)
        for i in range(2, 2 * n):
            self.lgs[i] = self.lgs[i >> 1] + 1
        self.st = []
        self.G = [[] for i in range(n)]  # 構築結果

        self.dfs(root)
        self.construct_sparse_table()

    def dfs(self, root):
        stc = [root]
        self.depth[root] = 0
        num = 0
        while stc:
            v = stc.pop()
            if v >= 0:
                self.eular[num] = v
                self.first[v] = num
                num += 1
                for u in self.edge[v][::-1]:
                    if self.depth[u] == -1:
                        self.depth[u] = self.depth[v] + 1
                        stc.append(~v)
                        stc.append(u)
            else:
                self.eular[num] = ~v
                num += 1

    def construct_sparse_table(self):
        self.st.append(self.eular)
        sz = 1
        while 2 * sz <= 2 * self.n - 1:
            prev = self.st[-1]
            nxt = [0] * (2 * self.n - 2 * sz)
            for j in range(2 * self.n - 2 * sz):
                v = prev[j]
                u = prev[j + sz]
                if self.depth[v] <= self.depth[u]:
                    nxt[j] = v
                else:
                    nxt[j] = u
            self.st.append(nxt)
            sz *= 2

    def lca(self, u, v):
        x = self.first[u]
        y = self.first[v]
        # if x > y : x , y = y , x
        d = self.lgs[y - x + 1]
        return (
            self.st[d][x]
            if self.depth[self.st[d][x]] <= self.depth[self.st[d][y - (1 << d) + 1]]
            else self.st[d][y - (1 << d) + 1]
        )

    def query(self, vs):
        """
        vs: 仮想木の頂点
        self.G: 仮想木における子
        返り値: 仮想木の根
        """

        k = len(vs)
        if k == 0:
            return -1
        vs.sort(key=self.first.__getitem__)
        stc = [vs[0]]
        self.G[vs[0]] = []

        for i in range(k - 1):
            w = self.lca(vs[i], vs[i + 1])
            if w != vs[i]:
                last = stc.pop()
                while stc and self.depth[w] < self.depth[stc[-1]]:
                    self.G[stc[-1]].append(last)
                    last = stc.pop()

                if not stc or stc[-1] != w:
                    stc.append(w)
                    vs.append(w)
                    self.G[w] = [last]
                else:
                    self.G[w].append(last)
            stc.append(vs[i + 1])
            self.G[vs[i + 1]] = []

        for i in range(len(stc) - 1):
            self.G[stc[i]].append(stc[i + 1])

        return stc[0]