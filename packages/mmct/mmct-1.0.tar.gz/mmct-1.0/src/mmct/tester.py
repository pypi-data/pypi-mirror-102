import numpy as np
import random

from . import mc
from . import stat

class tester:

	n_obs = 1
	n_trials = 1000
	statistics = np.zeros(1)

	__old_ps = None

	def run_trials(self, probs):
		# First, generate a cumulative sum of the probabilities in ps
		cps = np.zeros(probs.size)
		cps[0] = probs[0]
		for i in range(1,probs.size):
			cps[i] = cps[i-1] + probs[i]

		# Generate n_trials samples from the underlying distribution of ps
		self.statistics = np.zeros(self.n_trials)
		for i in range(0,self.n_trials):

			# Each distribution need n_obs observations
			rs = np.zeros(self.n_obs)
			# Generate n_obs random numbers in [0,1)
			for j in range(0,self.n_obs):
				rs[j] = random.random()

			# Generate a multinomial draw from the probabilities in ps (using cps)
			m = mc.get_multinom(cps,rs)

			# Calculate test statistic
			self.statistics[i] = stat.multinomialLLR(m,probs)

		# Set __old_ps, so we know the state of the distribution for later
		self.__old_ps = probs.copy()


	def do_test(self, x, probs):

		if x.size != probs.size:
			raise ValueError('Input arrays must have the same number of elements')

		n = np.sum(x)

		# Check if a rerun of trials is necessary
		if not np.array_equal(self.__old_ps,probs) or n!=self.n_obs or self.n_trials!=self.statistics.size:

			# Set correct number of observations
			self.n_obs = n

			# Run trials
			self.run_trials(probs)

		# Calculate statistic of x
		x_stat = stat.multinomialLLR(x, probs)

		# Count number of trials with statistic smaller than x
		n_smaller = 0
		for s in self.statistics:
			if s <= x_stat:
				n_smaller += 1
		return n_smaller/self.statistics.size
