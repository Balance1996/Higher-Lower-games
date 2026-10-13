#HL_tracer
def trace():
    return print("""
Higher Lower — State Change Trace
Case 1: A wins
Assume A has 800 followers and B has 500 followers.
Step	current_contender (A)	challenger (B)
1. Before guess	A (800)	B (500)
2. A wins	A (800)	B (500)
3. Select new B	A (800)	New B (≠ 800)
Code:
if user_choice == "A":
    challenger = available_contender(current_contender)



Remember: A stays. Only B changes.

Case 2: B wins
Assume A has 500 followers and B has 800 followers.
Step	current_contender (A)	challenger (B)
1. Before guess	A (500)	B (800)
2. Promote B to A	B (800)	B (800) temporarily
3. Select new B	B (800)	New B (≠ 800)
Code:
elif user_choice == "B":
    current_contender = challenger
    challenger = available_contender(current_contender)



Remember: B becomes A first. Then select a new B.

The order matters

A wins
Keep A → replace B




B wins
Promote B to A → replace B




""")