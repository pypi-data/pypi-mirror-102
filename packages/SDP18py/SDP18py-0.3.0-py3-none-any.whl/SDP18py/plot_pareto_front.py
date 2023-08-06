from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.tri as mtri
import pareto as pt
import copy


def plot_front(dp, pp):
	"""
	Plot pareto front with the dominated points (not implemented, requires too much memory to store all past points)

	:param dp: (list) dominated scores throughout the search
	:param pp: (list) pareto optimal scores
	"""
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	ax.scatter(dp[:,0],dp[:,1],dp[:,2])
	ax.scatter(pp[:,0],pp[:,1],pp[:,2],color='red')

	triang = mtri.Triangulation(pp[:, 0], pp[:, 1])
	ax.plot_trisurf(triang, pp[:, 2], color='red')
	plt.show()
	return


def plot_front_only(pp):
	"""
	Plot just the pareto front
	:param pp: (list) of pareto optimal scores
	:return:
	"""
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	ax.scatter(pp[:,0],pp[:,1],pp[:,2],color='blue')

	triang = mtri.Triangulation(pp[:, 0], pp[:, 1])
	ax.plot_trisurf(triang, pp[:, 2], color='blue')
	plt.show()
	return


def plot_front_multiple(pp_hco, pp_sa, pp_ts, pp_ga):
	"""
	Plot multiple pareto fronts together
	:param pp_hco: (list) pareto scores of MOSHCR
	:param pp_sa: (list) pareto scores of UMOSA
	:param pp_ts: (list) pareto scores of TAMOCO
	:param pp_ga: (list) pareto scores of NSGA-II
	"""

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	#hco - red
	ax.scatter(pp_hco[:,0],pp_hco[:,1],pp_hco[:,2],color='red')
	triang = mtri.Triangulation(pp_hco[:, 0], pp_hco[:, 1])
	ax.plot_trisurf(triang, pp_hco[:, 2], color='red')

	#sa - blue
	ax.scatter(pp_sa[:,0],pp_sa[:,1],pp_sa[:,2],color='blue')
	triang = mtri.Triangulation(pp_sa[:, 0], pp_sa[:, 1])
	ax.plot_trisurf(triang, pp_sa[:, 2], color='blue')

	#ts - green
	ax.scatter(pp_ts[:,0],pp_ts[:,1],pp_ts[:,2],color='green')
	triang = mtri.Triangulation(pp_ts[:, 0], pp_ts[:, 1])
	ax.plot_trisurf(triang, pp_ts[:, 2], color='green')

	#ga - pink
	ax.scatter(pp_ga[:,0],pp_ga[:,1],pp_ga[:,2],color='pink')
	triang = mtri.Triangulation(pp_ga[:, 0], pp_ga[:, 1])
	ax.plot_trisurf(triang, pp_ga[:, 2], color='pink')
	plt.show()
	return