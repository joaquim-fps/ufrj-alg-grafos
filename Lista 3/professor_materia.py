def get_sizes():
	sizes = input().split()

	return int(sizes[0]), int(sizes[1]), int(sizes[2])

def get_relations(num_relations):
	global relations_matrix

	for k in range(0, num_relations):
		relation = input().split()

		professor = int(relation[0])
		subject   = int(relation[1])

		relations_matrix[professor][subject] = 1

def match_professor_to_subjects(professor, chosen_professor, seen):
	for subject in range(0, num_subjects):
		if seen[subject] or (not(relations_matrix[professor][subject])):
			continue

		seen[subject] = True

		if chosen_professor[subject] == None or match_professor_to_subjects(chosen_professor[subject], chosen_professor, seen):
			chosen_professor[subject] = professor
			return True

		return False

def find_happiness():
	global num_professors, num_subjects
	global relations_matrix

	num_professors, num_subjects, num_relations = get_sizes()

	relations_matrix = [[0 for m in range(0, num_subjects)] for n in range(0, num_professors)]
	get_relations(num_relations)

	hapinness = 0
	chosen_professor = [None for i in range(0, num_subjects)]

	for professor in range(0, num_professors):
		seen = [False for j in range(0, num_subjects)]
		
		if match_professor_to_subjects(professor, chosen_professor, seen):
			hapinness = hapinness + 1

	return hapinness
