import numpy as np
import math
import pareto as pt


def MO_calculate(soln):
	"""
	Calculates objective vector [overtime, idletime, waiting time]
	:param soln: (ndarray) a solution
	:return: (ndarray) objective vector
	"""
	over_time_score = 0
	idle_time_score = 0
	waiting_time_score = 0
	alpha = 2.0  # multiplier for actual surgeries
	beta = 1.0  # multiplier for predicted surgeries

	# overtime
	last2hrs = soln[:, :, -8:]
	overtime_surg = last2hrs[last2hrs != 0]
	overtime_surg_type = [float(str(x)[1:2]) for x in overtime_surg]
	overtime_surg_type = np.array(overtime_surg_type)
	overtime_surg_type[overtime_surg_type == 1] *= alpha
	overtime_surg_type[overtime_surg_type == 2] *= beta
	over_time_score = sum(overtime_surg_type * 15) # in minutes

	# idletime
	first9hrs = soln[:, :, :-8]

	zero_count = np.count_nonzero(first9hrs == 0, axis=2)
	zero_count = np.sum(zero_count, axis=1)
	days_away = np.arange(start=1, stop=len(zero_count) + 1)
	days_away = np.power(0.9, days_away) # exponentially decaying function
	res = np.multiply(zero_count, days_away)
	idle_time_score = sum(res)

	# waiting time:
	inserted_surg = np.where((soln//100000>=20), 0, soln)
	inserted_surg = inserted_surg.reshape(len(inserted_surg), -1)
	inserted_surg[:, 1:] *= (np.diff(inserted_surg, axis=1) != 0)
	days_away = np.arange(start=1, stop=len(zero_count) + 1)
	inserted_surg = np.where((inserted_surg//100000==12),beta, inserted_surg)
	inserted_surg = np.where((inserted_surg//100000==11), alpha, inserted_surg)
	inserted_surg_t = inserted_surg.transpose()
	res_w = np.multiply(inserted_surg_t, days_away)
	res_w = res_w.flatten()
	waiting_time_score = sum(res_w)
	c = np.array(([over_time_score, idle_time_score, waiting_time_score]))
	return c


def calc_crowding_distance(F):
	"""
	Calculate crowding distance of each solution
	:param F: (list) scores of all solutions
	:return: (list) crowding distance of each solution
	"""
	infinity = 1e+14

	n_points = F.shape[0]
	n_obj = F.shape[1]

	if n_points <= 2:
		return np.full(n_points, infinity)
	else:

		# sort each column and get index
		I = np.argsort(F, axis=0, kind='mergesort')

		# now really sort the whole array
		F = F[I, np.arange(n_obj)]

		# get the distance to the last element in sorted list and replace zeros with actual values
		dist = np.concatenate([F, np.full((1, n_obj), np.inf)]) \
		       - np.concatenate([np.full((1, n_obj), -np.inf), F])

		index_dist_is_zero = np.where(dist == 0)

		dist_to_last = np.copy(dist)
		for i, j in zip(*index_dist_is_zero):
			dist_to_last[i, j] = dist_to_last[i - 1, j]

		dist_to_next = np.copy(dist)
		for i, j in reversed(list(zip(*index_dist_is_zero))):
			dist_to_next[i, j] = dist_to_next[i + 1, j]

		# normalize all the distances
		norm = np.max(F, axis=0) - np.min(F, axis=0)
		norm[norm == 0] = np.nan
		dist_to_last, dist_to_next = dist_to_last[:-1] / norm, dist_to_next[1:] / norm

		# if we divided by zero because all values in one columns are equal replace by none
		dist_to_last[np.isnan(dist_to_last)] = 0.0
		dist_to_next[np.isnan(dist_to_next)] = 0.0

		# sum up the distance to next and last and norm by objectives - also reorder from sorted list
		J = np.argsort(I, axis=0)
		crowding = np.sum(dist_to_last[J, np.arange(n_obj)] + dist_to_next[J, np.arange(n_obj)], axis=1) / n_obj

	# replace infinity with a large number
	crowding[np.isinf(crowding)] = infinity

	return crowding


def calculate_delta_S2(curr, perturb, T, lambdas_, pareto_scores): # scalarizing function
	"""
	Scalarizing function for UMOSA
	:param curr: (ndarray) current solution
	:param perturb: (ndarray) the neighbouring solution
	:param T: (float) current temperature
	:param lambdas_: (list) weight vectors
	:param pareto_scores: (list) of scores of solutions on the current pareto front
	:return: (float) probability of acceptance
	"""
	pareto_scores = np.array(pareto_scores)
	pareto_scores = np.delete(pareto_scores, -1, axis=1)
	max_overtime, max_idletime, max_waittime = pareto_scores.max(axis = 0)
	range_arr = np.array([max_overtime, max_idletime, max_waittime])
	lambdas_ = np.divide(lambdas_,range_arr)
	lambdas_ = lambdas_ / np.sum(lambdas_)
	s_curr = np.sum(np.multiply(curr, lambdas_))
	s_perturb = np.sum(np.multiply(perturb, lambdas_))
	delta_s = s_perturb - s_curr
	if delta_s < 0:
		return 1
	else:
		return np.exp(-delta_s/T)


