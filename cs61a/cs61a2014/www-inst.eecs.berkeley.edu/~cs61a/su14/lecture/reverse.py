# Reverse takes in a linked list and returns a
# new linked list with all the elements reversed

# WITHOUT USING INSERT_END
def reverse(linked_list):
  """ Reverse takes in a linked list and returns
      a new linked list with all of the elements
      reversed
      >>> x = link(1, link(2, (link(3, empty))))
      >>> y = reverse(x)
      >>> print_linked_list(y)
      < 3 2 1 >
    
   """
   # DOMAIN: linked list
   # RANGE: linked list
   def helper(lst, result):
     if lst == empty:
       return result
     f, r = first(lst), rest(lst)
     return helper(r, link(f, result))
   return helper(linked_list, empty)

""" HOW HELPER WORKS

Assume reverse(< 1 2 3>), then

        lst      result
helper(< 1 2 3 >, <> )
helper(< 2 3 >, < 1 >)
helper(< 3 >, < 2 1 >)
helper(<>, < 3 2 1 >)
< 3 2 1 >
"""


