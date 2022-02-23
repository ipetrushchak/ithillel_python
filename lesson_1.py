input_names = "Mira Mira Mira Maya Lena  Maya Lusya Maksimus Maya"
famyly_namber = {}
for famyly in input_names.split():
    try:
        famyly_namber[famyly] += 1
    except KeyError:
        famyly_namber[famyly] = 1
print(famyly_namber)