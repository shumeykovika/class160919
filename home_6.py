# Функция нахождения мин и макс в списке

numbers=[1,2,6,5,3,6]

def minmax(list):
	max_num = numbers[0]
	min_num = numbers[0]
	for num in numbers:
		if num < min_num:
			min_num = num
		if num > max_num:
			max_num = num
	return(min_num, max_num)
	
print(minmax(numbers))


#Создать словарь оценок предполагаемых студентов (Ключ - ФИ студента). Найти самого успешного и самого отстающего по среднему баллу.

d2 = {
	'Kate': [11, 10, 12],
	'John': [10, 11, 9],
	'Bill': [8, 9, 7], 
	'Flavia': [12, 12, 12],
	'Jane': [5, 6, 7], 
	'Peter': [11, 11, 11]
}

def middle (dictionary):
	sum_marks = list(map(sum, dictionary.values())) # выводит список общего балла у каждого студента
	
	middle = []
	for i in sum_marks:
		middle.append(i/3)
	return(middle) # список среднего балла студентов

print(middle(d2))

# ответ: [11.0, 10.0, 8.0, 12.0, 6.0, 11.0]

# Др.вариант, где оценок может быть не только 3
def middle (dictionary):
	middle = []
	for key,values in dictionary.items():
		dictionary[key] = sum(values)/len(values)
		middle.append(dictionary[key])
	return(middle) # список среднего балла студентов

print(middle(d2))


d = {
 "Ivanoff": [1, 2, 2],
 "Petroff": [4, 5, 5],
 "Sidoroff": [7, 8, 9]
}

def maxmin(rangs):
	for key, val in rangs.items():
  		rangs[key] = sum(val)/len(val)
 return {'max': max(rangs), 'min': min(rangs)}

print(maxmin(d))

