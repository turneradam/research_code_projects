#!/usr/bin/env python
from scipy import *
from scipy.linalg import eigh
import pylab

# setup
pylab.rc('font', size=8)
fig = pylab.figure(figsize=(3.25, 5))
data = loadtxt('fluor_opposite.dat')
dataMC = data - data.mean(0)

# scores
c = cov(dataMC, rowvar=False)
evals, evecs = eigh(c)
pos = argsort(evals)[::-1]
evecs = evecs[:,pos]
evals = evals[pos]
fracs = evals/sum(evals)
#PCs = dot(evecs.T, dataMC.T)
PC1, PC2, PC3, PC4 = dot(evecs.T, dataMC.T)
ax1 = fig.add_subplot(211)
ax1.plot(PC1, PC2, 'ko', ms=3)
ax1.axhline(0, color='k', ls='--', dashes=[1,1])
ax1.axvline(0, color='k', ls='--', dashes=[1,1])
ax1.set_title('scores')

# loadings
c = cov(dataMC.T, rowvar=False)
evals, evecs = eigh(c)
pos = argsort(evals)[::-1]
evecs = evecs[:,pos]
evals = evals[pos]
fracs = evals/sum(evals)
loadings = dot(evecs.T, data)
ax2 = fig.add_subplot(212)
ax2.plot(loadings[0], loadings[1], 'ko', ms=3)
ax2.set_title('loadings')

# pretty
for ax in [ax1, ax2]:
    ax.set_xlabel('PC1')
    ax.set_ylabel('PC2')

fig.set_tight_layout(True)
pylab.savefig('fluor.png')
