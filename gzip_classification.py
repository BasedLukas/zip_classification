
import gzip
from zip_implementation import Zip

def print_results():
    print("CompA: ", CompA)
    print("CompB: ", CompB)
    print("CompA_Unknown: ", CompA_Unknown)
    print("CompB_Unknown: ", CompB_Unknown)
    print("A_Diff: ", A_Diff)
    print("B_Diff: ", B_Diff)

    # get the min diff and print the category
    if A_Diff < B_Diff:
        print("StringUnknown is in GroupA")
    else:
        print("StringUnknown is in GroupB")  
    

GroupA = "This group is part of the business category. In these sentences we speak about profit, EBITDA and taxes."

GroupB = "Science category. In these sentences we speak about physics, chemistry, and other science related terms."

StringUnknown = "This is a sentence that we want to classify. It is a business sentence, we mention EBITDA, profit and taxes."


CompA = len(gzip.compress(bytes(GroupA, 'utf-8')))
CompB = len(gzip.compress(bytes(GroupB, 'utf-8')))

CompA_Unknown = len(gzip.compress(bytes(GroupA + StringUnknown, 'utf-8')))
CompB_Unknown = len(gzip.compress(bytes(GroupB + StringUnknown, 'utf-8')))

A_Diff = CompA_Unknown - CompA
B_Diff = CompB_Unknown - CompB

print("Using gzip")
print_results()
print()


z = Zip(return_type='binary', window_size=1000, lookahead_buffer_size=50)
CompA = len(z.compress(GroupA)[0])
CompB = len(z.compress(GroupB)[0])
CompA_Unknown = len(z.compress(GroupA + StringUnknown)[0])
CompB_Unknown = len(z.compress(GroupB + StringUnknown)[0])
A_Diff = CompA_Unknown - CompA
B_Diff = CompB_Unknown - CompB

print("Now using our custom implementation")
print_results()