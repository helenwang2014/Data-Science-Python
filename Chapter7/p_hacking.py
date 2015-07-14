import random

def run_experiment():
	return [random.random() < 0.5 for _ in range(1000)]

def reject_fairness(experiment):
	num_heads = len([flip for flip in experiment if flip])
	return num_heads < 469 or num_heads > 531

random.seed(0)
experiments = [run_experiment() for _ in range(1000)]
num_rejections = len([experiment 
					   for experiment in experiments
					   if reject_fairness(experiment)])
print num_rejections

