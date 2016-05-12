gradeBook = [[100, 94, 87, 33, 87],
			[95, 0, 85, 70, 99],
			[90, 91, 95, 93, 89]]

#calculate student 1 averages
def student_average(gradeBook):
	overallAverages = []
	for row in gradeBook:
		average = 0
		for item in row:
			average += item
		average = average / len(row)
		overallAverages.append(average)

	for i in range(3):
		print("student 1 average is: {}".format(student_average(overallAverages[i])))
		print("student 2 average is: {}".format(student_average(overallAverages[i + 1])))
		print("student 3 average is: {}".format(student_average(overallAverages[i + 2])))


final = student_average(gradeBook)
print(final)