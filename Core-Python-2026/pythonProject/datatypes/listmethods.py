# Example with List
from unicodedata import numeric

list = [5, "hello", 3.14, True, 10, "world", False, 25, 10, 30]
#print(list)

# # append() - Adds an element at the end of the list
#list.append(35)
print("List After Append",list)
#
#
# # clear() - Removes all items from the list
#list.clear()
#print('list after clear', list)
#
#
# # copy() - Returns a shallow copy of the list
# list = [5, "hello", 3.14, True, 10, "world", False, 25, 10, 30]
# list_copy = list.copy()
# print("List copy:", list_copy)
# list.clear()
# print(list)
# print(list_copy)
#
# # extend() - Adds all elements of an iterable (like a list) to the end of the list
# list.extend([40, "new_element", 50.5])
# print("List after extend([40, 'new_element', 50.5]):", list)
#
#
#
# # insert() - Inserts an element at the specified index
# list.insert(2,"inserted_value")
# print("List after insert(2, 'inserted_value'):", list)
#
#
# # pop() - Removes  last elmen  in list (default is the last item)
removed_item = list.pop()
print(list)
removed_item= list.pop()
print(list)
#
# # remove() - particular koi elements remove krna ho to
# list.remove("inserted_value")
# print('list after remove(inserted_value)',list)
#
# # reverse() - Reverses krta hai list ko
# list.reverse()
# print('list after reverse().',list)
#
#
# #, sort() - Sorts the list in ascending order
# # Note: Isme error aayega kyunki list me mixed data types hain (jaise int aur str).
# # Sorting sahi se dikhane ke liye hum sirf numeric elements wali list use karenge.
#
# numeric_list=[7,8,9,58,2,1]
#
# numeric_list.sort()
# print("numeric after sort list ",numeric_list)