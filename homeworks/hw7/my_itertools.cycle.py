my_list = [1, 2, 3, 4]
def my_iterator(iter_obj):
    while True:
        for i in iter_obj:
            yield i

# for itr in my_iterator(my_list):
#     print(itr)
