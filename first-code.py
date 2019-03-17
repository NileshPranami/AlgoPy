def firstFun(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Maths', 'Art']
info = {'name': 'John', 'age': 22}
firstFun(*courses, **info)
